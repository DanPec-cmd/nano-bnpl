# Nano BNPL

A lightweight Python implementation of a Buy Now, Pay Later (BNPL) system.

## Overview

**Nano BNPL** is a minimal, efficient implementation of a Buy Now, Pay Later payment platform. This project provides core BNPL functionality with a focus on simplicity and performance.

## Features

- 💳 Core BNPL payment processing
- 🔄 Payment installment management
- 📊 Transaction tracking
- 🐳 Docker support for easy deployment

## Tech Stack

- **Language**: Python (98.6%)
- **Containerization**: Docker (1.4%)

## Getting Started

### Prerequisites

- Python 3.8+
- pip or poetry
- Docker (optional, for containerized deployment)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/DanPec-cmd/nano-bnpl.git
cd nano-bnpl
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

#### Local Development
```bash
python main.py
```

#### Docker
```bash
docker build -t nano-bnpl .
docker run -it nano-bnpl
```

## Project Structure

```
nano-bnpl/
├── README.md
├── Dockerfile
├── requirements.txt
├── main.py
└── [source files]
```

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open source and available under an appropriate license.

## Contact

For more information, visit the [GitHub repository](https://github.com/DanPec-cmd/nano-bnpl).

---

**Status**: Active Development

