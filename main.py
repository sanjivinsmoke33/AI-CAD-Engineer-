import sys
import json

sys.path.append("src")

from ai.requirements import parse_requirement
from engineering.calculations import calculate_bracket_design
from catia.generator import connect_to_catia, create_l_bracket


def main():

    print("=" * 65)
    print("              AI CAD ENGINEER")
    print("=" * 65)

    print("\nDescribe the component you want to design.")
    print("Example:")
    print("  I want a bracket that can hold 5 kg\n")

    user_request = input("> ")

    # ==========================================================
    # STEP 1 — AI UNDERSTANDS USER
    # ==========================================================

    print("\n🧠 Understanding engineering requirement...")

    requirements = parse_requirement(user_request)

    print("\nAI REQUIREMENTS")
    print("-" * 40)

    print(json.dumps(requirements, indent=4))


    # ==========================================================
    # STEP 2 — ENGINEERING CALCULATIONS
    # ==========================================================

    print("\n⚙️ Running engineering calculations...")

    design = calculate_bracket_design(

        load_kg=float(
            requirements["load_kg"]
        ),

        safety_factor=float(
            requirements["safety_factor"]
        ),

        material=requirements["material"]
    )


    print("\nENGINEERING DESIGN")
    print("-" * 40)

    print(
        f"Load: "
        f"{design['load_kg']} kg"
    )

    print(
        f"Force: "
        f"{design['force_N']} N"
    )

    print(
        f"Material: "
        f"{design['material']}"
    )

    print(
        f"Width: "
        f"{design['width_mm']} mm"
    )

    print(
        f"Height: "
        f"{design['height_mm']} mm"
    )

    print(
        f"Depth: "
        f"{design['base_depth_mm']} mm"
    )

    print(
        f"Thickness: "
        f"{design['selected_thickness_mm']} mm"
    )


    # ==========================================================
    # STEP 3 — CONNECT TO CATIA
    # ==========================================================

    print("\n🛠️ Connecting to CATIA V5...")

    catia = connect_to_catia()


    # ==========================================================
    # STEP 4 — GENERATE CAD MODEL
    # ==========================================================

    print("\n🏗️ Generating 3D model...")

    create_l_bracket(

        catia,

        width=design["width_mm"],

        height=design["height_mm"],

        depth=design["base_depth_mm"],

        thickness=design["selected_thickness_mm"]
    )


    # ==========================================================
    # COMPLETE
    # ==========================================================

    print("\n" + "=" * 65)
    print("🔥 DESIGN COMPLETE")
    print("=" * 65)

    print("\nYour engineering requirement has been")
    print("converted into a CATIA 3D model.")

    print("\nPipeline:")
    print("Natural Language")
    print("      ↓")
    print("Llama AI")
    print("      ↓")
    print("Engineering Calculation")
    print("      ↓")
    print("CATIA V5")
    print("      ↓")
    print("3D L-Bracket")


if __name__ == "__main__":
    main()
