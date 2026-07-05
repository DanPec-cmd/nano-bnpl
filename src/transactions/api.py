from ninja import NinjaAPI, Schema
from django.shortcuts import get_object_or_404
from .models import Transaction, Customer, BNPLPlan
from decimal import Decimal
from typing import List

api = NinjaAPI()

# Schemas
class TransactionSchema(Schema):
    customer_id: str
    amount: float

class RepaymentSchema(Schema):
    amount: float

class PlanDetailSchema(Schema):
    id: str
    remaining_amount: float
    status: str
    installments_total: int

class PlanSummarySchema(Schema):
    id: str
    remaining_amount: float
    status: str

# Endpoints
@api.post("/transactions")
def create_transaction(request, payload: TransactionSchema):
    customer = get_object_or_404(Customer, id=payload.customer_id)
    tx = Transaction.objects.create(
        customer=customer,
        amount=Decimal(str(payload.amount)),
        status='PENDING'
    )
    return {"id": str(tx.id), "status": tx.status}

@api.post("/transactions/{transaction_id}/activate")
def activate_bnpl(request, transaction_id: str):
    tx = get_object_or_404(Transaction, id=transaction_id)
    if tx.customer.credit_limit < tx.amount:
        return {"error": "Insufficient credit limit"}
    plan = BNPLPlan.objects.create(
        transaction=tx,
        remaining_amount=tx.amount,
        status='ACTIVE'
    )
    tx.status = 'COMPLETED'
    tx.save()
    return {"plan_id": str(plan.id), "message": "BNPL Plan Activated!"}

@api.get("/plans/{plan_id}", response=PlanDetailSchema)
def get_plan(request, plan_id: str):
    plan = get_object_or_404(BNPLPlan, id=plan_id)
    return plan

@api.post("/plans/{plan_id}/repay")
def repay_plan(request, plan_id: str, payload: RepaymentSchema):
    plan = get_object_or_404(BNPLPlan, id=plan_id)
    payment_amount = Decimal(str(payload.amount))
    
    if payment_amount <= 0:
        return {"error": "Payment amount must be positive"}
    if payment_amount > plan.remaining_amount:
        return {"error": f"Payment exceeds remaining balance of {plan.remaining_amount}"}
    
    plan.remaining_amount -= payment_amount
    if plan.remaining_amount == 0:
        plan.status = 'PAID'
    plan.save()
    
    return {
        "message": "Payment successful",
        "remaining_balance": float(plan.remaining_amount),
        "status": plan.status
    }


@api.get("/customers/{customer_id}/plans", response=List[PlanSummarySchema])
def list_customer_plans(request, customer_id: str):
    # This queries all plans where the transaction belongs to this customer
    return BNPLPlan.objects.filter(transaction__customer_id=customer_id)