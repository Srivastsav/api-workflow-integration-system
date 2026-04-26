# API Workflow Integration System

## System Overview
This project demonstrates how a workflow automation system can be implemented programmatically using APIs.

## System Model
Input → API → Validation → Processing → Storage → Response

## Features
- Create leave request via API
- Validate input fields
- Store requests in system
- Retrieve all requests

## API Endpoints

### Create Request
POST /leave-request

### Get Requests
GET /requests

## Architecture
- API Layer: Flask
- Logic Layer: Python
- Data Layer: In-memory storage

## Business Value
- Demonstrates transition from low-code workflows to API-based systems
- Shows ability to implement workflow logic programmatically

## Skills Demonstrated
- API development
- Workflow implementation
- Input validation
- System design
