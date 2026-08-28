import math


def calculate_bracket_design(
    load_kg,
    safety_factor=2.0,
    material="Steel"
):
    """
    Calculate a starting design for a simple cantilever L-bracket.

    IMPORTANT:
    This is a preliminary sizing calculation, not a final
    structural certification.
    """

    # --------------------------------------------------
    # Material properties
    # --------------------------------------------------

    materials = {
        "Steel": {
            "yield_strength_mpa": 250
        },
        "Aluminium 6061": {
            "yield_strength_mpa": 276
        }
    }

    material_data = materials.get(
        material,
        materials["Steel"]
    )

    yield_strength = material_data["yield_strength_mpa"]

    # --------------------------------------------------
    # Convert mass to force
    # F = m × g
    # --------------------------------------------------

    gravity = 9.81

    force = load_kg * gravity

    # --------------------------------------------------
    # Apply safety factor
    # --------------------------------------------------

    design_force = force * safety_factor

    # --------------------------------------------------
    # Initial geometry assumptions
    # --------------------------------------------------

    bracket_width = 100.0
    bracket_height = 60.0
    base_depth = 40.0

    # Load arm
    load_arm = base_depth

    # --------------------------------------------------
    # Allowable bending stress
    # --------------------------------------------------

    allowable_stress = yield_strength / safety_factor

    # --------------------------------------------------
    # Required section modulus
    #
    # Z = M / sigma
    # M = F × L
    # --------------------------------------------------

    bending_moment = design_force * load_arm

    required_section_modulus = (
        bending_moment / allowable_stress
    )

    # --------------------------------------------------
    # Estimate thickness
    #
    # For a rectangular section:
    #
    # Z = b × t² / 6
    #
    # Solve:
    #
    # t = sqrt(6Z / b)
    # --------------------------------------------------

    width_for_section = bracket_width

    thickness = math.sqrt(
        (6 * required_section_modulus)
        / width_for_section
    )

    # Round up to a practical manufacturing value
    practical_thicknesses = [
        3,
        4,
        5,
        6,
        8,
        10,
        12,
        15,
        20
    ]

    selected_thickness = practical_thicknesses[-1]

    for t in practical_thicknesses:
        if t >= thickness:
            selected_thickness = t
            break

    # --------------------------------------------------
    # Return engineering design
    # --------------------------------------------------

    return {
        "load_kg": load_kg,
        "force_N": round(force, 2),
        "design_force_N": round(design_force, 2),
        "safety_factor": safety_factor,
        "material": material,
        "yield_strength_MPa": yield_strength,
        "allowable_stress_MPa": round(
            allowable_stress,
            2
        ),
        "bending_moment_Nmm": round(
            bending_moment,
            2
        ),
        "required_section_modulus_mm3": round(
            required_section_modulus,
            2
        ),
        "width_mm": bracket_width,
        "height_mm": bracket_height,
        "base_depth_mm": base_depth,
        "calculated_thickness_mm": round(
            thickness,
            2
        ),
        "selected_thickness_mm": selected_thickness
    }


if __name__ == "__main__":

    result = calculate_bracket_design(
        load_kg=5,
        safety_factor=2,
        material="Steel"
    )

    print("\n" + "=" * 50)
    print("AI CAD ENGINEER")
    print("PRELIMINARY ENGINEERING DESIGN")
    print("=" * 50)

    for key, value in result.items():
        print(f"{key}: {value}")
