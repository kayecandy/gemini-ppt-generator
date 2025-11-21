# Design Overview: GenAI-Powered Presentation Generator

## Executive Summary

This document outlines the end-to-end architecture of a presentation generation system that leverages Google's Gemini AI to transform user prompts into professionally formatted PowerPoint presentations while maintaining brand consistency and layout integrity.

---

## 1. User Input Handling

### Input Collection & Processing

The system accepts user input through a structured markdown format (`input/prompt.md`) that contains:

- **Topic/Theme**: The main subject of the presentation
- **Target Audience**: Context for tone and depth of content
- **Key Points**: Specific areas to cover or emphasize
- **Slide Count**: Desired presentation length (optional)

**Processing Flow:**

1. **Input Validation**: The system reads and validates the prompt file, ensuring all required fields are present
2. **Context Enrichment**: Additional context (brand guidelines, tone preferences) is merged with user input
3. **Prompt Engineering**: User requirements are transformed into a detailed instruction set for the GenAI model, including:
   - Structured output requirements (JSON schema)
   - Content constraints (character limits per placeholder)
   - Slide layout specifications
   - Formatting guidelines

---

## 2. GenAI Content Generation

### Gemini Integration Architecture

The system uses Google's Gemini 1.5 Pro model through the `google-generativeai` Python SDK to generate presentation content.

**Generation Process:**

1. **Schema-Driven Generation**: The model is provided with a JSON schema defining:
   ```json
   {
     "presentation_title": "string",
     "slides": [
       {
         "slide_number": "integer",
         "layout_type": "TITLE_SLIDE | TITLE_AND_CONTENT | etc.",
         "content": {
           "Title": "string",
           "Content Placeholder": ["bullet1", "bullet2"],
           ...
         }
       }
     ]
   }
   ```

2. **Layout Templates**: The system provides the AI with available slide layouts from `slide_layouts.json`, which maps each layout to its placeholder names and types

3. **Content Constraints**: Each placeholder has character limits to prevent overflow:
   - Titles: 100 characters
   - Body text: 500 characters per placeholder
   - Bullet points: 80 characters each

4. **Structured Output**: Gemini's response is formatted as valid JSON, ensuring machine-readable output that maps directly to PowerPoint placeholders

**Safety & Quality Controls:**

- Temperature settings for creativity balance (0.7 typical)
- Content safety filters
- Retry logic for malformed responses
- Validation of generated JSON against schema

---

## 3. Template Application

### Branded Template Integration

The system uses `python-pptx` library to apply generated content to a pre-designed PowerPoint template (`branding.pptx`).

**Application Process:**

1. **Template Loading**: The branded template is loaded with pre-configured:
   - Corporate color schemes
   - Font families and sizes
   - Logo placements
   - Master slide layouts

2. **Layout Selection**: For each slide in the generated content:
   - Match `layout_type` from JSON to the corresponding template layout
   - Create new slide using the matched layout

3. **Content Mapping**: Systematically populate placeholders:
   ```python
   for placeholder in slide.placeholders:
       if placeholder.name in content:
           # Map content to placeholder
           if placeholder.placeholder_format.type == TEXT:
               placeholder.text = content[placeholder.name]
           elif placeholder.placeholder_format.type == OBJECT:
               # Handle special cases (charts, images)
   ```

4. **Formatting Preservation**: The system:
   - Preserves existing font styles and sizes from template
   - Maintains paragraph formatting (alignment, spacing)
   - Respects text box boundaries
   - Retains brand colors and design elements

**Content Type Handling:**

- **Text Placeholders**: Direct string assignment
- **Bullet Lists**: Paragraph-level formatting with proper indentation
- **Titles**: Center alignment with title styling
- **Subtitles**: Secondary formatting as defined in template

---

## 4. Layout Consistency & Integrity

### Structure Preservation Strategy

The system employs multiple mechanisms to ensure layout integrity:

#### 4.1 Pre-Generation Validation

**Layout Discovery**: The `slide_layouts.json` reference file was created based on the combined output of `analyze_template.py` and `debug_placeholders.py` scripts, which:
- Extract all available layouts from the template
- Map placeholder names and types for each layout
- Ensure the AI only references valid layouts and placeholders

**Prompt Constraints**: The AI prompt explicitly includes:
- List of available layouts
- Placeholder names for each layout
- Character limits for each placeholder type

#### 4.2 Content-Layout Matching

**Strict Mapping**: 
- AI generates `layout_type` for each slide
- System validates layout exists in template before slide creation
- Fallback to default layout if specified layout unavailable

**Placeholder Validation**:
```python
available_placeholders = {p.name for p in slide.placeholders}
for key in content.keys():
    if key not in available_placeholders:
        log_warning(f"Placeholder {key} not found in layout")
```

#### 4.3 Content Overflow Prevention

**Character Limits**: Enforced at generation time
- Title: max 100 chars
- Body: max 500 chars
- Bullets: max 80 chars each

**Dynamic Adjustment**: If content exceeds limits:
- Truncation with ellipsis
- Split into multiple slides
- Warning logged for manual review

**Text Fitting**: Using `python-pptx` auto-fit settings:
- Shrink text on overflow (controlled)
- Do not auto-fit (preserve exact template sizing)

#### 4.4 Post-Generation Validation

**Quality Checks**:
- Verify all slides created successfully
- Confirm no empty placeholders (unless intentional)
- Validate placeholder content matches expected type
- Log any layout inconsistencies

**Manual Review Flags**: System identifies slides requiring review:
- Content approaching character limits (>90%)
- Fallback layouts used
- Placeholder mismatches

---

## Technical Architecture Summary

```
User Input (prompt.md)
    ↓
Input Processor
    ↓
Prompt Engineer → [Layout Specs (slide_layouts.json)]
    ↓
Google Gemini API (JSON Schema)
    ↓
JSON Response Validator
    ↓
Template Loader (template.pptx)
    ↓
Content-Layout Mapper
    ↓
PowerPoint Generator (python-pptx)
    ↓
Output Validation
    ↓
Final Presentation (output.pptx)
```

---

## Key Benefits

1. **Consistency**: AI-generated content always conforms to template structure
2. **Scalability**: Single template supports multiple presentation types
3. **Brand Integrity**: Template-based approach ensures brand compliance
4. **Quality Control**: Multi-layer validation prevents layout breaks
5. **Flexibility**: JSON schema allows easy adaptation to new layouts

---

## Future Enhancements

- **Dynamic Layout Selection**: AI chooses optimal layout based on content type
- **Image Integration**: Automatic image search and placement
- **Chart Generation**: Data-driven visualization creation
- **Multi-template Support**: Template selection based on presentation purpose
- **Iterative Refinement**: User feedback loop for content improvement

