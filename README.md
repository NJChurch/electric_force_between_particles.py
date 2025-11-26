# Coulomb's Law Calculator (CLI)

A simple command-line Python tool to compute the electric force between two point charges using Coulomb's Law. The program continuously prompts for input until the user chooses to exit, validating inputs and indicating whether the force is attractive or repulsive.

## Features

- Interactive CLI: repeatedly calculates until you choose to exit
- Validates input types and ensures distance is greater than zero
- Automatically determines and reports whether the force is attractive or repulsive
- Uses precise Coulomb’s constant: `k_e = 8.9875517923e9 N·m²/C²`

## Requirements

- Python 3.8+

## Installation

1. Ensure Python 3.8+ is installed.
2. Save the script as `coulomb_calculator.py` (or any name you prefer).

## Usage

Run the script:

```bash
python coulomb_calculator.py
```

You will be prompted for:
- `Enter the charge of the first particle (in Coulombs):` — e.g., `1e-6`
- `Enter the charge of the second particle (in Coulombs):` — e.g., `-2e-6`
- `Enter the distance between the two particles (in meters):` — e.g., `0.05`

Example output:
```
The electric force between the two particles is 7.19 Newtons (attractive force).
Do you want to calculate again? (yes/no):
```

## How It Works

Coulomb’s Law:
- Magnitude: `F = k_e * |q1 * q2| / r^2`
- Direction:
  - If `q1 * q2 > 0`, the force is repulsive (same sign charges).
  - If `q1 * q2 < 0`, the force is attractive (opposite sign charges).

The program:
- Converts inputs to floats and checks `r > 0`.
- Computes the force magnitude with `k_e = 8.9875517923e9`.
- Reports “repulsive” or “attractive” based on the sign of `q1 * q2`.
- Handles invalid numeric inputs gracefully.

## Notes and Tips

- Units:
  - Charges in Coulombs (C)
  - Distance in meters (m)
  - Force output in Newtons (N)
- If you often work with microcoulombs (μC), remember `1 μC = 1e-6 C`.
- For very small distances or large charges, the computed force can be large—ensure inputs are physically reasonable.

## License

MIT License (recommended). Add a `LICENSE` file to specify your chosen license.