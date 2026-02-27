# PHYS 263: University Physics III Laboratory
**George Mason University | Spring 2026**

## Course Overview
[cite_start]This repository contains the experimental designs, data visualizations, and statistical analyses completed for the University Physics III Laboratory[cite: 1, 10]. [cite_start]The course emphasizes four key aspects of experimental physics: designing experiments, developing technical laboratory skills, analyzing data using high-level programming (Python), and communicating results[cite: 10, 15, 17].

## Core Competencies
* [cite_start]**Experimental Design**: Engineering and troubleshooting experiments within constraints such as cost, time, and safety[cite: 13].
* [cite_start]**Data Analysis & Visualization**: Utilizing **Python** to interpret the validity, limitations, and uncertainties of results[cite: 15].
* [cite_start]**Scientific Programming**: Implementing numerical methods (NumPy) to characterize physical phenomena and filter sensor noise[cite: 28].
* [cite_start]**Technical Communication**: Presenting evidence-based arguments through formal written reports and oral presentations[cite: 17].

## Exercise Units
[cite_start]The following units represent the core curriculum and the evolution of the experimental data tracked in this repository[cite: 25]:

1. **Measurement, Uncertainty, and Scientific Programming**
   - [cite_start]Introduction to statistical methods and Python-based data characterization[cite: 26].
2. **Characterizing the Atmosphere**
   - Analysis of atmospheric variables and sensor calibration using mobile hardware.
3. **Pressure and Temperature**
   - [cite_start]Experimental verification of the Ideal Gas Law ($PV=nRT$) using a sealed 4200 mL fixed-volume system[cite: 25].
   - **Key Analysis**: Accounted for the displacement volume of 6 smartphones (approx. 831 mL) to calculate the true gas volume ($V_{gas} \approx 3369 \text{ mL}$).
4. **Total Internal Reflection**
   - [cite_start]Investigating the boundary conditions of light at refractive interfaces[cite: 25].
5. **Calibrating a Function Generator**
   - [cite_start]Signal analysis and equipment precision testing[cite: 25].
6. **Measuring a Refractive Index**
   - [cite_start]Determining optical properties of various media[cite: 25].
7. **Light Intensity and Distance**
   - [cite_start]Mapping the inverse-square law for electromagnetic radiation[cite: 25].

## Methodology & Uncertainty
Every quantitative measurement in this repository is defined by an interval of uncertainty, following the standards outlined in the lab manual:
* [cite_start]**Type A Uncertainty**: Evaluated through statistical analysis of repeated measurements ($s_{\bar{x}} = s/\sqrt{N}$)[cite: 15].
* **Type B Uncertainty**: Evaluated through scientific judgment, instrument specifications, and environmental systematic effects (e.g., heat radiation from hardware or volume displacement).
* **Data Cleaning**: Implemented moving averages (convolution) and strategic slicing to isolate "clean" linear trends from initial setup noise and end-of-trial systematic spikes.

## Technology Stack
* **Language**: Python 3.11.9 (managed via `pyenv`)
* **Libraries**: 
  - **NumPy**: For data slicing, mathematical convolution, and statistical calculations.
  - **Matplotlib**: For generating publication-quality scientific plots.
* **Tools**: VS Code, Git/GitHub for Version Control.

---
[cite_start]**Instructor**: Frank Cline [cite: 2]  
**Author**: Daksh Khandelwal  
[cite_start]**Institution**: George Mason University [cite: 1]
