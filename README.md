# Web Scraper Package

This package contains classes and modules for web scraping tasks.

## Contents

1. [Introduction](#introduction)
2. [WebScraper Class](#webscraper-class)
3. [PdfReader Class](#pdfreader-class)
4. [Requirements](#requirements)

---

## Introduction

Web scraping is the process of extracting data from websites. This package provides functionality to scrape content from web pages and PDF files.

## WebScraper Class

The `WebScraper` class in the `scraper.py` module is responsible for scraping content from web pages. It adheres to the following SOLID principles:

### Single Responsibility Principle (SRP)

- The class is responsible for handling web scraping tasks and error handling related to scraping.

### Open/Closed Principle (OCP)

- The class is open for extension, allowing additional features to be added without modifying existing code.

### Interface Segregation Principle (ISP)

- The class provides methods specifically for web scraping, avoiding unnecessary dependencies.

### Dependency Inversion Principle (DIP)

- The class depends on abstractions (requests library, BeautifulSoup) rather than concrete implementations, allowing flexibility and ease of maintenance.

### Defensive Programming

- The class includes error handling to handle unexpected situations gracefully, providing feedback on encountered issues.

## PdfReader Class

The `PdfReader` class in the `pdf_reader.py` module is responsible for reading text content from PDF files. It adheres to the following SOLID principles:

### Single Responsibility Principle (SRP) -

- The class is responsible for handling PDF file reading tasks and error handling related to reading.

### Open/Closed Principle (OCP) -

- The class is open for extension, allowing additional features to be added without modifying existing code.

### Interface Segregation Principle (ISP) -

- The class provides methods specifically for reading PDF files, avoiding unnecessary dependencies.

### Dependency Inversion Principle (DIP) -

- The class depends on abstractions (PyPDF2 library) rather than concrete implementations, allowing flexibility and ease of maintenance.

### Defensive Programming -

- The class includes error handling to handle unexpected situations gracefully, providing feedback on encountered issues.

## Requirements

The package requires the following external libraries, which can be installed using pip:
