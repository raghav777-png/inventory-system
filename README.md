# inventory-system
# Inventory & Asset Tracking System

## Overview
A command-line based inventory management system developed using Python and SQLite.

This system simulates structured asset tracking workflows used in operational and industrial environments.

## Key Features
- Add, update, and delete inventory records
- Persistent storage using SQLite
- Input validation and defensive programming
- Structured logging system for activity tracking
- Error handling for invalid inputs and database failures

## Technical Architecture
- Python 3
- SQLite database
- Logging module
- Modular function design
- CLI-based user interface

## Edge Case Handling
- Prevents negative quantities
- Prevents empty input fields
- Handles invalid ID updates/deletions
- Catches database connection errors

## How to Run

1. Clone the repository
2. Navigate to project directory
3. Run:

   python inventory_system.py

Database will be created automatically on first run.

## Future Enhancements
- GUI version
- Role-based authentication
- CSV export support
- Multi-user capability
