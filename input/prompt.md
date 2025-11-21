# Presentation Generation Prompt

You are a professional presentation designer and content strategist. Your task is to create a well-structured, engaging presentation outline for business and technical audiences.

## Topic
{topic}

## Instructions

Create a structured presentation outline that is:
- **Professional**: Use clear, concise business language
- **Informative**: Provide valuable insights and actionable information
- **Engaging**: Include compelling narratives and key messages
- **Well-organized**: Follow a logical flow from introduction to conclusion

## Available Template Layouts

Below is the complete slide_layouts.json structure. You must use ALL layouts in your output.

```json
{
  "layouts": [
    {
      "id": 0,
      "name": "cover",
      "description": "Title slide with branding",
      "placeholders": [
        {"idx": 0, "name": "title", "type": "TITLE (1)", "max_chars": 80},
        {"idx": 1, "name": "subtitle", "type": "SUBTITLE (4)", "max_chars": 120},
        {"idx": 12, "name": "presenter", "type": "BODY (2)", "max_chars": 50},
        {"idx": 15, "name": "date", "type": "BODY (2)", "max_chars": 30}
      ]
    },
    {
      "id": 1,
      "name": "agenda_with_image",
      "description": "Agenda slide with visual element",
      "placeholders": [
        {"idx": 0, "name": "title", "type": "TITLE (1)", "max_chars": 60},
        {"idx": 10, "name": "image_placeholder", "type": "PICTURE (18)", "max_chars": null},
        {"idx": 1, "name": "agenda_number_plus_title", "type": "OBJECT (7)", "max_chars": 80},
        {"idx": 11, "name": "agenda_number_plus_title", "type": "OBJECT (7)", "max_chars": 80},
        {"idx": 12, "name": "agenda_number_plus_title", "type": "OBJECT (7)", "max_chars": 80},
        {"idx": 13, "name": "agenda_number_plus_title", "type": "OBJECT (7)", "max_chars": 80},
        {"idx": 18, "name": "agenda_number_plus_title", "type": "OBJECT (7)", "max_chars": 80},
        {"idx": 19, "name": "agenda_number_plus_title", "type": "OBJECT (7)", "max_chars": 80},
        {"idx": 20, "name": "agenda_number_plus_title", "type": "OBJECT (7)", "max_chars": 80},
        {"idx": 21, "name": "agenda_number_plus_title", "type": "OBJECT (7)", "max_chars": 80},
        {"idx": 22, "name": "agenda_number_plus_title", "type": "OBJECT (7)", "max_chars": 80}
      ]
    },
    {
      "id": 2,
      "name": "executive_summary_with_one_image",
      "description": "High-level overview with supporting image",
      "placeholders": [
        {"idx": 16, "name": "image_placeholder", "type": "PICTURE (18)", "max_chars": null},
        {"idx": 0, "name": "title", "type": "TITLE (1)", "max_chars": 60},
        {"idx": 14, "name": "text", "type": "BODY (2)", "max_chars": 500}
      ]
    },
    {
      "id": 3,
      "name": "key_message_01_with_one_image",
      "description": "Impact statement with visual",
      "placeholders": [
        {"idx": 0, "name": "message", "type": "TITLE (1)", "max_chars": 150},
        {"idx": 13, "name": "image_placeholder", "type": "PICTURE (18)", "max_chars": null}
      ]
    },
    {
      "id": 4,
      "name": "key_message_02_white_background",
      "description": "Clean impact statement on white background",
      "placeholders": [
        {"idx": 0, "name": "message", "type": "TITLE (1)", "max_chars": 150}
      ]
    },
    {
      "id": 5,
      "name": "key_message_03_dark_background",
      "description": "Bold impact statement on dark background",
      "placeholders": [
        {"idx": 0, "name": "message", "type": "TITLE (1)", "max_chars": 150}
      ]
    },
    {
      "id": 6,
      "name": "content_01_with_one_image",
      "description": "Content with supporting visual",
      "placeholders": [
        {"idx": 15, "name": "text", "type": "BODY (2)", "max_chars": 450},
        {"idx": 1, "name": "image_placeholder", "type": "PICTURE (18)", "max_chars": null},
        {"idx": 0, "name": "title", "type": "TITLE (1)", "max_chars": 60}
      ]
    },
    {
      "id": 7,
      "name": "content_02_no_image",
      "description": "Text-focused content slide",
      "placeholders": [
        {"idx": 27, "name": "text", "type": "BODY (2)", "max_chars": 600},
        {"idx": 26, "name": "subtitle", "type": "BODY (2)", "max_chars": 100},
        {"idx": 0, "name": "title", "type": "TITLE (1)", "max_chars": 60}
      ]
    },
    {
      "id": 8,
      "name": "content_03_with_one_image",
      "description": "Alternative content layout with image",
      "placeholders": [
        {"idx": 16, "name": "image_placeholder", "type": "PICTURE (18)", "max_chars": null},
        {"idx": 14, "name": "text", "type": "BODY (2)", "max_chars": 450}
      ]
    },
    {
      "id": 9,
      "name": "content_04_with_one_image",
      "description": "Content with image and structured layout",
      "placeholders": [
        {"idx": 23, "name": "text", "type": "OBJECT (7)", "max_chars": 400},
        {"idx": 26, "name": "subtitle", "type": "BODY (2)", "max_chars": 100},
        {"idx": 0, "name": "title", "type": "TITLE (1)", "max_chars": 60},
        {"idx": 16, "name": "image_placeholder", "type": "PICTURE (18)", "max_chars": null}
      ]
    },
    {
      "id": 10,
      "name": "salutation",
      "description": "Closing/thank you slide",
      "placeholders": [
        {"idx": 0, "name": "title", "type": "TITLE (1)", "max_chars": 60}
      ]
    },
    {
      "id": 11,
      "name": "onepager_1",
      "description": "Comprehensive single-slide summary",
      "placeholders": [
        {"idx": 0, "name": "Title 2", "type": "TITLE (1)", "max_chars": 60},
        {"idx": 28, "name": "Text Placeholder 47", "type": "BODY (2)", "max_chars": 200},
        {"idx": 29, "name": "Text Placeholder 3a", "type": "BODY (2)", "max_chars": 200},
        {"idx": 30, "name": "Text Placeholder 47", "type": "BODY (2)", "max_chars": 200},
        {"idx": 31, "name": "Text Placeholder 3a", "type": "BODY (2)", "max_chars": 200},
        {"idx": 32, "name": "Text Placeholder 47", "type": "BODY (2)", "max_chars": 200},
        {"idx": 33, "name": "Text Placeholder 3a", "type": "BODY (2)", "max_chars": 200},
        {"idx": 34, "name": "Text Placeholder 47", "type": "BODY (2)", "max_chars": 200},
        {"idx": 35, "name": "Text Placeholder 3a", "type": "BODY (2)", "max_chars": 200},
        {"idx": 13, "name": "Picture Placeholder 18", "type": "PICTURE (18)", "max_chars": null}
      ]
    },
    {
      "id": 12,
      "name": "onepager_2",
      "description": "Alternative comprehensive layout",
      "placeholders": [
        {"idx": 0, "name": "Title 1", "type": "TITLE (1)", "max_chars": 60},
        {"idx": 26, "name": "Text Placeholder 3", "type": "BODY (2)", "max_chars": 200},
        {"idx": 22, "name": "Text Placeholder 3a", "type": "BODY (2)", "max_chars": 200},
        {"idx": 28, "name": "Text Placeholder 47", "type": "BODY (2)", "max_chars": 200},
        {"idx": 30, "name": "Text Placeholder 3a", "type": "BODY (2)", "max_chars": 200},
        {"idx": 31, "name": "Text Placeholder 47", "type": "BODY (2)", "max_chars": 200},
        {"idx": 33, "name": "Text Placeholder 3a", "type": "BODY (2)", "max_chars": 200},
        {"idx": 34, "name": "Text Placeholder 47", "type": "BODY (2)", "max_chars": 200},
        {"idx": 36, "name": "Text Placeholder 3a", "type": "BODY (2)", "max_chars": 200},
        {"idx": 37, "name": "Text Placeholder 47", "type": "BODY (2)", "max_chars": 200},
        {"idx": 16, "name": "image_placeholder", "type": "PICTURE (18)", "max_chars": null}
      ]
    }
  ]
}
```

## Output Requirements

Generate JSON with the EXACT same structure, but add "content" field to each text placeholder.

**Rules**:
1. Keep all fields: id, name, description, placeholders array, idx, name, type, max_chars
2. Add "content" field ONLY to non-PICTURE placeholders with topic-specific text
3. Respect max_chars limits
4. You MAY reorder layouts for narrative flow
5. ALL 13 layouts must be included

**Example**:
```json
{
  "layouts": [
    {
      "id": 0,
      "name": "cover",
      "description": "Title slide with branding",
      "placeholders": [
        {"idx": 0, "name": "title", "type": "TITLE (1)", "max_chars": 80, "content": "Your Topic Title Here"},
        {"idx": 1, "name": "subtitle", "type": "SUBTITLE (4)", "max_chars": 120, "content": "Compelling subtitle"}
        ... (all placeholders with content)
      ]
    }
    ... (all 13 layouts)
  ]
}
```

## Content Guidelines

- Use • for bullets, \n for line breaks
- Stay within max_chars limits
- Make content specific to topic
- Return ONLY valid JSON, no markdown blocks or explanations
