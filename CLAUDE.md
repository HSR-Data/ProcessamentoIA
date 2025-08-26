# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a research-focused Python project for AI-powered data processing in market research ("ProcessamentoIA - Ferramentas IA para processamento de dados para pesquisa de mercado"). The project focuses on document processing and data analysis for research purposes.

## Repository Structure

- `utils/` - Utility scripts for document processing
- `dados/` - Data directory containing:
  - `bancos/` - Database files (.sav format)
  - `questionarios/` - Research questionnaires (PDF and DOCX formats)

## Core Components

### Document Processing
- **Primary tool**: `utils/runDocling.py` - Uses the Docling library to convert PDF documents to Markdown format
- **Key functionality**: PDF-to-Markdown conversion with UTF-8 encoding support

## Key Dependencies

- `docling` - Document conversion library for PDF processing
- Standard Python libraries for file I/O operations

## Common Development Tasks

### Document Processing
```bash
# Run the main document processing script
python utils/runDocling.py
```

The script converts PDF files (like "qt2.pdf") to Markdown format and saves the output as text files with UTF-8 encoding.

## Data Handling Notes

- Research data is stored in SPSS format (.sav files)
- Questionnaires are available in both PDF and original DOCX formats
- All text output uses UTF-8 encoding to handle special characters properly