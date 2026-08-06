import json
import os


def detect_category(filename):

    filename = filename.lower()


    if "about" in filename:
        return "organization"

    elif "technical" in filename:
        return "technical_area"

    elif "publication" in filename:
        return "publication"

    elif "training" in filename:
        return "training"

    elif "event" in filename:
        return "event"

    elif "career" in filename:
        return "career"

    elif "contact" in filename:
        return "contact"

    elif "support" in filename:
        return "support"

    else:
        return "general"



def detect_subcategory(filename):

    filename = filename.lower()


    # Technical areas

    if "e-mobility" in filename:
        return "e_mobility"


    elif "climate-change" in filename:
        return "climate_change"


    elif "energy-access" in filename:
        return "energy_access"


    elif "energy-informatics" in filename:
        return "energy_informatics"


    elif "oil-and-gas" in filename:
        return "oil_and_gas"


    elif "power-sector" in filename:
        return "power_sector"


    elif "sustainable-infra" in filename:
        return "sustainable_infrastructure"



    # Publications

    elif "research-papers" in filename:
        return "research_paper"


    elif "reports" in filename:
        return "report"


    elif "datasets" in filename:
        return "dataset"


    elif "tools" in filename:
        return "tool"



    # Training

    elif "training" in filename:
        return "professional_training"


    return "general"




def detect_document_type(category):

    mapping = {

        "organization": "organization_information",

        "technical_area": "technical_information",

        "publication": "publication_document",

        "training": "training_material",

        "event": "event_information",

        "career": "career_information",

        "contact": "contact_information",

        "support": "support_information",

        "general": "general_document"

    }


    return mapping.get(
        category,
        "general_document"
    )





def extract_title(filename):

    title = filename.replace(
        ".txt",
        ""
    )

    title = title.replace(
        "_",
        " "
    )

    title = title.replace(
        "-",
        " "
    )

    return title.title()




def extract_keywords(content):

    keywords = []

    keyword_list = [

        "energy",
        "renewable",
        "solar",
        "battery",
        "electric vehicle",
        "ev",
        "power",
        "grid",
        "sustainability",
        "climate",
        "data"

    ]


    text = content.lower()


    for word in keyword_list:

        if word in text:
            keywords.append(word)


    return keywords





def create_metadata(
        filename,
        content,
        url
):

    category = detect_category(filename)


    metadata = {

        "source": filename,

        "url": url,

        "title": extract_title(filename),

        "category": category,

        "subcategory": detect_subcategory(filename),

        "document_type": detect_document_type(category),

        "keywords": extract_keywords(content),

        "length": len(content)

    }


    return {

        "content": content,

        "metadata": metadata

    }





def save_metadata(documents):

    os.makedirs(
        "metadata",
        exist_ok=True
    )


    with open(
        "metadata/documents.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            documents,
            f,
            indent=4,
            ensure_ascii=False
        )