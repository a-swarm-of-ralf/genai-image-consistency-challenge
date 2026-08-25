import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    # One Nice Image Is Easy

    {mo.image("notebooks/images/ai-slop.jpeg")}

    ## Introduction

    The **XYZ project** is exploring the possibility of adding **AI image generation** to its portfolio. Modern image-generation models can create impressive visuals, but using them consistently and reliably comes with challenges.

    Common issues include:

    - **AI artifacts** — subtle errors such as extra fingers, strange teeth, malformed objects, or incorrect details.
    - **Perspective and geometry** — inconsistent perspective, vanishing points, proportions, and spatial relationships.
    - **Style consistency** — maintaining the same visual style across multiple images.
    - **Subject consistency** — keeping characters, objects, clothing, and backgrounds recognizable from one image to the next.

    Rather than just talking about these limitations, we're going to put them to the test.

    ## The Challenge

    Your challenge is to create a **short visual story told in 5–8 images** using GenAI image-generation tools.

    Across the entire story, try to maintain:

    - A **consistent visual style**
    - The **same recurring characters**
    - Consistent **objects, clothing, and environments**
    - A clear **visual narrative** from one image to the next

    **_One nice image is easy. Now make 5–8 that belong together._**


    ## Setup

    For this workshop, you will need access to an **AI image-generation tool that supports reference images**. Reference images will become important as we experiment with maintaining consistent characters, objects, and visual styles across multiple images.

    The **XYZ project is currently considering Nano Banana 2** as one of the leading models for image generation, but the challenges in this workshop are deliberately **model-independent**. Feel free to experiment with any image model you have access to.

    ### Suggested Tools

    | Tool / Model | Why use it? |
    |---|---|
    | **Microsoft 365 Copilot Create** | Recommended for this workshop. Easy to use, available to participants, and supports using uploaded images as references. |
    | **Nano Banana 2** | Google's current general-purpose image model. Strong image generation and editing with a good balance between quality, speed, and cost. |
    | **Nano Banana Pro** | Google's higher-end model aimed at professional asset production, complex instructions, and high-resolution output. |
    | **ChatGPT Images** | Strong general-purpose generation and conversational image editing, including workflows using multiple uploaded images. |
    | **Open image models** | Models such as FLUX and similar open-weight ecosystems offer more control and opportunities for custom or self-hosted workflows, but generally require more setup. |

    Don't worry about choosing the *best* model. Comparing what different tools can and cannot do is part of the experiment.

    ### Recommended: Microsoft 365 Copilot Create

    For the exercises, we recommend using **Microsoft 365 Copilot Create**, since it is already available to workshop participants.

    Copilot Create lets you generate images from a text description and add an existing image as a visual reference. Depending on your organization's configuration, it can also provide styles, aspect ratios, editing tools, and brand kits.

    [Open Microsoft guidance for Copilot Create](https://support.microsoft.com/en-us/microsoft-365-copilot/create-ai-generated-images-with-the-microsoft-365-copilot-app?utm_source=chatgpt.com)

    ### How We'll Work

    Because we're using a web-based tool rather than an image-generation API, **the main artifact you'll create is the prompt**.

    For each exercise:

    1. Write and refine your prompt.
    2. Copy it into Copilot Create.
    3. Add reference images when the exercise calls for them.
    4. Generate and inspect the result.
    5. Save useful prompts and generated images.
    6. Iterate when the result doesn't meet your requirements.

    Keep your prompts in this repository as you work through the challenges.

    This is intentionally different from building a scripted image-generation pipeline. We're interested in the **creative and production workflow**: how much information, iteration, reference material, and manual review does it take to get from an idea to a consistent set of images?

    > **Tip:** Don't throw away prompts that fail. Keep them. Understanding *why* a seemingly good prompt produced an unexpected result is part of the workshop.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    # Challenge 1 — Tell a Story

    Your first challenge is to come up with a **simple story that can be told in 5–8 scenes**.

    Anything can work here. You could take inspiration from:

    - A favourite movie, book, or TV show
    - A classic children's story
    - An epic fantasy adventure
    - A day at the office
    - A trip through the city
    - A small mystery
    - Or something completely original

    **Keep it simple.** The challenge isn't writing an elaborate story; it's creating a sequence of images that clearly belong together.

    A good story for this exercise has:

    - **One or two protagonists** who appear in multiple scenes
    - **A recognizable location** or recurring environment
    - **One or two recurring objects** that need to remain recognizable
    - A clear **beginning, middle, and end**

    ## Example — The Lost Key

    Mila is on her way to visit her grandmother, who lives in an old house on the other side of the city. Her grandmother has given her an old brass key to let herself in.

    1. **Leaving Home** — Mila leaves her apartment wearing her yellow raincoat, carrying a red umbrella and the old brass key.
    2. **The Tram Stop** — She waits at a tram stop in the pouring rain, holding the red umbrella.
    3. **Something Is Missing** — Sitting on the tram, Mila reaches into her pocket and realizes the brass key is gone.
    4. **The Search** — Mila searches underneath the tram seats while other passengers look on.
    5. **Found!** — A young boy discovers the brass key underneath a seat and returns it to Mila.
    6. **The Green Door** — Mila arrives at her grandmother's old house, closes her red umbrella, and uses the brass key to unlock the large green front door.

    This gives us several things that need to remain consistent across the images: **Mila, her yellow raincoat, the red umbrella, the brass key, the tram, and the overall visual style.**

    ## Your Turn

    Write your story as **5–8 short scene descriptions**.

    Don't worry about detailed image prompts yet. At this stage, concentrate on **what happens in each scene** and which characters, objects, and locations will need to remain recognizable throughout your story.

    > **Tip:** Don't make things too easy for the image model. Recurring characters, distinctive clothing, recognizable objects, and repeated locations are exactly what we want to put to the test.
    """)
    return


@app.cell
def _():
    scene_01 = """
    Mila leaves her apartment to visit her grandmother.
    She is wearing a yellow raincoat and carries a red umbrella and an old brass key.
    """

    scene_02 = """
    Mila waits at a tram stop in the pouring rain.
    She is holding her red umbrella while waiting for the tram.
    """

    scene_03 = """
    Mila is sitting inside the tram when she realizes that the old brass key is missing.
    She searches the pockets of her yellow raincoat.
    """

    scene_04 = """
    Mila searches underneath the seats of the tram for the missing key.
    Other passengers watch as she looks around.
    """

    scene_05 = """
    A young boy finds the old brass key underneath one of the tram seats.
    He gives the key back to a relieved Mila.
    """

    scene_06 = """
    Mila arrives at her grandmother's old house.
    She closes her red umbrella and uses the brass key to unlock the large green front door.
    """
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 1.1 — Create the Prompts and Images

    Now turn each of your **5–8 scenes into an image-generation prompt** and generate the first version of your story.

    This is our **baseline**. Later in the workshop, we'll introduce techniques to improve consistency and compare the results with these first images.

    For now, work with **text prompts only**. Don't use reference images yet.

    ### Create a Prompt for Each Scene

    Write one prompt for every scene. Each prompt should contain enough information for the image model to understand both the individual scene and the visual language of the overall story.

    A useful structure is:

    1. **Task description** — What are you asking the model to create?
    2. **Scene description** — What is happening in this particular image?
    3. **Character descriptions** — What do recurring characters look like?
    4. **Object descriptions** — Describe important recurring objects when they appear.
    5. **Environment** — Where does the scene take place?
    6. **Composition** — Shot type, viewpoint, framing, positioning, etc.
    7. **Style description** — Define the visual style of the story.
    8. **Constraints** — Anything that should explicitly be included or avoided.

    ### Reuse Your Descriptions

    Consistency starts with the instructions you provide.

    Create a description for each recurring character and reuse **the same description verbatim** whenever that character appears.

    Do the same for:

    - Visual style
    - Important objects
    - Recurring locations

    For example:

    ```python
    style = "\""
    Warm modern children's-book illustration with soft rounded shapes,
    subtle watercolor textures, a muted orange-and-blue color palette,
    natural lighting, and a friendly, optimistic atmosphere.
    "\""

    mila = "\""
    Mila is an eight-year-old girl with curly dark-brown shoulder-length hair,
    brown eyes, freckles, and a round face. She wears a bright yellow raincoat,
    dark-blue trousers, red rain boots, and a small blue backpack.
    "\""

    brass_key = "\""
    An old-fashioned brass key with a round bow and three distinctive teeth.
    "\""
    ```

    You can then use these descriptions when constructing each prompt:

    ```python
    prompt_01 = f"\""
    Create an illustration for the first scene of a children's story.

    SCENE:
    Mila leaves her apartment on a rainy morning to visit her grandmother.
    She stands outside the apartment entrance holding a red umbrella.
    The old brass key is visible in her other hand.

    CHARACTER:
    {mila}

    IMPORTANT OBJECT:
    {brass_key}

    STYLE:
    {style}

    COMPOSITION:
    Medium-wide shot showing Mila and the entrance to the apartment building.
    Mila is the clear focal point of the image.
    "\""
    ```

    Repeat this for every scene in your story.

    ### Generate Your Baseline Images

    Generate **one image for each scene** using your prompts.

    Try not to endlessly regenerate until you get the perfect result. We want a realistic baseline of what the model produces from reasonably well-written prompts.

    Save:

    - Your prompts
    - Your 5–8 generated images
    - Any particularly interesting failures

    We'll return to them later.

    ### Tips

    - **Be specific, not verbose.** More words don't automatically produce a better image.
    - **Reuse exact descriptions.** Don't describe a character as *“curly dark hair”* in one prompt and *“wavy brown hair”* in another.
    - **Describe visible properties.** The model can't show that Mila is *kind and adventurous* as reliably as it can show *a yellow raincoat and blue backpack*.
    - **Give distinctive objects distinctive features.** “A key” leaves much more freedom than “an old brass key with a round bow and three distinctive teeth.”
    - **Describe composition explicitly** when it matters: close-up, wide shot, viewed from above, character on the left, empty space on the right, etc.
    - **Don't rely on names for continuity.** Writing “Mila” in every prompt doesn't tell the model that this Mila must look identical to the Mila it generated previously.
    - **Check instruction adherence.** Before judging whether an image looks good, check whether it actually contains what you asked for.
    - **Keep the first results.** Imperfections are useful data for the next challenges.

    > **Remember:** we're not trying to solve consistency yet. We're establishing how far we can get with careful text prompting alone.
    """)
    return


@app.cell
def _():
    style = """
    Warm modern children's-book illustration with soft rounded shapes,
    subtle watercolor textures, a muted orange-and-blue color palette,
    natural lighting, and a friendly, optimistic atmosphere.
    """

    mila = """
    Mila is an eight-year-old girl with curly dark-brown shoulder-length hair,
    brown eyes, freckles, and a round face. She wears a bright yellow raincoat,
    dark-blue trousers, red rain boots, and a small blue backpack.
    """

    boy = """
    A seven-year-old boy with short blond hair, blue eyes, and a friendly round face.
    He wears a green jacket, brown trousers, and white sneakers.
    """

    brass_key = """
    An old-fashioned brass key with a round bow and three distinctive teeth.
    """

    red_umbrella = """
    A bright red umbrella with a curved wooden handle.
    """

    ex1_prompt_01 = f"""
    Create an illustration for the first scene of a children's story.

    SCENE:
    Mila leaves her apartment on a rainy morning to visit her grandmother.
    She stands outside the apartment entrance holding a red umbrella.
    The old brass key is clearly visible in her other hand.

    CHARACTER:
    {mila}

    IMPORTANT OBJECTS:
    {red_umbrella}
    {brass_key}

    STYLE:
    {style}

    COMPOSITION:
    Medium-wide shot showing Mila and the entrance to the apartment building.
    Mila is the clear focal point of the image.
    """


    ex1_prompt_02 = f"""
    Create an illustration for the second scene of a children's story.

    SCENE:
    Mila waits at a tram stop in the pouring rain.
    She stands underneath her red umbrella as a tram approaches in the background.
    The wet street reflects the lights of the city.

    CHARACTER:
    {mila}

    IMPORTANT OBJECT:
    {red_umbrella}

    STYLE:
    {style}

    COMPOSITION:
    Wide street-level shot showing Mila at the tram stop and the approaching tram.
    Mila is in the foreground, with enough of the environment visible to establish
    the rainy city setting.
    """


    ex1_prompt_03 = f"""
    Create an illustration for the third scene of a children's story.

    SCENE:
    Mila is sitting inside the tram when she realizes that the old brass key is missing.
    She looks worried while searching the pockets of her yellow raincoat.
    Her closed red umbrella rests beside her.

    CHARACTER:
    {mila}

    IMPORTANT OBJECT:
    {red_umbrella}

    STYLE:
    {style}

    COMPOSITION:
    Medium shot inside the tram.
    Mila is seated next to a window and is the clear focal point.
    Show enough of the tram interior to establish the location.
    """


    ex1_prompt_04 = f"""
    Create an illustration for the fourth scene of a children's story.

    SCENE:
    Mila searches underneath the seats of the tram for her missing brass key.
    She kneels in the aisle and looks beneath one of the seats.
    Several passengers watch curiously from their seats.
    Her closed red umbrella is nearby.

    CHARACTER:
    {mila}

    IMPORTANT OBJECT:
    {red_umbrella}

    STYLE:
    {style}

    COMPOSITION:
    Wide interior shot looking along the aisle of the tram.
    Mila is kneeling near the center of the image while searching underneath a seat.
    The rows of seats and several passengers are visible around her.
    """


    ex1_prompt_05 = f"""
    Create an illustration for the fifth scene of a children's story.

    SCENE:
    A young boy has discovered Mila's missing brass key underneath a tram seat.
    He holds the key out toward Mila.
    Mila looks relieved and reaches out to accept it.

    CHARACTERS:
    {mila}

    {boy}

    IMPORTANT OBJECT:
    {brass_key}

    STYLE:
    {style}

    COMPOSITION:
    Medium shot inside the tram showing both children.
    The boy holds the brass key clearly between them.
    Their expressions and the returned key are the main focus of the image.
    """


    ex1_prompt_06 = f"""
    Create an illustration for the final scene of a children's story.

    SCENE:
    Mila has arrived at her grandmother's old house after the rain.
    She stands in front of a large green wooden front door and uses the old brass key
    to unlock it.
    Her closed red umbrella is in her other hand.

    CHARACTER:
    {mila}

    IMPORTANT OBJECTS:
    {brass_key}
    {red_umbrella}

    STYLE:
    {style}

    COMPOSITION:
    Medium-wide shot showing Mila standing in front of the large green door.
    The brass key should be clearly visible in the lock.
    The old house entrance frames Mila and creates a warm ending to the story.
    """
    return


@app.cell(hide_code=True)
def _(mo):
    scene_01_image = mo.image("notebooks/images/ex1_scene01.png")
    scene_02_image = mo.image("notebooks/images/ex1_scene02.png")
    scene_03_image = mo.image("notebooks/images/ex1_scene03.png")
    scene_04_image = mo.image("notebooks/images/ex1_scene04.png")
    scene_05_image = mo.image("notebooks/images/ex1_scene05.png")
    scene_06_image = mo.image("notebooks/images/ex1_scene06.png")

    mo.md(
        f"""
    ### The Lost Key

    #### 1. Leaving Home

    {scene_01_image}

    Mila leaves her apartment on a rainy morning to visit her grandmother.
    She is wearing her yellow raincoat and carries a red umbrella and an old
    brass key.

    ---

    #### 2. The Tram Stop

    {scene_02_image}

    Mila waits at a tram stop in the pouring rain. She stands underneath her
    red umbrella as the tram approaches through the rainy city streets.

    ---

    #### 3. Something Is Missing

    {scene_03_image}

    Sitting inside the tram, Mila suddenly realizes that something is wrong.
    She searches the pockets of her yellow raincoat.

    **The old brass key is gone!**

    ---

    #### 4. The Search

    {scene_04_image}

    Mila searches underneath the seats of the tram for the missing key.
    She kneels in the aisle and looks beneath the seats while the other
    passengers watch curiously.

    But where could the key be?

    ---

    #### 5. Found!

    {scene_05_image}

    A young boy spots something underneath one of the tram seats.

    It's Mila's old brass key!

    He picks it up and returns it to a very relieved Mila.

    ---

    #### 6. The Green Door

    {scene_06_image}

    After the rain, Mila finally arrives at her grandmother's old house.

    She stands in front of the large green wooden door, puts the old brass
    key into the lock, and turns it.

    **She made it!**

    ---

    ### Now look at all six images again...

    Do they really look like illustrations from the **same story**?

    Pay attention to Mila, her clothing, the umbrella, the key, the tram,
    the environments, and the overall illustration style.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md("""
    ### 2.1 Discussion

    Above is the example story about **Mila and the Lost Key**.

    Compare it with the story your group generated:

    - How consistent are the characters, objects, and visual style?
    - Which details changed between scenes?
    - Did you notice problems only after seeing all images together?
    - How do your results compare with the Mila example?
    - Did different image models produce noticeably different results?
    - Which model seemed better at consistency, instruction following, or visual quality?
    """),kind="info",)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Challenge 2 — Production Mode

    We have a story.

    In Challenge 1, we took the straightforward approach: describe each scene as carefully as possible and ask the image model to generate it.

    That gave us our **baseline**.

    Now let's see what happens when we approach the same task more like a visual production workflow.

    Instead of relying on text prompts alone, we're going to create a set of **reference images** that define what our story is supposed to look like.

    ## What Are Reference Images?

    A reference image is an existing image provided to the model together with your prompt.

    Instead of only telling the model:

    > Mila is an eight-year-old girl with curly dark-brown hair, freckles, and a yellow raincoat.

    we can also **show it what Mila looks like**.

    References can help establish things such as:

    - **Style** — how the images should be illustrated
    - **Characters** — what recurring people should look like
    - **Objects** — the appearance of important props or products
    - **Locations** — what recurring environments should look like
    - **Composition** — the framing or layout we're trying to achieve

    Different models support references in different ways, and providing a reference does **not** guarantee that every detail will be reproduced exactly.

    For example, Google's Gemini 3 image models accept up to **14 reference images**, but allocate them differently:

    | Model | Object references | Character references | Style references |
    |---|---:|---:|---:|
    | **Nano Banana 2** | Up to 10 | Up to 4 | — |
    | **Nano Banana Pro** | Up to 6 | Up to 5 | Up to 3 |

    Nano Banana Pro therefore provides explicit support for dedicated **style references**, while Nano Banana 2 focuses its reference capacity on objects and characters. citeturn0search1

    Other tools may handle references differently. Part of the challenge is discovering what your chosen tool can reliably preserve.

    ---

    # Exercise 2.1 — Create a Style Bible

    Before generating new scenes, define the **visual rules of your story**.

    In Challenge 1 we already included a style description in every prompt. Now we're going to make that description more deliberate and turn it into a visual reference.

    ## Define Your Style

    Create a short **style bible** describing the visual language that should apply to every image.

    Consider:

    ### Illustration Technique

    How should the image be rendered?

    For example:

    - Watercolor illustration
    - Digital painting
    - Flat vector illustration
    - Pencil and ink
    - 3D render
    - Photorealistic photography

    ### Shapes and Linework

    Think about the visual forms:

    - Soft or angular shapes?
    - Strong outlines or no visible outlines?
    - Precise or hand-drawn lines?
    - Simple or intricate forms?

    ### Color Palette

    Define how color should be used:

    - Bright or muted?
    - Warm or cool?
    - Limited palette or many colors?
    - High or low contrast?
    - Particular dominant colors?

    ### Lighting

    Describe the lighting:

    - Soft natural light
    - Dramatic cinematic lighting
    - Overcast daylight
    - Warm evening light
    - Flat graphic lighting

    ### Mood

    What should the images feel like?

    For example:

    - Friendly
    - Optimistic
    - Serious
    - Mysterious
    - Playful
    - Corporate
    - Dramatic

    ### Level of Detail

    How visually complex should the images be?

    - Minimal and graphic
    - Moderately detailed
    - Richly illustrated
    - Highly realistic

    ### Composition

    Define some general composition rules:

    - Simple compositions with one clear focal point
    - Lots of negative space
    - Busy environmental scenes
    - Centered subjects
    - Asymmetrical editorial compositions

    ### Camera Language

    Think about how the story should be visually photographed or framed:

    - Mostly eye-level
    - Cinematic wide shots
    - Intimate close-ups
    - Documentary photography
    - Children's-book compositions
    - Dramatic low-angle shots

    ---

    ## Create a Style Reference

    Now turn your style bible into a prompt and generate **one or more images that represent the visual style** you want for the complete story.

    The content of the image isn't particularly important.

    What matters is that it demonstrates the visual characteristics you want to reproduce.

    For example:

    > Create a style reference for a modern children's-book illustration.
    >
    > Show a quiet European residential street on a rainy morning with a small tram in the distance.
    >
    > Use soft rounded shapes and subtle watercolor textures. Use a muted palette dominated by warm oranges, deep blues, soft greens, and neutral stone colors. Use clean but slightly organic forms without strong comic-book outlines.
    >
    > Lighting should be soft, natural, and slightly overcast, while the overall atmosphere remains warm, friendly, and optimistic.
    >
    > Use a moderate level of detail: environments should feel lived-in and recognizable without becoming photorealistic or visually busy.
    >
    > Use an eye-level, medium-wide composition with a clear focal point and enough environmental detail to establish the location.
    >
    > This image will be used as a **visual style reference for a series of illustrations**, so prioritize a clear and distinctive visual language over storytelling or character design.

    Generate a few alternatives if necessary and choose the image that best represents your intended style.

    ## Deliverables

    At the end of this exercise, keep:

    - Your **written style bible**
    - Your **style-reference prompt**
    - Your chosen **style reference image(s)**

    We'll use these references when we return to our story.

    > **Don't try to fix the characters yet.** At this stage we're isolating one problem: can we establish a visual language and reproduce it across multiple images?
    """)
    return


@app.cell
def _():
    ex2_style_prompt = """
    Create a visual style reference for a modern children's-book illustration series.

    SCENE:
    Show a quiet European city street on a rainy morning. Include colorful old
    buildings, wet pavement, a tram line, a few trees, and warm lights visible
    through some windows. Do not include any prominent characters; the purpose
    of this image is to establish the visual style rather than the story.

    ILLUSTRATION TECHNIQUE:
    Modern children's-book illustration with subtle watercolor textures and
    soft digital painting. The artwork should feel hand-crafted rather than
    photorealistic.

    SHAPES AND LINEWORK:
    Use soft, rounded, simplified shapes with clean but slightly organic edges.
    Avoid heavy comic-book outlines and highly precise geometric forms.

    COLOR PALETTE:
    Use a muted but warm palette dominated by orange, blue, soft green, and
    neutral stone colors. Colors should feel harmonious and slightly desaturated.

    LIGHTING:
    Soft natural light from an overcast rainy morning. Use gentle reflections
    on the wet pavement and subtle warm light from windows.

    MOOD:
    Friendly, warm, optimistic, and slightly whimsical despite the rainy weather.
    The atmosphere should feel safe and inviting.

    LEVEL OF DETAIL:
    Moderately detailed. Buildings and street furniture should be recognizable,
    but simplified enough to remain suitable for a children's-book illustration.
    Avoid photorealistic textures and excessive background detail.

    COMPOSITION:
    Eye-level, medium-wide composition with a clear focal point and enough
    environment visible to establish the setting. Use balanced areas of visual
    detail and negative space.

    CAMERA LANGUAGE:
    Natural eye-level perspective similar to a carefully composed storybook
    illustration. Avoid dramatic wide-angle distortion, extreme perspective,
    or cinematic depth of field.

    IMPORTANT:
    This image will be used as the STYLE REFERENCE for all illustrations in
    the same story. Prioritize a clear, distinctive, and reproducible visual
    language over characters or storytelling.
    """
    return


@app.cell(hide_code=True)
def _(mo):
    style_reference = mo.image("notebooks/images/ex2_style_reference.png")

    mo.md(
        f"""
    ### Example — Mila Style Reference

    For the **Mila and the Lost Key** story, we turned our style bible into a
    dedicated style reference image.

    {style_reference}

    This image is not part of the story itself. Its purpose is to establish the
    **visual language** we want the other images to follow: illustration technique,
    shapes, linework, colors, lighting, mood, level of detail, composition, and
    camera language.

    We'll use this image as a reference when generating the story again.

    > **Your turn:** Create and save a style reference for your own story.
    > Don't worry about characters or recurring objects yet — focus on making
    > the **style** as clear and recognizable as possible.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    ## Exercise 2.2 — Create Character References

    We have defined **how our story should look**. Now we need to define **who appears in it**.

    Just as a written style description leaves room for interpretation, a written character description does too. Even if we repeat exactly the same description in every prompt, the model can interpret details such as facial features, hair, proportions, and clothing differently each time.

    To reduce that ambiguity, we'll create **character reference images**.

    ### Character Sheets

    You've probably seen character sheets as concept art in animation, games, or special-edition art books. They show the same character from different angles, in different poses, and with different expressions.

    A useful character reference might establish:

    - **Age**
    - **Face** — face shape, eyes, nose, freckles, etc.
    - **Hair** — color, length, texture, and hairstyle
    - **Body type and proportions**
    - **Clothing**
    - **Shoes**
    - **Accessories**
    - **Distinctive features**

    Depending on your image model, your character sheet could contain:

    - A neutral full-body pose
    - Front view
    - Three-quarter view
    - Side view
    - Different poses
    - Different facial expressions

    The objective is **not to create the prettiest character sheet**.

    The objective is to remove ambiguity:

    > **What does this character actually look like?**

    ### Should You Use the Style Reference?

    If your tool supports it, **include the style reference from Exercise 2.1 when creating your character reference**.

    We're gradually building a visual specification for our story:

    **Style Bible → Style Reference → Character Reference → Final Scenes**

    The character reference should therefore define the character **within the visual style we've already established**, rather than introducing a new interpretation of that style.

    ---

    ### Example — Mila

    For our example, we'll use `ex2_style_reference.png` from the previous exercise as a style reference and create a character sheet for Mila.

    ```python
    ex2_character_prompt = "\"\"
    Create a CHARACTER REFERENCE SHEET for Mila, using the provided
    'ex2_style_reference.png' image as the visual STYLE REFERENCE.

    The character sheet must follow the same illustration technique, shapes,
    linework, color treatment, lighting, and level of detail as the provided
    style reference.

    CHARACTER:
    Mila is an eight-year-old girl with a friendly round face, brown eyes,
    freckles across her cheeks and nose, and curly dark-brown shoulder-length
    hair.

    She has the natural proportions and build of an eight-year-old child.

    CLOTHING:
    Mila wears a bright yellow raincoat, dark-blue trousers, red rain boots,
    and a small blue backpack.

    Her clothing and accessories must remain exactly the same in every depiction.

    CHARACTER SHEET:
    Show multiple clearly separated depictions of the SAME character on one
    character-reference sheet.

    Include:

    1. Full-body neutral pose, viewed from the front.
    2. Full-body three-quarter view.
    3. Full-body side view.
    4. Walking pose.
    5. Happy facial expression.
    6. Worried facial expression.
    7. Surprised facial expression.

    CONSISTENCY:
    Every depiction must clearly represent the SAME Mila.

    Keep her facial features, freckles, hairstyle, hair length, body proportions,
    clothing colors, raincoat design, boots, and backpack consistent across all
    views and expressions.

    STYLE:
    Warm modern children's-book illustration with soft rounded shapes,
    subtle watercolor textures, a muted orange-and-blue color palette,
    natural lighting, and a friendly, optimistic atmosphere.

    Use the provided style reference as the primary guide for the visual
    appearance of the illustration.

    LAYOUT:
    Present the different views and expressions as a clean professional
    character-design reference sheet on a simple neutral background.

    Do not create a story scene or environment.
    Do not add additional characters.
    Do not add text labels unless necessary.

    IMPORTANT:
    This image will be used as a CHARACTER REFERENCE for generating Mila
    consistently across multiple illustrations.

    Prioritize a clear, reproducible character design and consistency between
    the different views over making the sheet decorative or cinematic.
    "\"\"
    ```

    ### Create Your Character References

    Now create a character reference for each important recurring character in your story.

    For minor background characters, this usually isn't necessary. Concentrate your effort on characters whose identity needs to survive across multiple scenes.

    Save both:

    - The **character-reference prompt**
    - The resulting **character-reference image**

    We'll use them as inputs when we generate the story again.

    > **Tip:** Inspect the character sheet itself for consistency. The model may already change small details **within the reference sheet**. A reference image containing contradictory versions of your character gives the model contradictory instructions later.
    """)
    return


@app.cell
def _():
    ex2_character_prompt_mila = """
    Create a CHARACTER REFERENCE SHEET for Mila, using the provided
    'ex2_style_reference.png' image as the visual STYLE REFERENCE.

    The character sheet must follow the same illustration technique, shapes,
    linework, color treatment, lighting, and level of detail as the provided
    style reference.

    CHARACTER:
    Mila is an eight-year-old girl with a friendly round face, brown eyes,
    freckles across her cheeks and nose, and curly dark-brown shoulder-length
    hair.

    She has the natural proportions and build of an eight-year-old child.

    CLOTHING:
    Mila wears a bright yellow raincoat, dark-blue trousers, red rain boots,
    and a small blue backpack.

    Her clothing and accessories must remain exactly the same in every depiction.

    CHARACTER SHEET:
    Show multiple clearly separated depictions of the SAME character on one
    character-reference sheet.

    Include:

    1. Full-body neutral pose, viewed from the front.
    2. Full-body three-quarter view.
    3. Full-body side view.
    4. Walking pose.
    5. Happy facial expression.
    6. Worried facial expression.
    7. Surprised facial expression.

    CONSISTENCY:
    Every depiction must clearly represent the SAME Mila.

    Keep her facial features, freckles, hairstyle, hair length, body proportions,
    clothing colors, raincoat design, boots, and backpack consistent across all
    views and expressions.

    STYLE:
    Warm modern children's-book illustration with soft rounded shapes,
    subtle watercolor textures, a muted orange-and-blue color palette,
    natural lighting, and a friendly, optimistic atmosphere.

    Use the provided style reference as the primary guide for the visual
    appearance of the illustration.

    LAYOUT:
    Present the different views and expressions as a clean professional
    character-design reference sheet on a simple neutral background.

    Do not create a story scene or environment.
    Do not add additional characters.
    Do not add text labels unless necessary.

    IMPORTANT:
    This image will be used as a CHARACTER REFERENCE for generating Mila
    consistently across multiple illustrations.

    Prioritize a clear, reproducible character design and consistency between
    the different views over making the sheet decorative or cinematic.
    """

    ex2_boy_character_prompt = """
    Create a CHARACTER REFERENCE SHEET for the boy from the Mila story, using the
    provided 'ex2_style_reference.png' image as the visual STYLE REFERENCE.

    The character sheet must follow the same illustration technique, shapes,
    linework, color treatment, lighting, and level of detail as the provided
    style reference.

    CHARACTER:
    The boy is seven years old. He has short blond hair, blue eyes, and a friendly
    round face.

    He has the natural proportions and build of a seven-year-old child.

    CLOTHING:
    The boy wears a soft green jacket, brown trousers, and simple white sneakers.

    His clothing must remain exactly the same in every depiction.

    CHARACTER SHEET:
    Show multiple clearly separated depictions of the SAME character on one
    character-reference sheet.

    Include:

    1. Full-body neutral pose, viewed from the front.
    2. Full-body three-quarter view.
    3. Full-body side view.
    4. Kneeling down and reaching underneath something.
    5. Friendly, happy facial expression.
    6. Curious facial expression.
    7. Surprised facial expression.

    CONSISTENCY:
    Every depiction must clearly represent the SAME boy.

    Keep his facial features, hairstyle, hair color, body proportions, jacket,
    trousers, shoes, and clothing colors consistent across all views, poses,
    and expressions.

    STYLE:
    Warm modern children's-book illustration with soft rounded shapes,
    subtle watercolor textures, a muted orange-and-blue color palette,
    natural lighting, and a friendly, optimistic atmosphere.

    Use the provided style reference as the primary guide for the visual
    appearance of the illustration.

    LAYOUT:
    Present the different views, poses, and expressions as a clean professional
    character-design reference sheet on a simple neutral background.

    Do not create a story scene or environment.
    Do not add Mila or any other characters.
    Do not add text labels unless necessary.

    IMPORTANT:
    This image will be used as a CHARACTER REFERENCE for generating the boy
    consistently in later illustrations.

    Prioritize a clear, reproducible character design and consistency between
    the different views over making the sheet decorative or cinematic.
    """
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    ### Example — Character References

    For the **Mila and the Lost Key** story, we created reference sheets for both recurring characters.

    The goal is not just to create attractive character designs, but to establish a **visual source of truth** that we can reuse when generating the individual story scenes.

    #### Mila

    {mo.image("notebooks/images/ex2_character_reference_mila.png")}

    Mila's reference establishes her face, hair, proportions, clothing, colors, and accessories across several poses and expressions.

    #### The Boy

    {mo.image("notebooks/images/ex2_character_reference_boy.png")}

    The boy only appears briefly, but having a reference gives us explicit control over his appearance when we generate the scene in which he returns the key.

    > **Next:** We'll provide these character sheets as reference images when regenerating our scenes and see how much they improve character consistency.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    ## Exercise 2.3 — Object & Environment References

    We have defined our **style** and our **characters**. But characters aren't the only things that can unexpectedly change between images.

    Recurring **objects, vehicles, and locations** also need continuity.

    A bicycle may change frame shape. A phone may gain another camera. A product package may change proportions. A room may suddenly have different windows. A vehicle shown from the outside may bear little resemblance to its interior in the next image.

    So let's define the rest of our visual world.

    ### What Needs a Reference?

    Look through your scenes and identify objects or environments that:

    - Appear in multiple images
    - Are important to the story
    - Need to be immediately recognizable
    - Have distinctive visual characteristics
    - Establish continuity between scenes

    Possible examples include:

    - A bicycle
    - A backpack
    - A product or package
    - A vehicle
    - A phone
    - A piece of jewelry
    - A distinctive building
    - An important room
    - A mysterious brass key

    You don't need a reference for **everything**.

    Concentrate on elements where changing their appearance would make the story feel inconsistent.

    ### Define What It Actually Looks Like

    As with our characters, start by removing ambiguity.

    Instead of:

    > An old brass key

    define the important visual characteristics:

    > An old-fashioned brass key made from aged brass, approximately 8 cm long, with a large circular bow, a narrow cylindrical shaft, and three distinctive rectangular teeth.

    Then create a reference image showing the object clearly.

    For complex objects, vehicles, or locations, consider showing **multiple useful views in the same reference image**.

    For example:

    - Front, side, and three-quarter view of a vehicle
    - Exterior and entrance of a building
    - Several angles of an important object
    - Wide view and important details of a room

    As before, include your **style reference** when your tool supports it so that these references already belong to the same visual world.

    ---

    ## Example — The Mila Story

    For **Mila and the Lost Key**, there are several elements worth defining before we regenerate the story.

    ### 🔑 The Brass Key

    The key is central to the story and appears in several scenes.

    Create a reference that clearly establishes:

    - Material and color
    - Overall shape
    - Size
    - Shape of the bow
    - Shape of the shaft
    - Number and shape of the teeth
    - Signs of age or wear

    The goal is that the key Mila holds in scene 1 is recognizably the **same key** returned to her in scene 5 and used in the door in scene 6.

    {mo.image("notebooks/images/ex2_key_reference.png")}

    ### 🚋 The Tram — Exterior

    The tram appears first from the outside and later becomes an important location.

    Define:

    - Overall shape
    - Colors
    - Windows
    - Doors
    - Headlights
    - Number of sections
    - Other distinctive visual details

    A side or three-quarter view can make a useful vehicle reference.

    {mo.image("notebooks/images/ex2_tram_exterior_reference.png")}

    ### 💺 The Tram — Interior

    The interior appears across several consecutive scenes, so it is especially important for visual continuity.

    Define:

    - Seat design and color
    - Floor
    - Windows
    - Doors
    - Handrails
    - Lighting
    - Width and layout of the aisle

    Think about the relationship between the exterior and interior references. They should plausibly depict **the same tram**.

    {mo.image("notebooks/images/ex2_tram_interior_reference.png")}

    ### 🏠 Mila's Apartment Building

    The first scene establishes where Mila's journey begins.

    Consider defining:

    - Architectural style
    - Building materials and colors
    - Windows
    - Entrance
    - Steps or pavement
    - Surrounding street

    This location only appears once in our current story, so ask yourself:

    > **Does this actually need a reference?**

    Perhaps it doesn't.

    Reference images cost time and, depending on the model, you may only be able to provide a limited number. Part of a production workflow is deciding **which elements need explicit control**.

    ### 🚪 Grandma's House

    Grandma's house is the destination and provides the final image of the story.

    Important characteristics might include:

    - An old European townhouse
    - Weathered stone or brick
    - A large green wooden front door
    - Brass lock and door furniture
    - Steps leading to the entrance
    - Warm light visible through nearby windows

    Again, this location currently appears only once. But the **green door** is important to the ending, so defining the door may be more useful than defining the entire house.

    ---

    ## Create Your References

    Review your own story and choose the objects, vehicles, and environments that would benefit most from references.

    For each one:

    1. Write down its defining visual characteristics.
    2. Decide which views would be useful.
    3. Generate a clean reference image.
    4. Include your style reference where appropriate.
    5. Inspect the reference itself for inconsistencies.
    6. Save the prompt and resulting image.

    Don't automatically create references for every noun in your story.

    > **The objective isn't to create the largest possible reference library. It's to identify which visual elements must remain stable for your story to feel like one coherent production.**
    """)
    return


@app.cell
def _():
    ex2_key_prompt = """
    Create an OBJECT REFERENCE SHEET for the brass key from the Mila story.

    Use the provided 'ex2_style_reference.png' image as the visual STYLE REFERENCE.

    OBJECT:
    An old-fashioned brass door key made from slightly aged and worn brass.
    The key is approximately 8 cm long.

    It has:
    - A large circular bow at the top
    - A narrow cylindrical shaft
    - Three distinctive rectangular teeth at the end
    - Small scratches and signs of age
    - A warm, slightly tarnished brass color

    REFERENCE SHEET:
    Show multiple clearly separated views of the SAME key:

    1. Front view
    2. Back view
    3. Side view
    4. Three-quarter perspective view

    CONSISTENCY:
    Every view must depict exactly the SAME physical key.

    Keep the proportions, circular bow, shaft, three teeth, material, color,
    wear, and small details consistent between all views.

    STYLE:
    Warm modern children's-book illustration with soft rounded shapes,
    subtle watercolor textures, a muted orange-and-blue color palette,
    natural lighting, and a friendly, optimistic atmosphere.

    Use the provided style reference as the primary guide for the visual
    appearance of the illustration.

    LAYOUT:
    Present the views as a clean object-design reference sheet on a simple
    neutral background. Make the key large enough that its shape and distinctive
    teeth are clearly visible.

    Do not include characters, hands, doors, or other objects.

    IMPORTANT:
    This image will be used as an OBJECT REFERENCE in multiple story illustrations.
    Prioritize a clear, distinctive, and reproducible object design.
    """
    return


@app.cell
def _():
    ex2_tram_exterior_prompt = """
    Create a VEHICLE REFERENCE SHEET for the tram used in the Mila story.

    Use the provided 'ex2_style_reference.png' image as the visual STYLE REFERENCE.

    VEHICLE:
    Design a friendly, slightly old-fashioned European city tram.

    The tram has:
    - A rounded front
    - A cream-colored upper body
    - A muted dark-blue lower body
    - A thin warm-orange stripe separating the two colors
    - Two connected sections
    - Large rectangular windows with softly rounded corners
    - Three passenger doors along the visible side
    - Two round headlights on the front
    - A simple pantograph connecting the tram to overhead wires
    - Dark metal wheels and undercarriage

    The design should feel practical and believable, but slightly simplified
    for a children's-book illustration.

    REFERENCE SHEET:
    Show multiple clearly separated views of the SAME tram:

    1. Front view
    2. Full side view
    3. Front three-quarter view
    4. Rear three-quarter view

    CONSISTENCY:
    Every view must depict exactly the SAME tram.

    Keep the body shape, proportions, windows, doors, colors, orange stripe,
    headlights, pantograph, and number of sections consistent between all views.

    STYLE:
    Warm modern children's-book illustration with soft rounded shapes,
    subtle watercolor textures, a muted orange-and-blue color palette,
    natural lighting, and a friendly, optimistic atmosphere.

    Use the provided style reference as the primary guide for the visual
    appearance of the illustration.

    LAYOUT:
    Present the different views as a clean professional vehicle-design reference
    sheet on a simple neutral background.

    Show the complete tram in each major view. Avoid dramatic perspective or
    environmental scenery that obscures the vehicle design.

    Do not include Mila or other prominent characters.

    IMPORTANT:
    This image will be used as the VEHICLE REFERENCE for the tram throughout
    the story.

    Prioritize a clear and reproducible vehicle design and consistency between
    the different views.
    """

    ex2_tram_interior_prompt = """
    Create an ENVIRONMENT REFERENCE SHEET for the INTERIOR of the tram used
    in the Mila story.

    Use the provided images as references:

    - 'ex2_style_reference.png' defines the VISUAL STYLE.
    - 'ex2_tram_exterior_reference.png' defines the TRAM.

    The interior must plausibly belong to the exact same tram shown in the
    provided exterior reference.

    TRAM INTERIOR:
    Design the passenger interior of this two-section European city tram.

    The interior has:
    - A central aisle running through the tram
    - Rows of paired passenger seats
    - Muted dark-blue upholstered seats
    - Cream-colored interior wall and ceiling panels
    - Warm-orange details that echo the stripe on the tram exterior
    - Large rectangular windows corresponding to the exterior windows
    - Passenger doors positioned consistently with the exterior reference
    - Dark non-slip flooring
    - Simple brushed-metal handrails and vertical poles
    - Soft overhead lighting

    The space should feel practical, welcoming, and slightly old-fashioned,
    matching the exterior design.

    EXTERIOR-INTERIOR CONSISTENCY:
    Use the exterior tram reference to determine the overall proportions,
    window placement, door placement, and visual design language.

    The interior should look like a believable interior of THAT tram,
    not a generic or unrelated train interior.

    REFERENCE SHEET:
    Show several useful views of the SAME tram interior:

    1. Wide view looking down the central aisle toward the front
    2. Wide view looking down the aisle in the opposite direction
    3. View of a typical seating area beside a window
    4. View showing a passenger door, nearby seats, and handrails

    CONSISTENCY:
    Every view must depict the SAME interior.

    Keep the seat design, colors, windows, doors, flooring, wall panels,
    handrails, lighting, and overall layout consistent between views.

    STYLE:
    Warm modern children's-book illustration with soft rounded shapes,
    subtle watercolor textures, a muted orange-and-blue color palette,
    natural lighting, and a friendly, optimistic atmosphere.

    Follow the provided style reference closely.

    LAYOUT:
    Present the different views as a clean environment-design reference sheet.
    The purpose is to clearly establish the tram interior rather than tell
    a story.

    Do not include Mila or other prominent characters.
    A completely empty tram is acceptable.

    IMPORTANT:
    This image will be used as an ENVIRONMENT REFERENCE for several consecutive
    scenes in the story.

    Prioritize spatial clarity, consistency between views, and consistency
    with the provided tram exterior over decorative details.
    """
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Challenge 3 — Try Again

    We now have more than just prompts.

    We've created a small **visual reference library** that defines the style, characters, objects, vehicles, and environments of our story.

    Now let's generate the story again.

    This time, use your reference images alongside your prompts and see whether they improve the results.

    ## Exercise 3.1 — Regenerate Your Story

    Return to the **5–8 scenes** you created in Challenge 1.

    For each scene:

    1. Start with your original scene prompt.
    2. Decide which reference images are relevant.
    3. Add those references to your image-generation tool.
    4. Update the prompt so it explicitly tells the model how each reference should be used.
    5. Generate the scene again.
    6. Save the new image so you can compare it with your original.

    For example, a scene from the Mila story might use:

    - **Style reference** — how the image should look
    - **Mila reference** — what Mila should look like
    - **Tram exterior reference** — what the tram should look like

    A later scene inside the tram might instead use:

    - **Style reference**
    - **Mila reference**
    - **Boy reference**
    - **Key reference**
    - **Tram interior reference**

    Don't automatically provide every reference to every prompt. Use the references that are **actually relevant to the scene**.

    ## Tell the Model What the References Mean

    Don't just upload several images and assume the model understands why they're there.

    Make their purpose explicit in your prompt:

    > Use `ex2_style_reference.png` as the **STYLE REFERENCE**.
    > Use `ex2_character_reference_mila.png` as the **CHARACTER REFERENCE for Mila**.
    > Use `ex2_tram_interior_reference.png` as the **ENVIRONMENT REFERENCE for the tram interior**.

    Then describe the scene as before.

    ## Keep the Target the Same

    We're trying to compare this workflow with our baseline.

    Don't completely redesign your story or deliberately improve every aspect of your prompts.

    The important difference should be:

    **Challenge 1:** Text description → Image

    **Challenge 3:** Text description + Visual references → Image

    That gives us something meaningful to compare.

    ---

    ## Exercise 3.2 — Compare the Results

    Put the **original and regenerated stories next to each other**.

    Don't just ask which images are prettier.

    Look specifically at what we tried to control.

    | Area | Challenge 1 | Challenge 3 |
    |---|---|---|
    | Visual style | Consistent? | Improved? |
    | Main character | Same person? | Improved? |
    | Clothing | Stable? | Improved? |
    | Recurring objects | Same design? | Improved? |
    | Vehicles | Same vehicle? | Improved? |
    | Environments | Recognizable? | Improved? |
    | Scene instructions | Followed? | Improved? |
    | Overall story | Feels coherent? | Improved? |

    Also look for **new problems**.

    Did references constrain the model in unexpected ways? Did it copy elements you didn't want? Did composition become harder to control? Did one reference seem to override another?

    ## Discuss

    Compare your results with the other groups.

    - How much did reference images improve consistency?
    - Which references were most effective?
    - What remained inconsistent?
    - Did adding more references always help?
    - Were some details easier to control than others?
    - How much additional work did the reference-based workflow require?
    - Were there differences between image models?
    - Would you now consider the result **production ready**?

    > **The question isn't whether references make the images better. The question is how much control they give us — and how much work is required to get there.**
    """)
    return


@app.cell
def _():
    ex3_scene_01_prompt = """
    Create the first illustration for the children's story "Mila and the Lost Key".

    REFERENCE IMAGES:
    - Use 'ex2_style_reference.png' as the STYLE REFERENCE.
    - Use 'ex2_character_reference_mila.png' as the CHARACTER REFERENCE for Mila.
    - Use 'ex2_key_reference.png' as the OBJECT REFERENCE for the brass key.

    Follow the provided references closely. Preserve their visual design rather
    than creating new interpretations.

    SCENE:
    It is a rainy morning in a quiet European city.

    Mila has just left her apartment and is on her way to visit her grandmother.
    She stands outside the entrance of her apartment building.

    Mila holds an open red umbrella in one hand and the old brass key in her
    other hand. The key should be clearly visible.

    The pavement is wet from the rain and reflects some of the surrounding
    buildings and soft morning light.

    CHARACTER:
    Mila is an eight-year-old girl with curly dark-brown shoulder-length hair,
    brown eyes, freckles, and a round face.

    She wears a bright yellow raincoat, dark-blue trousers, red rain boots,
    and a small blue backpack.

    Mila must match the provided character reference. Preserve her facial
    features, hairstyle, proportions, clothing design, clothing colors,
    boots, and backpack.

    IMPORTANT OBJECT:
    The brass key must match the provided object reference.

    It is an old-fashioned, slightly worn brass key with a large circular bow,
    a narrow shaft, and three distinctive teeth.

    Do not redesign or simplify the key.

    STYLE:
    Warm modern children's-book illustration with soft rounded shapes,
    subtle watercolor textures, and soft digital painting.

    Use a muted but warm palette dominated by orange, blue, soft green,
    and neutral stone colors.

    Use soft natural light from an overcast rainy morning, gentle reflections
    on wet surfaces, and a friendly, warm, optimistic atmosphere.

    The image should be moderately detailed and handcrafted rather than
    photorealistic.

    Follow the provided style reference closely for illustration technique,
    shapes, linework, palette, lighting, texture, and level of detail.

    COMPOSITION:
    Medium-wide, eye-level storybook composition.

    Mila is the clear focal point. Show enough of the apartment entrance and
    street to establish that she has just left home.

    The red umbrella and brass key should both be clearly readable.

    CONSISTENCY:
    This image is part of a multi-image story.

    Prioritize consistency with the provided references over introducing new
    character, object, or stylistic details.
    """

    ex3_scene_02_prompt = """
    Create the second illustration for the children's story "Mila and the Lost Key".

    REFERENCE IMAGES:
    - Use 'ex2_style_reference.png' as the STYLE REFERENCE.
    - Use 'ex2_character_reference_mila.png' as the CHARACTER REFERENCE for Mila.
    - Use 'ex2_tram_exterior_reference.png' as the VEHICLE REFERENCE for the tram.

    Follow the provided references closely. Preserve their visual design rather
    than creating new interpretations.

    SCENE:
    Mila waits at a tram stop in the pouring rain.

    She stands underneath her open red umbrella near the edge of the tram stop.
    The same tram established in the vehicle reference is approaching along
    the tracks in the background.

    The wet street and pavement reflect the tram lights and surrounding city.

    CHARACTER:
    Mila is an eight-year-old girl with curly dark-brown shoulder-length hair,
    brown eyes, freckles, and a round face.

    She wears a bright yellow raincoat, dark-blue trousers, red rain boots,
    and a small blue backpack.

    Mila must match the provided character reference. Preserve her face,
    hairstyle, proportions, clothing, colors, boots, and backpack.

    TRAM:
    The approaching tram must clearly be the SAME tram shown in
    'ex2_tram_exterior_reference.png'.

    Preserve its rounded shape, proportions, two connected sections,
    cream-colored upper body, muted dark-blue lower body, thin warm-orange stripe,
    large rectangular windows, passenger doors, round headlights, and pantograph.

    Do not redesign the tram.

    STYLE:
    Warm modern children's-book illustration with soft rounded shapes,
    subtle watercolor textures, and soft digital painting.

    Use a muted but warm palette dominated by orange, blue, soft green,
    and neutral stone colors.

    Use soft overcast natural lighting, visible rain, gentle reflections on
    wet pavement, and a friendly, slightly whimsical atmosphere.

    Follow the provided style reference closely for illustration technique,
    linework, palette, lighting, texture, and level of detail.

    COMPOSITION:
    Wide, eye-level street view.

    Mila is prominent in the foreground at the tram stop.
    The approaching tram is clearly visible in the background.

    Show enough of the European city environment to establish the rainy setting,
    but keep Mila and the tram as the primary visual elements.

    CONSISTENCY:
    This is the same Mila and the same tram established by the reference images.

    Prioritize visual continuity with those references over introducing new
    design details.
    """

    ex3_scene_03_prompt = """
    Create the third illustration for the children's story "Mila and the Lost Key".

    REFERENCE IMAGES:
    - Use 'ex2_style_reference.png' as the STYLE REFERENCE.
    - Use 'ex2_character_reference_mila.png' as the CHARACTER REFERENCE for Mila.
    - Use 'ex2_tram_exterior_reference.png' as supporting reference for the TRAM.
    - Use 'ex2_tram_interior_reference.png' as the ENVIRONMENT REFERENCE for
      the tram interior.

    The scene takes place INSIDE the exact tram established by these references.

    SCENE:
    Mila is sitting inside the tram when she suddenly realizes that her old
    brass key is missing.

    She looks worried and searches the pockets of her yellow raincoat.

    Her closed red umbrella rests beside her.

    Rain is visible through the tram window.

    CHARACTER:
    Mila is an eight-year-old girl with curly dark-brown shoulder-length hair,
    brown eyes, freckles, and a round face.

    She wears a bright yellow raincoat, dark-blue trousers, red rain boots,
    and a small blue backpack.

    Mila must match the provided character reference closely.

    Preserve her facial features, hairstyle, proportions, raincoat design,
    trousers, boots, backpack, and colors.

    EXPRESSION AND ACTION:
    Mila should look genuinely concerned but not frightened.

    Her hands should clearly be searching the pockets of her raincoat so that
    the viewer can understand what is happening without additional text.

    TRAM INTERIOR:
    The environment must match 'ex2_tram_interior_reference.png'.

    Preserve the established central aisle, dark-blue upholstered seats,
    cream-colored panels, warm-orange details, large windows, dark flooring,
    metal handrails, and soft overhead lighting.

    The interior must also remain visually plausible as the inside of the tram
    shown in 'ex2_tram_exterior_reference.png'.

    STYLE:
    Warm modern children's-book illustration with soft rounded shapes,
    subtle watercolor textures, soft digital painting, and a muted but warm
    orange-and-blue palette.

    Use natural overcast lighting entering through the windows together with
    soft interior lighting.

    The atmosphere remains warm and approachable despite Mila's concern.

    Follow the provided style reference closely.

    COMPOSITION:
    Medium, eye-level shot.

    Mila is seated next to a window and is the clear focal point.
    Show enough of the seats, aisle, window, and tram interior to make the
    location immediately recognizable.

    CONSISTENCY:
    Preserve the established character, tram, and visual style.

    Do not redesign Mila or the tram interior.
    """

    ex3_scene_04_prompt = """
    Create the fourth illustration for the children's story "Mila and the Lost Key".

    REFERENCE IMAGES:
    - Use 'ex2_style_reference.png' as the STYLE REFERENCE.
    - Use 'ex2_character_reference_mila.png' as the CHARACTER REFERENCE for Mila.
    - Use 'ex2_tram_exterior_reference.png' as supporting reference for the TRAM.
    - Use 'ex2_tram_interior_reference.png' as the ENVIRONMENT REFERENCE for
      the tram interior.

    This is the SAME Mila and SAME tram shown in the previous scenes.

    SCENE:
    Mila searches underneath the seats of the tram for her missing brass key.

    She kneels in the central aisle and bends down to look underneath one of
    the seats.

    Her closed red umbrella is lying nearby.

    Several passengers remain seated and watch curiously, but they are secondary
    background characters.

    The brass key has NOT been found yet and should NOT be visible.

    CHARACTER:
    Mila is an eight-year-old girl with curly dark-brown shoulder-length hair,
    brown eyes, freckles, and a round face.

    She wears a bright yellow raincoat, dark-blue trousers, red rain boots,
    and a small blue backpack.

    Mila must match the provided character reference closely.

    Preserve her face, hair, body proportions, clothing design, colors,
    boots, and backpack.

    POSE:
    Mila is kneeling naturally in the aisle and looking underneath a seat.

    Make the pose physically believable and ensure that her arms, hands,
    legs, clothing, and nearby furniture interact naturally.

    TRAM INTERIOR:
    Match the provided tram interior reference closely.

    Preserve the dark-blue seats, cream-colored panels, orange details,
    large windows, central aisle, dark floor, metal handrails, and lighting.

    The tram should clearly be the same environment as scene 3.

    STYLE:
    Warm modern children's-book illustration with soft rounded shapes,
    subtle watercolor textures, soft digital painting, a muted warm palette,
    and natural lighting.

    Follow the provided style reference closely.

    COMPOSITION:
    Wide, eye-level interior shot looking along the aisle.

    Mila is near the center of the composition and clearly visible searching
    underneath a seat.

    Show enough of the surrounding seats and tram architecture to make
    environmental continuity visible.

    CONSISTENCY:
    Prioritize continuity with the established Mila and tram interior.

    Do not introduce unnecessary changes to clothing, seat design, colors,
    windows, or other established visual details.
    """

    ex3_scene_05_prompt = """
    Create the fifth illustration for the children's story "Mila and the Lost Key".

    REFERENCE IMAGES:
    - Use 'ex2_style_reference.png' as the STYLE REFERENCE.
    - Use 'ex2_character_reference_mila.png' as the CHARACTER REFERENCE for Mila.
    - Use 'ex2_character_reference_boy.png' as the CHARACTER REFERENCE for the boy.
    - Use 'ex2_key_reference.png' as the OBJECT REFERENCE for the brass key.
    - Use 'ex2_tram_exterior_reference.png' as supporting reference for the TRAM.
    - Use 'ex2_tram_interior_reference.png' as the ENVIRONMENT REFERENCE for
      the tram interior.

    Follow each reference according to its assigned role.

    SCENE:
    Inside the tram, the young boy has discovered Mila's missing brass key
    underneath a seat.

    The boy holds the key out toward Mila.

    Mila looks relieved and reaches toward him to accept it.

    This should feel like the emotional resolution of the search from the
    previous scenes.

    MILA:
    Mila is an eight-year-old girl with curly dark-brown shoulder-length hair,
    brown eyes, freckles, and a round face.

    She wears a bright yellow raincoat, dark-blue trousers, red rain boots,
    and a small blue backpack.

    Mila must closely match 'ex2_character_reference_mila.png'.

    THE BOY:
    The boy is seven years old with short blond hair, blue eyes, and a friendly
    round face.

    He wears a soft green jacket, brown trousers, and simple white sneakers.

    He must closely match 'ex2_character_reference_boy.png'.

    Do not blend the visual characteristics of the two character references.

    BRASS KEY:
    The boy is holding the SAME brass key established in 'ex2_key_reference.png'.

    Preserve its aged brass material, large circular bow, narrow shaft,
    and three distinctive teeth.

    The key should be clearly visible between the two characters.

    TRAM INTERIOR:
    The scene takes place in the SAME tram interior established by
    'ex2_tram_interior_reference.png'.

    Preserve its seat design, colors, windows, panels, flooring, handrails,
    and general layout.

    STYLE:
    Warm modern children's-book illustration with soft rounded shapes,
    subtle watercolor textures, soft digital painting, and a muted warm
    orange-and-blue palette.

    Use natural lighting and a friendly, optimistic atmosphere.

    Follow the provided style reference closely.

    COMPOSITION:
    Medium, eye-level shot showing Mila and the boy together.

    The boy holds the brass key clearly between them while Mila reaches toward it.

    Their expressions, interaction, and the key are the primary focus.
    The tram interior remains recognizable but secondary.

    CONSISTENCY:
    Preserve both character identities independently.

    The key and tram must remain consistent with their respective references.

    Do not redesign established characters, objects, or environments.
    """

    ex3_scene_06_prompt = """
    Create the final illustration for the children's story "Mila and the Lost Key".

    REFERENCE IMAGES:
    - Use 'ex2_style_reference.png' as the STYLE REFERENCE.
    - Use 'ex2_character_reference_mila.png' as the CHARACTER REFERENCE for Mila.
    - Use 'ex2_key_reference.png' as the OBJECT REFERENCE for the brass key.

    Follow the provided references closely and preserve their established designs.

    SCENE:
    Mila has arrived at her grandmother's old house after the rain.

    She stands at the entrance in front of a large green wooden front door.

    Mila inserts the old brass key into the lock and turns it to unlock the door.

    Her closed red umbrella is held in her other hand.

    The rain has stopped, but the pavement and steps are still wet.
    A subtle warm light from the house makes the scene feel welcoming.

    CHARACTER:
    Mila is an eight-year-old girl with curly dark-brown shoulder-length hair,
    brown eyes, freckles, and a round face.

    She wears a bright yellow raincoat, dark-blue trousers, red rain boots,
    and a small blue backpack.

    Mila must closely match 'ex2_character_reference_mila.png'.

    Preserve her facial features, hairstyle, proportions, clothing design,
    colors, boots, and backpack.

    BRASS KEY:
    The key in the lock must clearly be the SAME key shown in
    'ex2_key_reference.png'.

    Preserve its aged brass material, large circular bow, narrow shaft,
    and three distinctive teeth.

    The key should be clearly visible interacting naturally with the door lock.

    ENVIRONMENT:
    Grandmother's house is an old, welcoming European townhouse.

    The entrance has:
    - A large weathered green wooden front door
    - A brass lock and simple brass door furniture
    - A stone doorway and small stone steps
    - Subtle signs of age and use
    - Warm light visible from inside or through a nearby window

    The architecture should belong naturally to the same European city
    established earlier in the story.

    STYLE:
    Warm modern children's-book illustration with soft rounded shapes,
    subtle watercolor textures, and soft digital painting.

    Use a muted but warm palette dominated by orange, blue, soft green,
    and neutral stone colors.

    The rain has stopped, so use soft natural post-rain lighting, gentle
    reflections on wet surfaces, and subtle warm light from the house.

    The mood should feel safe, warm, satisfying, and optimistic.

    Follow 'ex2_style_reference.png' closely for illustration technique,
    shapes, linework, palette, texture, lighting, and level of detail.

    COMPOSITION:
    Medium-wide, eye-level storybook composition.

    Mila and the large green door are the main focus.

    Show Mila using the brass key in the lock. The interaction between her hand,
    the key, and the lock should be clear and physically believable.

    Show enough of the old house entrance to create a satisfying visual ending
    without allowing the environment to overwhelm Mila.

    CONSISTENCY:
    This is the final scene of the same visual story.

    Mila and the brass key must remain consistent with their reference images,
    and the illustration must remain consistent with the established visual style.

    Prioritize continuity and instruction adherence over introducing new
    decorative details.
    """
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        f"""
    # Example — The Lost Key, Take Two

    We've now regenerated the complete **Mila and the Lost Key** story using our
    style, character, object, and environment references.

    Compare these images with the baseline from Challenge 1. Do the references
    make the story feel more like a single, coherent visual production?

    ---

    ## 1. Leaving Home

    {mo.image("notebooks/images/ex3_scene01.png")}

    Mila leaves her apartment on a rainy morning to visit her grandmother.
    She carries her red umbrella and the old brass key.

    ---

    ## 2. The Tram Stop

    {mo.image("notebooks/images/ex3_scene02.png")}

    Mila waits at the tram stop in the pouring rain. In the distance, her tram
    approaches through the wet city streets.

    ---

    ## 3. Something Is Missing

    {mo.image("notebooks/images/ex3_scene03.png")}

    Sitting inside the tram, Mila suddenly realizes that something is wrong.
    She searches the pockets of her yellow raincoat.

    **The old brass key is gone!**

    ---

    ## 4. The Search

    {mo.image("notebooks/images/ex3_scene04.png")}

    Mila searches underneath the tram seats while the other passengers look on.

    But where could the key be?

    ---

    ## 5. Found!

    {mo.image("notebooks/images/ex3_scene05.png")}

    A young boy discovers something underneath one of the seats.

    It's Mila's brass key!

    He returns it to a very relieved Mila.

    ---

    ## 6. The Green Door

    {mo.image("notebooks/images/ex3_scene06.png")}

    Mila finally arrives at her grandmother's house.

    She puts the old brass key into the large green door and turns it.

    **She made it!**

    ---

    ## 🔎 Compare With the Baseline

    Look at the complete sequence before focusing on individual images.

    Consider:

    - **Mila** — Does she now look like the same character throughout?
    - **Style** — Do the six images feel like they belong to the same book?
    - **Clothing** — Are Mila's raincoat, boots, trousers, and backpack consistent?
    - **Tram** — Does the tram remain recognizable between exterior and interior scenes?
    - **Key** — Is it recognizably the same object when it reappears?
    - **Environment** — Do recurring locations feel more coherent?
    - **Details** — What still changes unexpectedly?
    - **Artifacts** — Can you find anything that looks convincing at first glance but falls apart on closer inspection?

    > ### Discussion
    >
    > Did the reference-based workflow produce a **meaningful improvement** over
    > text prompting alone?
    >
    > What problems did it solve? What problems remain? And how much additional
    > work did it take to get here?
    """
    )
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
