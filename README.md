# Presentation Generator POC

A proof of concept that generates branded PowerPoint presentations from a topic using GenAI.

## Features

✅ **CLI Interface** - Simple command-line interface to accept topics  
✅ **GenAI Integration** - Uses Google Gemini 2.0 Flash to generate presentation outlines and content  
✅ **Branded Templates** - Uses the provided branding.pptx template with multiple layouts  
✅ **PPTX Output** - Produces professional PowerPoint presentations

## Requirements

- Python 3.9+
- Google Gemini API key

## Installation

1. Install dependencies:
```bash
pip install python-pptx google-generativeai
```

2. Set up your Google Gemini API key:
```bash
export GEMINI_API_KEY='your-api-key-here'
```

Get an API key at: https://aistudio.google.com/app/apikey

## Usage

### Basic Usage

```bash
python3 presentation_generator.py "Artificial Intelligence in Healthcare"
```

This will create a file named `generated_artificial_intelligence_in_healthcare.pptx`

### Custom Output Filename

```bash
python3 presentation_generator.py "Cloud Computing" -o my_presentation.pptx
```

### Custom Template

```bash
python3 presentation_generator.py "Data Science" -t custom_template.pptx
```

### Pass API Key as Argument

```bash
python3 presentation_generator.py "Machine Learning" -k "your-api-key"
```

## How It Works

1. **Input**: You provide a topic via CLI
2. **GenAI Call**: The tool calls Google Gemini 2.0 Flash to generate:
   - Presentation title and subtitle
   - Structured outline with 5-7 slides
   - Content for each slide
3. **Template Application**: Uses the branded template's layouts:
   - Cover slide
   - Agenda slide
   - Content slides
   - Key message slides
   - Closing slide
4. **Output**: Generates a complete PPTX file

## Template Structure

The tool uses these layouts from `branding.pptx`:

- Layout 0: **cover** - Title slide
- Layout 4: **key_message_02_white_background** - Key messages
- Layout 7: **content_02_no_image** - Content and agenda slides
- Layout 10: **salutation** - Thank you slide

## Examples

```bash
# Generate a presentation about AI
python3 presentation_generator.py "The Future of Artificial Intelligence"

# Generate a presentation about sustainability
python3 presentation_generator.py "Sustainable Business Practices"

# Generate a presentation about cybersecurity
python3 presentation_generator.py "Cybersecurity Best Practices for 2025"
```

## Output

The generated presentation includes:
- Professional cover slide with title and subtitle
- Agenda slide listing key topics
- Multiple content slides with detailed information
- Key message slides for emphasis
- Thank you/closing slide

All slides maintain the branding, colors, and style from the template.

## Troubleshooting

**Error: Gemini API key not provided**
- Set the environment variable: `export GEMINI_API_KEY='your-key'`
- Or pass it as an argument: `-k 'your-key'`

**Error: Template file not found**
- Make sure `branding.pptx` is in the same directory
- Or specify the path: `-t /path/to/template.pptx`

## Development

### Analyze Template Structure

```bash
python3 analyze_template.py
```

This shows all available layouts and placeholders in the template.

## Future Enhancements

- Support for images and charts
- Multiple GenAI provider options (Anthropic, Google, etc.)
- Web UI interface
- Custom styling options
- Export to other formats (HTML slides, PDF)
