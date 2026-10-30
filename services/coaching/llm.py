from services.config_services.state.workout_config import PROMPT


class LLMCoach:
    def __init__(self, groq_client):
        self.client = groq_client
        self.history = []
        self.system_prompt = PROMPT

    def give_feedback(self, event, issue):
        try:
            prompt = f"Event: {event}"

            if issue:
                prompt += f" Form Issue: {issue}"

            messages = [
                {"role": "system", "content": self.system_prompt},
                *self.history[-10:],
                {"role": "user", "content": prompt}
            ]

            # print(f"Calling Groq: {event}")

            response = self.client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=messages,
                temperature=0.4,
            )

            text = response.choices[0].message.content

            if not text:
                # print("ERROR: Groq returned empty content")
                return None

            text = text.strip()

            self.history.append({
                "role": "assistant",
                "content": text
            })

            # print("LLM RESULT:", text)
            return text

        except Exception as e:
            print(f"GROQ API ERROR: {type(e).__name__}: {e}")
            return None

    
    