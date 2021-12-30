# ASD_16S_metaanalysis
Meta-analysis of 16S microbiome studies for Autism Spectrum Disorder
##### Primary authors: Aries Chavira, Robert Mills, and Eric Hou-Jen Wang (Precidiag Inc. 2021)

This repo contains the scripts and notebooks to reproduce the analysis from Chavira 2022 (in prep).

## Outline of Directories

### Data. Contains the relevant data and metadata
- Contains raw AmericanGut dataset

### Figure 1. PRISMA flow chart and cohort demographics
- Preprocessing of Amergican Gut data, propensity scoring matching, and feature distributions (amgut_processing_distributions.ipynb)
- Extended Data Figure 1. Comparison of ASD and control demographics from data compiled from the American gut project

### Figure 2. Association of ASD status to microbiome alpha and beta-diversity
- Extended Data Figure 2. Principal coordinate analysis of samples by status
- Extended Data Figure 3. Principal coordinate analysis of samples colored by study design factors

### Figure 3. Taxonomic and functional differences between ASD and controls
- Extended Data Figure 4. Extended taxonomic and functional differences between ASD and controls by cohort

### Figure 4. Comparing machine learning performance on ASD status prediction
- Extended Data Figure 5. Adaboost and decision tree classifier performance on ASD status prediction

### Figure 5. Evaluating study design factors that influence the performance of machine learning models and taxonomic abundance
- Extended Data Figure 6. Evaluating the influence relationship between of sample size and predictive accuracy at different age ranges 

### Supplementary Figures
- Supplementary Figure 1. Effect of sequencing depth on ASD/NT phylum abundance
- Supplementary Figure 2. Effect of sequencing depth on ASD/NT class abundance
- Supplementary Figure 3. Effect of sequencing depth on ASD/NT order abundance
- Supplementary Figure 4. Effect of sequencing depth on ASD/NT genus abundance
- Supplementary Figure 5. Effects of country on ASD/NT phylum abundance
- Supplementary Figure 6. Effects of country on ASD/NT class abundance
- Supplementary Figure 7. Effects of country on ASD/NT order abundance
- Supplementary Figure 8. Effects of country on ASD/NT genus abundance
- Supplementary Figure 9. Effects of control type on ASD/NT phylum abundance
- Supplementary Figure 10. Effects of control type on ASD/NT class abundance
- Supplementary Figure 11. Effects of control type on ASD/NT order abundance
- Supplementary Figure 12. Effects of control type on ASD/NT genus abundance

### utils. Contains the relevant utility functions and classes
