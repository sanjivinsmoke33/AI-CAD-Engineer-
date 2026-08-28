import win32com.client


def connect_to_catia():

    print("Connecting to CATIA V5...")

    catia = win32com.client.GetActiveObject(
        "CATIA.Application"
    )

    print("✅ Connected to CATIA V5")

    return catia


def create_l_bracket(
    catia,
    width,
    height,
    depth,
    thickness
):

    print("\nCreating L-bracket...")
    print(f"Width: {width} mm")
    print(f"Height: {height} mm")
    print(f"Depth: {depth} mm")
    print(f"Thickness: {thickness} mm")

    # --------------------------------------------------
    # CREATE PART
    # --------------------------------------------------

    document = catia.Documents.Add("Part")

    part = document.Part

    # --------------------------------------------------
    # CREATE BODY
    # --------------------------------------------------

    body = part.Bodies.Add()

    body.Name = "LBracketBody"

    # --------------------------------------------------
    # GET YZ PLANE
    # --------------------------------------------------

    origin = part.OriginElements

    yz_plane = origin.PlaneYZ

    # --------------------------------------------------
    # CREATE SKETCH
    # --------------------------------------------------

    sketches = body.Sketches

    sketch = sketches.Add(yz_plane)

    sketch.Name = "LBracketProfile"

    # --------------------------------------------------
    # DRAW L PROFILE
    # --------------------------------------------------

    factory = sketch.OpenEdition()

    # Outer vertical
    factory.CreateLine(
        0, 0,
        0, height
    )

    # Top
    factory.CreateLine(
        0, height,
        thickness, height
    )

    # Inner vertical
    factory.CreateLine(
        thickness, height,
        thickness, thickness
    )

    # Inner horizontal
    factory.CreateLine(
        thickness, thickness,
        depth, thickness
    )

    # Outer bottom
    factory.CreateLine(
        depth, thickness,
        depth, 0
    )

    # Close profile
    factory.CreateLine(
        depth, 0,
        0, 0
    )

    sketch.CloseEdition()

    part.Update()

    # --------------------------------------------------
    # PAD
    # --------------------------------------------------

    shape_factory = part.ShapeFactory

    pad = shape_factory.AddNewPad(
        sketch,
        width
    )

    pad.Name = "LBracketWidth"

    part.Update()

    print("\n🔥 L-BRACKET CREATED IN CATIA!")

    return document


if __name__ == "__main__":

    catia = connect_to_catia()

    create_l_bracket(
        catia,
        width=100,
        height=60,
        depth=40,
        thickness=3
    )
