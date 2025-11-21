# Quick Start Guide

## 🎯 POC Components

Your presentation generator POC includes:

1. **`presentation_generator.py`** - Main CLI tool with GenAI integration
2. **`generate_prompt.py`** - Generates prompt.md from slide_layouts.json
3. **`test_generator.py`** - Demo version (no API key needed)
4. **`README.md`** - Full documentation

### 🔧 Utility Scripts (`./scripts/`)

- **`analyze_template.py`** - Analyzes PowerPoint template structure and lists all available layouts
- **`debug_placeholders.py`** - Debug tool that displays detailed placeholder information (idx, type, name) for each layout
- **`check_models.py`** - Checks available Gemini models and their configurations

## ✅ POC Requirements Met

✓ **CLI Interface** - Accepts topic as command-line argument  
✓ **GenAI Integration** - Uses OpenAI GPT-4 for content generation  
✓ **Branded Template** - Uses your `branding.pptx` with all layouts  
✓ **PPTX Output** - Generates complete PowerPoint presentations  

## 🚀 Quick Test (No API Key Required)

```bash
python3 test_generator.py
```

This creates `test_presentation.pptx` with a complete demo presentation about AI.

## 🔍 Analyzing Your Template

To understand your template structure:

```bash
# View all layouts and placeholders
python3 scripts/analyze_template.py

# Get detailed placeholder debugging info
python3 scripts/debug_placeholders.py

# Check available Gemini models
python3 scripts/check_models.py
```

## 🔑 Using with Real GenAI

### 1. Get Google Gemini API Key
Visit: https://makersuite.google.com/app/apikey

### 2. Set Environment Variable
```bash
export GEMINI_API_KEY='your-api-key-here'
```

### 3. Generate Presentation
```bash
python3 presentation_generator.py "Your Topic Here"
```

## 📋 Example Commands

```bash
# Generate about cybersecurity
python3 presentation_generator.py "Cybersecurity Best Practices"

# Generate about cloud computing with custom output
python3 presentation_generator.py "Cloud Computing" -o cloud.pptx

# Pass API key directly
python3 presentation_generator.py "Data Science" -k "sk-..."
```

## 📊 What Gets Generated

For any topic, the POC creates a complete presentation using ALL 13 available layouts:
- **Cover slide** (title, subtitle, presenter, date)
- **Agenda slide** (up to 9 agenda items)
- **Executive summary** (high-level overview)
- **Key message slides** (3 variations: with image, white background, dark background)
- **Content slides** (4 variations: with/without images, different layouts)
- **One-pager slides** (2 comprehensive summary layouts)
- **Salutation** (closing/thank you slide)

All content is dynamically generated based on your topic and uses your branded template's styling.

## 🎨 Available Template Layouts

All 13 layouts from `input/slide_layouts.json`:
- **Layout 0**: cover - Title slide with branding
- **Layout 1**: agenda_with_image - Agenda with up to 9 items
- **Layout 2**: executive_summary_with_one_image - High-level overview
- **Layout 3-5**: key_message variants - Impact statements (with image, white, dark)
- **Layout 6-9**: content variants - Information slides (4 different layouts)
- **Layout 10**: salutation - Closing slide
- **Layout 11-12**: onepager variants - Comprehensive summaries

## 📁 Files Generated

- `output/test_presentation.pptx` - Demo output (from test script)
- `output/<topic>.pptx` - GenAI output (from main script)
- `output/<topic>_response.json` - Raw AI response for debugging

## 🔧 Customization

### Modify Content Generation
Edit `input/prompt.md` to:
- Change content guidelines
- Adjust character limits
- Modify presentation structure
- Customize content style

### Update Template Structure
Edit `input/slide_layouts.json` to:
- Add new layouts
- Modify placeholder configurations
- Update character limits
- Change layout descriptions

### Regenerate Prompt
After modifying `slide_layouts.json`:
```bash
python3 generate_prompt.py
```
This updates `input/prompt.md` with the latest layout structure.

## 💡 Tips

1. Use descriptive topics: "The Impact of AI on Healthcare" vs "AI"
2. The more specific the topic, the better the content
3. GenAI generates 5-7 slides by default
4. All slides maintain your template branding

## 🎉 Success!

You now have a working POC that:
- Takes a topic as input ✓
- Uses GenAI to generate content ✓
- Applies your branded template ✓
- Outputs a professional PPTX file ✓
