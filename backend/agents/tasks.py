from crewai import Task

def created_draft_task(agent, project_name,raw_notes):
    return Task (
        description=(
            f"Analyze the raw notes for the project named '{project_name}'. "
            f"Identify the main purpose, prerequisites, installation steps, and usage commands.\n\n"
            f"User's Raw Notes:\n{raw_notes}\n\n"
            f"Create a clean, structured documentation draft containing these core headers."

         ),
        expected_output="A clean markdown draft containing accurate technical sections with zero emojis or badges.",
         verbose=False,
        agent=agent
        
    )


def create_polish_task(agent):
    return Task(
        description=(
            "Review the technical draft generated in the previous step. Without changing any technical commands, "
            "restructure the document for maximum visual appeal on GitHub. Add relevant emojis to main section "
            "headers, format code blocks cleanly, and convert listed tech-stacks into high-quality visual badges "
            "using shields.io markup syntax."
        ),
        expected_output="A perfectly formatted final Markdown string ready to be used as a GitHub README.",
         verbose=False,
        agent=agent
        
    )


def create_optimization_task(agent):
    return Task(
        description=(
            "Review the visually polished markdown from the previous designer step. Without removing any badges, "
            "formatting, or code setups, append a professional section named '🎯 Project Impact & Highlights'. "
            "In this section, frame the project's technical achievements in a way that appeals to technical recruiters. "
            "At the very bottom of the file, add a separate '🏷️ Repository Metadata' snippet containing a suggested "
            "1-sentence GitHub description and a list of 5 searchable repository topics/tags."
        ),
        expected_output="The complete final Markdown README with an appended professional impact section and repository metadata tags.",
        verbose=False,
        agent=agent
    )

def create_qa_task(agent):
    return Task(
        description=(
            "Thoroughly inspect the complete, optimized Markdown file produced by the previous step. "
            "Scan for any typos, missing Markdown formatting tags, unclosed bold markings (**), or split code fences. "
            "Fix any structural defects immediately without altering the project's technical content, badges, or portfolio highlights. "
            "CRITICAL: Do not wrap your final output in any markdown code blocks or backticks (```). Output the clean text directly."
        ),
        expected_output="A perfectly clean, flawless, raw Markdown string with guaranteed correct formatting syntax.",
        verbose=False,
        agent=agent
    )