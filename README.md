# Soil Monitoring System

A Raspberry Pi and Python-based soil monitoring project designed to
monitor soil conditions and support data-driven irrigation decisions.

## Overview

The system combines Raspberry Pi sensor monitoring with analysis of
soil-moisture data.

The Raspberry Pi component demonstrates real-time sensor monitoring,
while the dataset analysis component explores historical soil-moisture
measurements collected from a field-scale sensor network.

## Objectives

- Monitor soil conditions using Raspberry Pi sensors
- Collect and record soil-monitoring readings
- Analyze historical soil-moisture measurements
- Study moisture variation at different soil depths
- Support irrigation decisions based on observed soil conditions
- Reduce unnecessary water usage through condition-based monitoring

## Project Architecture

```text
                 Soil Monitoring System
                          |
            +-------------+-------------+
            |                           |
      Raspberry Pi                 Historical Data
      Sensor System                Analysis
            |                           |
      Sensor Readings             Kaggle Dataset
            |                           |
            +-------------+-------------+
                          |
                    Data Processing
                          |
                   Soil Moisture
                       Analysis
                          |
                Irrigation Support