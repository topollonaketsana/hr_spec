__________________________________________________________________________________________________________________________________________________

## The theory behind HR-spec
This document explains the scientific foundation for the HR-Spec package. It covers the Hertzsprung–Russell diagram, stellar evolution, physical scaling laws, and the motivation for applying machine learning in stellar classification.

## The HR diagram
The **HR Diagram** is an important tool in astrophysics that models stars according to:
- Surface Temperature (in Kelvin), decreasing to the right.
- Luminosity (in solar units, $L_\odot $)

## Stellar stages on the HR Diagram:

| Stage             | Description                                         |
|-------------------|-----------------------------------------------------|
| Main Sequence     | Where stars spend most of their lives burning H     |
| Red Giants        | Cool but very luminous — evolved stars              |
| White Dwarfs      | Hot but dim — leftover cores of low-mass stars      |
| Supergiants       | Bright, massive stars at end of life                |


## Stellar Life Cycle 

A star's evolution depends highly on its **mass**. Here’s a simplified process for life of a star:

- **Birth**: Collapse of a gas cloud → protostar
- **Main Sequence**: H-burning in core
- **Post-MS**:
  - Low mass → Red Giant → Planetary Nebula → White Dwarf
  - High mass → Red Supergiant → Supernova → Neutron Star / Black Hole

_________________________________________________________________________________________________________________________________________________

## Physical relations (scalling)

### Luminosity–Mass Relation:


$L \propto M^{3.5}$

For most main-sequence stars, luminosity increases rapidly with mass.

### Radius–Mass Relation:


$R \propto M^{0.5}$






### Lifetime Estimate:

$
\tau \propto \frac{1}{M^{2.5}} \quad \text{(approximation)}
$

In HR-Spec we include the metalisity z:

$
\tau \approx \frac{10}{M} \cdot (1 - 0.1 \cdot Z)
$

Where:
- $M$ = stellar mass (solar units)
- $Z$ = metallicity
- $\tau$ = main-sequence lifetime (Gyr)






___________________________________________________________________________________________________________________________________________________
