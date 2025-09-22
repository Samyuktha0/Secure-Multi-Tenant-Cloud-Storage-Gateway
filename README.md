# Secure Multi-Tenant Cloud Storage Gateway

A scalable, secure gateway for multi-tenant cloud storage with S3-compatible APIs, encryption, and role-based access control.

## Features
- S3-compatible API endpoints
- AES encryption for data at rest
- TLS termination via Nginx
- Tenant isolation and IAM-style access control
- MongoDB metadata store and Redis caching

## Setup
```bash
pip install -r requirements.txt
python gateway/app.py
