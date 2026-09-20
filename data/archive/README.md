# Soil Moisture Dataset

This directory contains documentation for the soil moisture dataset used
for analysis in the Soil Monitoring System project.

## Dataset Source

The dataset was obtained from Kaggle:

https://www.kaggle.com/datasets/sathyanarayanrao89/soil-moisture-data-from-field-scale-sensor-network

## Dataset

**Name:** Soil Moisture data from field scale sensor network

The dataset contains soil water content and temperature measurements
collected from a field-scale sensor network.

## Data Organization

The original dataset contains two main groups:

- Daily measurements
- Hourly measurements

The dataset contains sensor readings from multiple locations.

## Measurements

### Volumetric Water Content

Soil moisture measurements are represented using volumetric water content
at different depths:

- `VW_30cm`
- `VW_60cm`
- `VW_90cm`
- `VW_120cm`
- `VW_150cm`

The measurements represent volumetric water content in `m³/m³`.

### Temperature

Temperature measurements are available at:

- `T_30cm`
- `T_60cm`
- `T_90cm`
- `T_120cm`
- `T_150cm`

Temperature values are measured in degrees Celsius.

## Date Range

The dataset description covers measurements from:

`2007-04-20` to `2016-06-16`

## Usage in This Project

The dataset is used for:

- Soil moisture analysis
- Monitoring moisture levels at different depths
- Exploring changes in soil moisture over time
- Understanding relationships between soil moisture and temperature
- Supporting the analysis component of the soil monitoring project

The dataset is used for analysis and does not represent direct Raspberry Pi
sensor readings.

## Dataset Files

The original Kaggle dataset contains sensor files organized into Daily and
Hourly collections.

The complete dataset is not stored in this GitHub repository because of
its large size.

## License

The Kaggle dataset is listed as **CC0: Public Domain** on its dataset page.

Please refer to the original Kaggle dataset page for complete metadata,
provenance, and licensing information.