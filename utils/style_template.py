style_list = [
    {
        "name": "No_style",
        "prompt": "{prompt} 8k,RAW",
        "negative_prompt": "worst quality",
    },
    {
        "name": "Realistic",
        "prompt": "{prompt}  (photorealistic:1.4),8k,RAW photo, best quality, masterpiece,dramatic shadows,uhd, high quality,dramatic,cinematic",
        "negative_prompt": "(worst quality, low quality, normal quality, lowres), (bad teeth, deformed teeth, deformed lips), (bad proportions), (deformed eyes, bad eyes), (deformed face, ugly face), (deformed hands,fused fingers), morbid, mutilated, mutation, disfigured",
    },
    {
        "name": "Japanese_Anime",
        "prompt": "{prompt} (anime key visual:1.5), (by CLAMP:1.4),  Chobits style, detailed anime illustration, clean line art, elegant composition, expressive eyes, soft cel shading, thin outlines, masterpiece, best quality",
        "negative_prompt": "lowres,text, error, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry",
    },
    {
        "name": "Digital_Oil_Painting",
        "prompt": "{prompt}  traditional oil on canvas, (heavy impasto:1.3) , (visible brushwork on the face and skin 1.1), textured canvas visible through the paint, unfinished artistic feel, rich color layers, in the style of (John Singer Sargent/Valentin Serov 1.4),  8k resolution photograph of the painting",
        "negative_prompt": "anime, cartoon, graphic, text, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured, lowres, error, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry",
    },
    {
        "name": "Pixar_Disney_Character",
        "prompt": "{prompt}  (Pixar style 3D character design 1.5), (Disney style 1.5), Unreal Engine 5 render, vibrant color palette, soft volumetric lighting, incredibly detailed, expressive eyes, trending on CGSociety and Artstation, 8k. The scene is vibrant, motivational, filled with vivid colors and a sense of wonder.",
        "negative_prompt": "lowres, text, bad eyes, bad legs, error,extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, blurry, grayscale, noisy, sloppy, messy, grainy,ultra textured,",
    },
    {
        "name": "Photographic",
        "prompt": "cinematic photo {prompt}  Hyperrealistic, Hyperdetailed, detailed skin,soft lighting, best quality, ultra realistic, 8k, golden ratio, Intricate, High Detail, film photography",
        "negative_prompt": "drawing, painting, crayon, sketch, graphite, impressionist, noisy, blurry, soft, deformed, ugly, lowres, text, error,  extra digit, fewer digits, cropped, worst quality, low quality,signature, watermark, username",
    },
    {
        "name": "Comic_book",
        "prompt": "{prompt} (Bruce Timm style:1.4),  (inked by Kevin Nowlan:1.3), American comic book art, bold ink lines, sharp angular anatomy, cel-shaded, limited color palette, heroic expression, 2D illustration.",
        "negative_prompt": "photograph, deformed, glitch, noisy, realistic, stock photo, lowres,text, error,extra digit, fewer digits, cropped, worst quality, low quality, normal quality,signature, watermark, username, blurry",
    },
    {
        "name": "Line_art",
        "prompt": "{prompt}  (line art style:1.4), (clean black and white ink drawing:1.3), (fine outlines:1.3), (minimal shading), (contour emphasis), (studio ghibli storyboard style:1.2), masterful composition, perfect perspective, expressive linework, smooth flow, elegant silhouette, sketchbook aesthetic, white background, (anime illustration:1.1), high detail, ultra clean, minimalist composition, precise form definition",
        "negative_prompt": "photorealistic, 35mm film, deformed, glitch, blurry, noisy, off-center, deformed, cross-eyed, closed eyes,ugly, disfigured, mutated, realism, realistic, impressionism, expressionism,acrylic, lowres, text, error,extra digit, fewer digits,  worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username",
    },
    {
        "name": "Black_and_White_Film_Noir",
        "prompt": "{prompt}  (b&w, Monochromatic, Film Photography:1.3), film noir, analog style, soft lighting, subsurface scattering,heavy shadow, masterpiece, best quality,",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, blurry, noisy, off-center, deformed, cross-eyed, closed eyes,ugly, disfigured, mutated, impressionism, expressionism,acrylic, lowres,text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username",
    },
    {
        "name": "Isometric_Rooms",
        "prompt": "{prompt}  (Hyper-detailed 3D character figurine 1.5), (realistic PVC toy texture 1.3), tiny cute isometric, soft cinematic lighting, studio setup, shallow depth of field, rendered in blender, premium collectible figure, elegant pose, 100mm macro lens, smooth plastic skin, realistic materials, high-quality render",
        "negative_prompt": "photorealistic,35mm film,deformed,glitch,blurry,noisy,off-center,deformed,cross-eyed,closed eyes,ugly,disfigured,mutated,realism,realistic,impressionism,expressionism,acrylic,lowres,text,error,extra digit,fewer digits,cropped, worst quality, low quality, normal quality, jpeg artifacts, signature,watermark, username,",
    },
    {
        "name": "Chinese_Painting",
        "prompt": "{prompt} (Chinese ink wash painting 1.1), (by Xu Beihong and Qi Baishi style 1.2), expressive brushstrokes, xuan paper, poetic minimalism, elegant and powerful, monochrome ink tones",
        "negative_prompt": "(seal 1.5), (stamp 1.5), (chop 1.5), (red stamp 1.5), red seal, worst quality, low quality, normal quality, lowres, bad anatomy, bad hands, deformed hands, fused fingers, missing fingers, extra limbs, long neck, watermark, signature, text, title, username,cartoon, 3d, render, cg, pixel art, anime, western comic, oil painting, photorealistic, digital art, vibrant colors, saturated colors, colorful, glossy, overexposed, underexposed, grainy, blurry, messy composition",
    }
]

styles = {k["name"]: (k["prompt"], k["negative_prompt"]) for k in style_list}
