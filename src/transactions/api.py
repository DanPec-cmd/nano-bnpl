from ninja import NinjaAPI, Schema
from django.shortcuts import get_object_or_404
from .models import Transaction, Customer, BNPLPlan
from decimal import Decimal
from ninja import Schema

# 1. Define a response schema for clean JSON output
class PlanDetailSchema(Schema):
    id: str
    remaining_amount: float
    status: str
    installments_total: int

@api.get("/plans/{plan_id}", response=PlanDetailSchema)
def get_plan(request, plan_id: str):
    plan = get_object_or_404(BNPLPlan, id=plan_id)
    return plan

api = NinjaAPI()

# Pydantic schema for validation
class TransactionSchema(Schema):
    customer_id: str
    amount: float

@api.post("/transactions")
def create_transaction(request, payload: TransactionSchema):
    # Fetch the customer
    customer = get_object_or_404(Customer, id=payload.customer_id)
    
    # Create the transaction
    tx = Transaction.objects.create(
        customer=customer,
        amount=Decimal(str(payload.amount)),
        status='PENDING'
    )
    
    return {"id": str(tx.id), "status": tx.status}



@api.post("/transactions/{transaction_id}/activate")
def activate_bnpl(request, transaction_id: str):
    # 1. Fetch the transaction
    tx = get_object_or_404(Transaction, id=transaction_id)
    
    # 2. Risk Check (The "Twisto" Logic)
    if tx.customer.credit_limit < tx.amount:
        return {"error": "Insufficient credit limit"}
    
    # 3. Create the BNPL Plan
    plan = BNPLPlan.objects.create(
        transaction=tx,
        remaining_amount=tx.amount,
        status='ACTIVE'
    )
    
    # 4. Update the transaction status
    tx.status = 'COMPLETED'
    tx.save()
    
    return {"plan_id": str(plan.id), "message": "BNPL Plan Activated!"}