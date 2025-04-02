# Improved Zero-Shot Prompt Template with Decision Framework
improved_zero_shot_template = """You are a world-class investigative journalist and fact-checker with expertise in detecting misinformation.

To determine if news is REAL or FAKE, follow this systematic approach:

STEP 1: Examine the title characteristics
- Sensationalist language or excessive punctuation suggests FAKE
- Neutral, precise language suggests REAL
- Headlines with ALL CAPS or excessive capitalization often signal FAKE news
- Question-based headlines often indicate FAKE news fishing for attention

STEP 2: Evaluate claim plausibility
- Extraordinary or implausible claims without evidence suggest FAKE
- Reasonable claims consistent with known facts suggest REAL
- Claims about celebrities' personal actions/feelings without quotes often indicate FAKE

STEP 3: Analyze specificity and attribution
- Vague assertions or unattributed claims suggest FAKE
- Specific details, named sources, and verifiable facts suggest REAL
- Headlines reporting established events or announcements are typically REAL

Now analyze this news item:
{news_data}

Based on this analysis framework, classify this as "REAL" or "FAKE".
Respond with only "REAL" or "FAKE" without any additional explanation."""


# Improved Few-Shot Template with Selected High-Quality Examples from Dataset
improved_few_shot_template = """You are a world-class investigative journalist and fact-checker with expertise in detecting misinformation.

When analyzing news articles, pay attention to these key patterns:

PATTERN 1: Sensationalist vs. Neutral Language
- Emotional language, excessive punctuation, and ALL CAPS often indicate FAKE news
- Measured, neutral language often indicates REAL news

PATTERN 2: Specificity vs. Vagueness
- Specific details, named sources, and verifiable events suggest REAL news
- Vague assertions, unnamed sources, and generalized claims suggest FAKE news

PATTERN 3: Question Headlines vs. Statement Headlines
- Headlines phrased as questions often indicate FAKE news
- Headlines making direct statements often indicate REAL news

Here are examples from real news analysis:

EXAMPLE 1:
Title: Erin Napier Delivers a Beautiful Baby Helen
Features:
- Capitalization: Normal (14.0% uppercase)
- Punctuation: Neutral
- Language tone: Neutral
Classification: REAL
Reasoning: The title reports a specific event with named individuals in a straightforward manner without sensationalism, using neutral language and tone typical of factual reporting.

EXAMPLE 2:
Title: 'The Voice' Season 13 Winner: Chloe Kohanski
Features:
- Capitalization: Normal (13.6% uppercase)
- Punctuation: Neutral
- Language tone: Neutral
Classification: REAL
Reasoning: The headline reports a verifiable entertainment industry outcome with specific details (season number and winner's name) in a direct, factual manner without embellishment.

EXAMPLE 3:
Title: BOMBSHELL: COMEY KNEW MURDERED DNC STAFFER, SETH RICH, WAS WIKILEAKS SOURCE & COVERED IT UP FOR HILLARY
Features:
- Capitalization: Excessive (80.6% uppercase)
- Punctuation: Neutral
- Language tone: Emotional (contains sensational term "BOMBSHELL")
Classification: FAKE
Reasoning: The excessive capitalization is a red flag, along with the sensationalist "BOMBSHELL" term. The title makes an extraordinary conspiracy claim without evidence, using emotionally manipulative framing.

EXAMPLE 4:
Title: Is Jared Leto, 45, Crushing On 19-Year-old Paris Jackson?
Features:
- Capitalization: Normal
- Punctuation: Neutral
- Language tone: Neutral
- Format: Question headline
Classification: FAKE
Reasoning: The question headline format is designed to create speculation without providing evidence. The claim involves celebrities' personal feelings, which the writer would have no way to verify without direct sources.

EXAMPLE 5:
Title: Katie Holmes And Jamie Foxx Update: Is He Adopting Her Daughter, Suri Cruise?
Features:
- Capitalization: Normal
- Punctuation: Neutral
- Language tone: Neutral
- Format: Question headline
Classification: FAKE
Reasoning: The question format allows the writer to make a sensational implication without evidence. The headline involves celebrities' private family matters, which would require insider knowledge to report factually.

EXAMPLE 6:
Title: Jeffrey Tambor May Be Leaving 'Transparent' Amid Sexual Harassment Allegations
Features:
- Capitalization: Normal (12.8% uppercase)
- Punctuation: Neutral
- Language tone: Neutral
Classification: REAL
Reasoning: The headline reports on a developing news story using measured language with appropriate qualifiers ("may be"), referring to publicly known allegations and a potential consequence, without sensationalism.

EXAMPLE 7:
Title: Jennifer Lopez wants boyfriend Alex Rodriguez to fire beautiful female staff
Features:
- Capitalization: Normal
- Punctuation: Neutral
- Language tone: Neutral
Classification: FAKE
Reasoning: The headline makes claims about a celebrity's private wishes and intentions without attribution or evidence. It presents speculation about personal relationships as fact, which is a common pattern in celebrity gossip misinformation.

EXAMPLE 8:
Title: Figure skater Adam Rippon wants to 'reinvent,' pursue acting
Features:
- Capitalization: Normal
- Punctuation: Neutral
- Language tone: Neutral
Classification: REAL
Reasoning: The headline reports on a public figure's stated career intentions, likely from an interview or public statement, using neutral language and direct attribution without sensationalism.

Now analyze this news item:
{news_data}

Based on the patterns and examples above, classify this as "REAL" or "FAKE".
Respond with only "REAL" or "FAKE" without any additional explanation."""