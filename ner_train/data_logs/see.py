import spacy
from spacy.tokens import Span

# Define the custom entity label
LABEL = 'ADDRESS'

# Define the custom entity patterns
address_patterns = [
    {"label": LABEL, "pattern": [{"LOWER": {"IN": ["avenue", "blvd", "boulevard"]}}]}, 
    {"label": LABEL, "pattern": [{"LOWER": "drive"}]},
    {"label": LABEL, "pattern": [{"LOWER": "lane"}]},
    {"label": LABEL, "pattern": [{"LOWER": "road"}]},
    {"label": LABEL, "pattern": [{"LOWER": "street"}]},
    {"label": LABEL, "pattern": [{"LOWER": "suite"}]},
    {"label": LABEL, "pattern": [{"LOWER": "apt"}]},
    {"label": LABEL, "pattern": [{"LOWER": "apartment"}]},
    {"label": LABEL, "pattern": [{"LOWER": "building"}]},
    {"label": LABEL, "pattern": [{"LOWER": "floor"}]},
    {"label": LABEL, "pattern": [{"LOWER": "room"}]},
    {"label": LABEL, "pattern": [{"LOWER": "unit"}]}
]

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Add the custom entity patterns to the pipeline
ruler = nlp.add_pipe("entity_ruler", before='ner')
ruler.add_patterns(address_patterns)

# Define the text to be processed
text = "Join us at 1234 Sunset Boulevard, Suite 5678, in Los Angeles, CA 90012 for a workshop."

# Process the text with spaCy
doc = nlp(text)

# Extract the entities
entities = [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents if ent.label_ == LABEL]

# Print the extracted entities
print(entities)