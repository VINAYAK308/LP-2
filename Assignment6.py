def diagnose(symptoms):
    # Normalize input
    symptoms = [s.strip().lower() for s in symptoms]

    # Rule-based diagnosis
    if "fever" in symptoms and "cough" in symptoms:
        return {
            "disease": "Flu",
            "doctor": "General Physician",
            "advice": "Take rest, drink fluids, and take paracetamol."
        }

    elif {"fever", "headache", "body pain"}.issubset(symptoms):
        return {
            "disease": "Dengue",
            "doctor": "Physician",
            "advice": "Get a blood test done immediately and stay hydrated."
        }

    elif "chest pain" in symptoms:
        return {
            "disease": "Possible Heart Problem",
            "doctor": "Cardiologist",
            "advice": "Seek immediate medical attention."
        }

    elif {"stomach pain", "vomiting"}.issubset(symptoms):
        return {
            "disease": "Food Poisoning",
            "doctor": "Gastroenterologist",
            "advice": "Drink ORS and avoid outside food."
        }

    elif "rash" in symptoms:
        return {
            "disease": "Allergy",
            "doctor": "Dermatologist",
            "advice": "Avoid allergens and take antihistamines."
        }

    elif "fever" in symptoms and "sore throat" in symptoms:
        return {
            "disease": "Viral Infection",
            "doctor": "General Physician",
            "advice": "Rest well, drink warm fluids, and monitor symptoms."
        }

    else:
        return {
            "disease": "Unknown",
            "doctor": "General Physician",
            "advice": "Please consult a doctor for proper diagnosis."
        }


def start_system():
    print("===================================")
    print("     Hospital Expert System ")
    print("===================================")
    print("Enter symptoms separated by comma")
    print("Example: fever, cough\n")

    user_input = input("Symptoms: ")

    # Handle empty input
    if not user_input.strip():
        print("\n Note: Please enter at least one symptom.")
        return

    symptoms = user_input.split(",")

    result = diagnose(symptoms)

    print("\n--- Diagnosis Result ---")
    print(f"Possible Disease      : {result['disease']}")
    print(f"Recommended Doctor    : {result['doctor']}")
    print(f"Advice                : {result['advice']}")

    print("\n Note: This is a basic expert system and not a medical diagnosis.")


if __name__ == "__main__":
    start_system()

# Symptoms: fever, cough

# --- Diagnosis Result ---
# Possible Disease      : Flu
# Recommended Doctor    : General Physician
# Advice                : Take rest, drink fluids, and take paracetamol.

#  Note: This is a basic expert system and not a medical diagnosis.

# Symptoms: fever, headache, body pain

# --- Diagnosis Result ---
# Possible Disease      : Dengue
# Recommended Doctor    : Physician
# Advice                : Get a blood test done immediately and stay hydrated.

#  Note: This is a basic expert system and not a medical diagnosis.


# Symptoms: chest pain

# --- Diagnosis Result ---
# Possible Disease      : Possible Heart Problem
# Recommended Doctor    : Cardiologist
# Advice                : Seek immediate medical attention.

#  Note: This is a basic expert system and not a medical diagnosis.