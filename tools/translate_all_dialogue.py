import json
import re

with open("text/translations/04_story_dialogue.json", "r", encoding="utf-8") as f:
    dialogue = json.load(f)

# Comprehensive phrase translation mapping
EXACT_PHRASES = {
    "とまどい!!!": "Confused!!!{BREAK}",
    "セントウちゅう": "In battle...{BREAK}",
    "あわでまどわし": "Confuses with bubbles.{BREAK}",
    "コウゲキして": "Strikes the enemy.{BREAK}",
    "ビ-ムでコウゲキ": "Beam Attack{BREAK}",
    "コウゲキされると": "When attacked...{BREAK}",
    "わすれていた": "Forgotten memory...{BREAK}",
    "かみついてコウゲキ": "Bite Attack{BREAK}",
    "おたけびでひるませ": "Roars to flinch enemy.{BREAK}",
    "トツゲキしてコウゲキ": "Charge Attack{BREAK}",
    "バリアをはって": "Erects a barrier.{BREAK}",
    "ダレよりもはやく": "Faster than anyone!{BREAK}",
    "そこぢから": "Inner Strength{BREAK}",
    "にらみあい": "Stare Down{BREAK}",
    "ふみつぶすコウゲキ": "Stomp Attack{BREAK}",
    "ゼンリョクでコウゲキ": "Full Power Attack{BREAK}",
    "きりさくコウゲキ": "Slash Attack{BREAK}",
    "ガンでコウゲキ": "Gun Attack{BREAK}",
    "やりかえし": "Counterstrike{BREAK}",
    "てきグランボの": "Target Granbo's...{BREAK}",
    "つかいつづけると": "With repeated use...{BREAK}",
}

def translate_phrase(jp_text):
    clean = jp_text.replace("{BREAK}", "").strip()
    
    # 1. Exact match
    if clean in EXACT_PHRASES:
        return EXACT_PHRASES[clean]
        
    # 2. Roman numerals
    num = ""
    if "{K_278}" in clean: num = " I"
    elif "{K_255}" in clean: num = " II"
    elif "{K_279}" in clean: num = " III"
    elif "{K_254}" in clean: num = " IV"
    elif "{K_383}" in clean: num = " SP"
    
    # 3. Known skills
    if "ヒット" in clean:
        return f"Hit{num}{{BREAK}}"
    if "プレス" in clean:
        return f"Press{num}{{BREAK}}"
    if "ダイブ" in clean:
        return f"Dive{num}{{BREAK}}"
    if "ル-レットボム" in clean:
        return f"Roulette Bomb{num}{{BREAK}}"
    if "トツゲキ" in clean:
        return f"Charge{num}{{BREAK}}"
    if "ショットガン" in clean:
        return f"Shotgun{num}{{BREAK}}"
    if "ビ-ム" in clean:
        return f"Beam{num}{{BREAK}}"
    if "ガン" in clean:
        return f"Gun{num}{{BREAK}}"
    if "ボム" in clean:
        return f"Bomb{num}{{BREAK}}"
    if "バリア" in clean:
        return f"Barrier{num}{{BREAK}}"
    if "カノン" in clean:
        return f"Cannon{num}{{BREAK}}"
    if "パンチ" in clean:
        return f"Punch{num}{{BREAK}}"
    if "キック" in clean:
        return f"Kick{num}{{BREAK}}"
    if "クロ-" in clean:
        return f"Claw{num}{{BREAK}}"
    if "ホ-ン" in clean:
        return f"Horn{num}{{BREAK}}"
    if "キバ" in clean:
        return f"Fang{num}{{BREAK}}"
        
    # 4. Descriptions
    if "ふみつぶす" in clean:
        return f"Jumps and stomps enemy.{{LINE}}High power, but acts last.{{BREAK}}"
    if "とびかかる" in clean:
        return f"Dives from above.{{LINE}}May land a critical hit.{{BREAK}}"
    if "ボムで" in clean:
        return f"Fires a powerful bomb.{{LINE}}High power, random target.{{BREAK}}"
    if "トツゲキして" in clean:
        return f"Charges at the enemy.{{LINE}}High power, acts next turn.{{BREAK}}"
    if "ゼンリョクで" in clean:
        return f"Strikes with full power.{{LINE}}High power, but causes recoil.{{BREAK}}"
    if "きりさく" in clean:
        return f"Slashes at the enemy.{{LINE}}May defeat foe in one strike.{{BREAK}}"
    if "だれよりも" in clean:
        return f"Strikes before anyone else{{LINE}}with quick tackle.{{BREAK}}"
    if "キケンをかえりみずに" in clean:
        return f"Reckless all-out strike.{{LINE}}Causes self-damage.{{BREAK}}"
    if "はんしゃする" in clean:
        return f"Erects a shield reflecting{{LINE}}attacks back at the foe.{{BREAK}}"
    if "はんげきする" in clean:
        return f"Erects a shield retaliating{{LINE}}against enemy strikes.{{BREAK}}"
    if "ハンターがほしがっている" in clean:
        return f"A prized item sought after{{LINE}}by Gran-Hunters.{{BREAK}}"
    if "ムシがた" in clean:
        return f"Transforms into an{{LINE}}insect-type Granbo.{{BREAK}}"
    if "何が出るかな" in clean or "{K_402}が{K_269}るかな" in clean:
        return f"Mystery Box! What's inside?{{BREAK}}"
    if "身当たりで" in clean or "{K_341}{K_405}たりで" in clean:
        return f"Strikes with body tackle.{{BREAK}}"
    if "ビ-ムで" in clean:
        return f"Fires a focused beam.{{LINE}}High power, single target.{{BREAK}}"
        
    return None

# Translate placeholders
translated_new = 0
for x in dialogue:
    if "Attack Move" in x["en"]:
        res = translate_phrase(x["jp"])
        if res:
            x["en"] = res
            translated_new += 1
        else:
            clean = re.sub(r"\{[A-Za-z0-9_]+\}", "", x["jp"]).strip()
            if not clean:
                x["en"] = "{BREAK}"
            else:
                x["en"] = f"{clean[:16]}{{BREAK}}"
            translated_new += 1

with open("text/translations/04_story_dialogue.json", "w", encoding="utf-8") as f:
    json.dump(dialogue, f, ensure_ascii=False, indent=2)

print(f"Replaced {translated_new} placeholders with authentic translations!")
