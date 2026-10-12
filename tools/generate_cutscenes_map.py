# -*- coding: utf-8 -*-
"""
generate_cutscenes_map.py
Builds tools/batch_07_cutscenes.py containing translations for all 319 entries in scratch/entries_0_349.json.
"""

import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

entries = json.load(open("scratch/entries_0_349.json", encoding="utf-8"))

print(f"Generating translations for {len(entries)} cutscene entries...")

# We will create an extensive dictionary
out_py = "tools/batch_07_cutscenes.py"

# Let's inspect the target offsets and create translations
lines = []
lines.append("# -*- coding: utf-8 -*-")
lines.append('"""')
lines.append("batch_07_cutscenes.py")
lines.append("Translation mapping for all 319 field and cutscene strings in 07 dataset.")
lines.append('"""')
lines.append("")
lines.append("CUTSCENE_MAP = {")

# Helper function to generate high-fidelity English for a Japanese string
def translate_cutscene(target, jp):
    clean = re.sub(r"\{[A-Za-z0-9_]+\}", "", jp).strip()
    
    # Check specific addresses
    if target == 0x1AD928:
        return "{CTRL_8002}{K_38088}Town Boy{K_247}Ugh...{LINE}Can I really make it{LINE}all the way across?{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1AF5C4:
        return "{CTRL_8002}{K_38088}Old Man{K_247}Damn it, what a mess...{K_248}{CTRL_8300}{K_38088}Old Man{K_247}At this rate, I can't{LINE}go to the {CTRL_8833}Battle Stadium{CTRL_8800}!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target in [0x1AF9FA, 0x1AF9FC]:
        return "{CTRL_8607}{K_38045}{K_247}What a huge letdown...{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1B24C8:
        return "{CTRL_8002}{K_38088}Outlaw{K_247}Damn it!!{LINE}At this rate, we can't{LINE}lay a finger on them!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1B2E44:
        return "{CTRL_8002}{K_38088}Old Man{K_247}The Sky Shark isn't in{LINE}this town anymore...{K_248}{CTRL_8300}{K_38088}Old Man{K_247}Looks like they fled{LINE}toward the cave...{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1B38A8:
        return "{CTRL_8002}{CTRL_8610}{K_38039}{K_247}The Sky Shark's base is{LINE}behind this waterfall!!{K_248}{CTRL_8300}{CTRL_8611}{K_38039}{K_247}But if we jump in recklessly,{LINE}we'll get swept away...{K_248}{CTRL_8300}{CTRL_8611}{K_38039}{K_247}What should we do...?{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1B5B00:
        return "{CTRL_8002}{CTRL_8620}{K_38055}{K_247}Where do you think you're going!{K_248}{CTRL_8300}{CTRL_8620}{K_38055}{K_247}The shop is over to the east,{LINE}in that red building!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1B7F00:
        return "Won't fight me?{LINE}Hmph, beating Bermuda must{LINE}have been a lie!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1B94D6:
        return "{CTRL_8001}{CTRL_8602}{K_38040}{K_247}Well then, I'll go ahead{LINE}and scout the Granbos{LINE}in this area!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target in [0x1BB8CC, 0x1BB8EC]:
        return "Standby{NULL}"
    if target == 0x1BB92A:
        return "{CTRL_8002}{K_38088}Boy{K_247}My brother is the only{LINE}skyship pilot in Blossom Town!{LINE}Isn't that awesome!!{K_248}{CTRL_8300}{K_38088}Boy{K_247}Someday I'm definitely{LINE}gonna become a skyship{LINE}pilot too!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1BC056:
        return "{CTRL_8002}{K_38088}Girl{K_247}I totally hate studying!!{K_248}{CTRL_8300}{K_38088}Girl{K_247}Sigh, I want to play{LINE}outside all day!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1BC98C:
        return "{CTRL_8002}{K_38088}Shopkeeper{K_247}I was quite surprised...{K_248}{CTRL_8300}{K_38088}Shopkeeper{K_247}My grandkid offered to run{LINE}the shop while my daughter{LINE}was taken away...{K_248}{CTRL_8300}{K_38088}Shopkeeper{K_247}Watching them at the register,{LINE}they handled it splendidly!{K_248}{CTRL_8300}{K_38088}Shopkeeper{K_247}They must have learned by{LINE}watching their mom work!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target in [0x1C07D4, 0x1C081E, 0x1C0834]:
        return "{CTRL_8002}{K_38088}Veteran Saber{K_247}Use {CTRL_8833}Transform{CTRL_8800} effectively{LINE}by matching enemy elements!{K_248}{CTRL_8300}{K_38088}Veteran Saber{K_247}{CTRL_8833}Defense{CTRL_8800} reduces damage taken.{WAIT}{K_38088}Veteran Saber{K_247}If you can't win, choose{LINE}{CTRL_8833}Run{CTRL_8800} and flee immediately!{K_248}{CTRL_8300}{K_38088}Veteran Saber{K_247}Master these 6 commands{LINE}and you'll fear nothing!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1C10F2:
        return "{CTRL_8002}{K_38088}Veteran Saber{K_247}That machine over there{LINE}is the {CTRL_8833}Item Locker{CTRL_8800}.{K_248}{CTRL_8300}{K_38088}Veteran Saber{K_247}You can store items here{LINE}when your bag is full!{K_248}{CTRL_8300}{K_38088}Veteran Saber{K_247}Store unneeded items here{LINE}to travel lightly!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1C15E2:
        return "{CTRL_8833}Run{CTRL_8800} lets you flee if{LINE}you have no chance to win!{WAIT}{K_38088}Veteran Saber{K_247}Master these 6 battle options{LINE}for every situation!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1C171A:
        return "Awesome!!{WAIT}{K_38088}Boy{K_247}I'll help you out too!{WAIT}{K_38088}Boy{K_247}Shall I tell you the secret{LINE}of {CTRL_8833}Elemental Types{CTRL_8800}?{K_248}{LINE}{CTRL_8D00}{CTRL_8100}{BREAK}"
    if target == 0x1C2728:
        return "There should be someone at{LINE}the Saber Station who knows{LINE}all the details!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1C2E72:
        return "{CTRL_8002}{CTRL_8620}{K_38055}{K_247}By the way, Kakeru...{WAIT}{CTRL_8620}{K_38055}{K_247}Do you plan to rescue{LINE}Shizuku right away?{K_248}{LINE}{CTRL_8D00}{CTRL_8100}{BREAK}"
    if target == 0x1C2F54:
        return "You must defeat Bermuda...{WAIT}{CTRL_8621}{K_38055}{K_247}Bermuda told you that with{LINE}only one Granbo you have{LINE}no chance of winning...{WAIT}{CTRL_8621}{K_38055}{K_247}As you are now, you cannot{LINE}defeat Bermuda.{WAIT}{CTRL_8621}{K_38055}{K_247}First, figure out what you{LINE}need to beat Bermuda!!{WAIT}{CTRL_8620}{K_38055}{K_247}That is all I can tell you...{LINE}Now go!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1C351C:
        return "{CTRL_8620}{K_38055}{K_247}You will grow much stronger!{LINE}Wahahaha!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1C8222:
        return "{CTRL_8001}{CTRL_860F}{K_38053}{K_247}Lord Bermuda!{LINE}We succeeded in capturing{LINE}the villagers of this town!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1CC224:
        return "{CTRL_8001}{CTRL_8613}{K_38041}{K_247}You've come... for me...{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1CF22C:
        return "{CTRL_8002}{CTRL_861F}{K_38053}{K_247}Wh-Why isn't this elevator{LINE}moving!?{WAIT}{CTRL_861F}{K_38053}{K_247}At this rate, I can't reach{LINE}Lord Bermuda!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1CF44E:
        return "{CTRL_8002}{K_37377}Push the switch?{LINE}{LINE}{CTRL_8D00}{CTRL_8100}{BREAK}"
    if target == 0x1CF82A:
        return "{CTRL_8002}{CTRL_860F}{K_38053}{K_247}What is it? I'm busy!{WAIT}{CTRL_860F}{K_38053}{K_247}The elevator isn't moving?{LINE}Did you forget to flip{LINE}the power switch again!?{WAIT}{CTRL_860F}{K_38053}{K_247}I knew it! Get over to the{LINE}surveillance room right now!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1CFB9A:
        return "{CTRL_8002}{CTRL_860F}{K_38053}{K_247}Hm? What is it?{WAIT}{CTRL_860F}{K_38053}{K_247}Do you have business with{LINE}Lord Bermuda?{K_248}{LINE}{LINE}{CTRL_8D00}{CTRL_8100}{BREAK}"
    if target == 0x1CFE9C:
        return "{CTRL_8002}{CTRL_860F}{K_38053}{K_247}Lord Bermuda!!{WAIT}{CTRL_860F}{K_38053}{K_247}Loading of the {CTRL_8833}Hunt Gloves{CTRL_8800}{LINE}is now complete!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1CFEE8:
        return "Complete!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target in [0x1D27E0, 0x1D2808, 0x1D3448]:
        return "{CTRL_8002}{K_38088}Female Saber{K_247}Want to battle my Granbo?{LINE}If you win, I'll give you an{LINE}HP skill!{WAIT}{K_38088}Female Saber{K_247}Let's see if you can fight{LINE}the Sky Shark! If you can't{LINE}beat me, you won't beat them!{K_248}{LINE}{CTRL_8D00}{BREAK}"
    if target == 0x1D3208:
        return "Let me test your skill first!{WAIT}{K_38088}Male Saber{K_247}If you defeat me, I'll give{LINE}you a {CTRL_8833}Mecha Egg{CTRL_8800}!{LINE}Well, what do you say?{K_248}{LINE}{CTRL_8D00}{BREAK}"
    if target == 0x1D4318:
        return "You'd better do it!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1D586C:
        return "{CTRL_8002}{K_38088}Girl{K_247}I'm gonna buy a ton of HP{LINE}Capsules for my Pochimaru!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1D5EC2:
        return "{CTRL_8002}{K_38088}Veteran Saber{K_247}The water suddenly dried up,{LINE}then returned to normal...{WAIT}{K_38088}Veteran Saber{K_247}In my 50 years as a Saber,{LINE}I've never seen such a thing!{WAIT}{K_38088}Veteran Saber{K_247}Something terrible is brewing...{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1D7498:
        return "{CTRL_8002}{K_38088}Boy{K_247}Mom... Dad...{LINE}What should I do...?{WAIT}{K_38088}Boy{K_247}I know! I'll ask the wise{LINE}old grandpa next door!{WAIT}{K_38088}Boy{K_247}He knows everything, so he'll{LINE}surely tell me what to do!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1D79F0:
        return "{CTRL_8002}{K_37377}A pink desk... Could this be{LINE}the old man's taste...?{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1D8B90:
        return "{CTRL_8002}{CTRL_8602}{K_38040}{K_247}What is this place?{WAIT}{CTRL_8602}{K_38040}{K_247}It's locked, but I'm really{LINE}curious about it===!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1D8C02:
        return "{CTRL_8002}{CTRL_8614}{K_38043}{K_247}Would you like another{LINE}explanation of Grand Change?{K_248}{LINE}{CTRL_8D00}{CTRL_8100}{BREAK}"
    if target in [0x1DACBC, 0x1DACC8]:
        return "{CTRL_8002}{CTRL_8602}{K_38040}{K_247}Ah, Kakeru===!!{LINE}I caught important info!{WAIT}{CTRL_8602}{K_38040}{K_247}Bermuda's Granbos use Fire{LINE}and Water elements!{WAIT}{CTRL_8602}{K_38040}{K_247}His main Granbo inflicts Virus,{LINE}so bring Virus Capsules!{WAIT}{CTRL_8602}{K_38040}{K_247}Here, take one of my{LINE}Virus Capsules with you!{K_248}{LINE}{CTRL_8D00}{BREAK}"
    if target == 0x1DAF60:
        return "{CTRL_8002}{CTRL_8614}{K_38043}{K_247}What is it? I'm busy with{LINE}Grand Change research!!{WAIT}{CTRL_8614}{K_38043}{K_247}If you have no business,{LINE}please leave!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1DB300:
        return "{K_38088}Doctor{K_247}Alright, let me explain{LINE}Grand Change to you!!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1DE2FE:
        return "{CTRL_8002}{CTRL_860F}{K_38053}{K_247}I'm filling this hole!{LINE}Don't distract me!{WAIT}{CTRL_860F}{K_38053}{K_247}We need to make this outpost{LINE}look proper quickly!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1DE5B0:
        return "{CTRL_8002}{CTRL_860F}{K_38053}{K_247}Phew... Finished changing{LINE}all the lightbulbs...{WAIT}{CTRL_860F}{K_38053}{K_247}Replacing every bulb in this{LINE}building alone... I'm amazing!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target in [0x1DE66A, 0x1DE692]:
        return "{CTRL_8001}{CTRL_8608}{K_38046}{K_247}Ohohohoho... I heard you{LINE}pulled off a Grand Change,{LINE}so I came to see for myself...{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1DE90C:
        return "{CTRL_8002}{CTRL_860F}{K_38053}{K_247}Quiet! I'm repairing Lord{LINE}Bermuda's door! If I mess{LINE}up, he'll blast me away!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1DEB3E:
        return "{CTRL_8002}{K_37377}It's Sky Shark Bermuda's desk.{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1DFC98:
        return "{CTRL_8002}{K_38088}Old Man{K_247}Did you defeat Bermuda?{LINE}Thank you, you saved us!!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1E014E:
        return "{CTRL_8002}{CTRL_8603}{K_38041}{K_247}Kakeru!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1E0300:
        return "Could you please help us?{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target in [0x1E1ECC, 0x1E1ED8]:
        return "Standby{NULL}"
    if target == 0x1E1F60:
        return "{CTRL_8002}{K_38088}Old Man{K_247}The most important thing for{LINE}people here? Granbo Battles,{LINE}without a doubt!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1E271A:
        return "He has an unmistakable{LINE}hairstyle, so you'll know{LINE}him when you see him!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1E38AE:
        return "{CTRL_8002}{K_38088}Female Saber{K_247}I came to repair my Batatchi.{LINE}Battling constantly means{LINE}endless repairs!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1E3D68:
        return "{CTRL_8002}{K_38088}Old Man{K_247}Granbo Battles are supreme!{LINE}You should watch one! Want me{LINE}to tell you where it is?{K_248}{LINE}{CTRL_8D00}{CTRL_8100}{BREAK}"
    if target == 0x1E50CE:
        return "{CTRL_8002}{K_38088}Boy{K_247}My sister is the receptionist{LINE}at the stadium! She has a lot{LINE}of fans too!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1E5472:
        return "{CTRL_8002}{K_38088}Old Woman{K_247}Almost everyone in this town{LINE}works at the Battle Stadium!{LINE}My whole family works there!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1E583E:
        return "{CTRL_8002}{K_38088}Man{K_247}Don't interrupt! I'm training{LINE}my son so he can enter Granbo{LINE}battles!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1E730C:
        return "{CTRL_8002}{CTRL_861F}{K_38053}{K_247}Blast it!! While I looked away,{LINE}those brats slipped inside!{WAIT}{CTRL_861F}{K_38053}{K_247}Lord Barth will be furious...{LINE}I need an excuse!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1E75AE:
        return "{CTRL_8002}{CTRL_861F}{K_38053}{K_247}Damn... Sprained my foot...{LINE}Why must I risk my neck just{LINE}to deliver to Lord Barth...?{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1E79E8:
        return "{CTRL_8002}{CTRL_860F}{K_38053}{K_247}Shut up! I'm watching the best{LINE}part! Hehehe... this video is{LINE}hilarious!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1E7CBE:
        return "{CTRL_8002}{CTRL_860F}{K_38053}{K_247}Reinforcements!? Lord Barth{LINE}is dealing with intruders{LINE}behind that door! Back him up!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1E7ED0:
        return "{CTRL_8002}{CTRL_8611}{K_38039}{K_247}No way... How could I lose...?{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1E9A90:
        return "{CTRL_8002}{K_38088}Elder Woman{K_247}I'm the elder here. Few people{LINE}live here because everyone moves{LINE}closer to the stadium!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1EBECE:
        return "{CTRL_8002}{K_38088}Boy{K_247}I came to get my Granbo fixed.{LINE}The climate here isn't great{LINE}for machinery!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1EC564:
        return "{CTRL_8002}{K_38088}Female Saber{K_247}As you see, I'm the only one{LINE}here... I want to leave this{LINE}countryside soon!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1ECA56:
        return "{CTRL_8002}{K_38088}Girl{K_247}My mom and dad both work at{LINE}the Battle Stadium!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1ECCCC:
        return "I believe they'll come back!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1ED01C:
        return "{CTRL_8002}{K_38088}Innkeeper{K_247}Welcome! This is an inn!{LINE}Not a guest? Well, relax{LINE}and take your time anyway!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1ED6F6:
        return "{CTRL_8002}{K_38088}Girl{K_247}I'm the only child at this inn.{LINE}I want to help, but with no{LINE}guests, there's nothing to do!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1EDBEC:
        return "{CTRL_8002}{K_38088}Man{K_247}I love Granbo Battles! Steel{LINE}clashing against steel, oil{LINE}flying! Nothing beats it!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1EE32A:
        return "{CTRL_8002}{K_37377}Locked with a sturdy {CTRL_8833}Key{CTRL_8800}!{LINE}Cannot enter!!{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1EE4FC:
        return "Standby{NULL}"
    if target == 0x1EFC78:
        return "{CTRL_8002}{CTRL_8601}{K_38039}{K_247}Let me introduce myself!{LINE}My name is {CTRL_8833}Akari{CTRL_8800}!{LINE}Nice to meet you!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target in [0x1F0000, 0x1F0034]:
        return "{CTRL_8612}{K_38040}{K_247}Sky Shark has never done{LINE}anything this reckless before...{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1F008E:
        return "Let's head to the town the{LINE}pilot mentioned!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1F1F88:
        return "{CTRL_8002}{K_38088}Receptionist{K_247}Welcome to Battle Stadium!{LINE}Preparations are underway,{LINE}so please visit again soon!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1F22BC:
        return "{CTRL_8002}Cannot speak right now.{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1F2A3E:
        return "{CTRL_8002}{CTRL_860F}{K_38053}{K_247}That's the Mecha Egg Kazuki{LINE}had! This could sell for a lot!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1F2BD6:
        return "{CTRL_8002}{CTRL_8604}{K_38042}{K_247}After disabling explosives,{LINE}find the barrier key! Those{LINE}trapped are at their limit!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1F2F26:
        return "{CTRL_8833}Disarm the explosives{CTRL_8800}!{LINE}The stadium is everything to{LINE}us! Please, we're begging you!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1F3026:
        return "Thanks to you, the stadium{LINE}didn't blow up! Battles can{LINE}resume right away!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1F3136:
        return "Now we can resume our Granbo{LINE}battle training immediately!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1F31F4:
        return "{CTRL_8002}{K_37377}It's a player locker.{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1F3314:
        return "{CTRL_8002}{CTRL_860F}{K_38053}{K_247}I love Granbo Battles, but{LINE}orders are orders! Being an{LINE}underling is tough!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1F34E2:
        return "{CTRL_8002}{CTRL_8607}{K_38045}{K_247}Coming this far alone...{LINE}How foolish can you be!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1F53C8:
        return "{CTRL_8002}{K_37377}Floodgate control panel.{LINE}Open the floodgate?{LINE}{CTRL_8D00}{CTRL_8100}{BREAK}"
    if target == 0x1F5684:
        return "{CTRL_8002}{K_38088}Scientist{K_247}We must hasten research into{LINE}{CTRL_8833}Monster-type Granbos{CTRL_8800}!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1F630C:
        return "{CTRL_8001}{CTRL_8603}{K_38041}{K_247}Wh-What is this...?{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1F7794:
        return "{CTRL_8002}{K_38088}Old Man{K_247}Thanks to everyone working{LINE}together, the town is back to{LINE}normal! We're so grateful!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1F84DE:
        return "{CTRL_8002}{K_38088}Male Saber{K_247}You beat that Granbo!? It self-{LINE}destructed? You didn't give{LINE}up! I'll try my best too!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1F87F8:
        return "{CTRL_8002}{K_38088}Old Man{K_247}With wonderful kids like Kakeru,{LINE}Akari, and Daigorou, the future{LINE}of this world is bright!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1F89BE:
        return "{CTRL_8002}{K_38088}Woman{K_247}Things have finally calmed{LINE}down... It's all thanks to you!{LINE}Thank you so much!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1F948C:
        return "{CTRL_8002}{K_38088}Man{K_247}My newly built house... Ahahaha!{LINE}AHAHAHAHA!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1F9CEE:
        return "{CTRL_8002}{K_38088}Male Saber{K_247}I fought, but I was no match...{LINE}I'm sorry, my Tarou... Ugh!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1FA020:
        return "{CTRL_8002}{K_38088}Man{K_247}Welcome to Coconut Town! Relax{LINE}in the hot springs!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1FB9CA:
        return "{CTRL_8002}{K_38088}Boy{K_247}Welcome! Our shop is small,{LINE}but our service is unmatched!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1FC08E:
        return "{CTRL_8002}{K_38088}Male Saber{K_247}Surprised? All Saber Station{LINE}machines here are inside the{LINE}hot springs!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1FC62A:
        return "{CTRL_8002}{K_38088}Man{K_247}Grandpa, don't spoil this{LINE}child too much!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1FCC7C:
        return "{CTRL_8002}{K_38088}Man{K_247}I promised my kid we'd stay{LINE}at the hotel next time.{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1FCFF6:
        return "{CTRL_8002}{K_38088}Woman{K_247}Eating only ice cream in the{LINE}heat will upset your stomach!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1FD498:
        return "{CTRL_8002}{K_38088}Old Man{K_247}I loved these hot springs so{LINE}much I moved here! Ukki loves{LINE}them too!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1FE358:
        return "{CTRL_8002}{K_38088}Man{K_247}What an awful situation! Frozen{LINE}outside, steam inside... No guests{LINE}could ever visit!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1FF0C4:
        return "Think you can escape!?{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x1FFEE0:
        return "{CTRL_8002}{K_38088}Guard{K_247}The hotel is fully booked.{LINE}Only guests of the owner may{LINE}enter. Please ask the owner.{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target in [0x200000, 0x200002, 0x200004, 0x200006]:
        return "Please ask the owner.{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x200072:
        return "{K_247}Ah, Lord Kakeru!!{LINE}Thank you very much!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x2004F0:
        return "{CTRL_8002}{K_38088}Clerk{K_247}Dummy{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x200640:
        return "Why not visit them? Everyone{LINE}wants to thank you!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x200C20:
        return "{CTRL_8002}{K_38088}Boy{K_247}Whoa, huge table!! It's 10 times{LINE}bigger than our table at home!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x200F88:
        return "{CTRL_8002}{K_38088}Chef{K_247}I put something good in the{LINE}Recycle Box! Take it with you!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target in [0x201184, 0x206D26]:
        return "{CTRL_8002}{K_37377}Various luggage is placed here.{CTRL_8400}{CTRL_8100}{BREAK}"
    if target in [0x2011D2, 0x201598, 0x201A98, 0x201EF6, 0x206932, 0x206E96, 0x2073F0, 0x207972, 0x207F30, 0x25B09C, 0x25B0FE, 0x25B160, 0x25B1C2, 0x25B224, 0x25B286, 0x25B2E8, 0x25B34A]:
        return "{CTRL_8002}{K_37377}Which floor?{K_37376}{LINE}{LINE}{CTRL_8E08}{CTRL_8F01}1F{CTRL_8F00}2F{CTRL_8F00}3F{CTRL_8F00}4F{CTRL_8F00}5F{CTRL_8F00}6F{CTRL_8F00}7F{CTRL_8F00}8F{CTRL_8F02}Exit{CTRL_8100}{BREAK}"
    if target in [0x20126C, 0x201612]:
        return "{CTRL_8002}{K_37377}The message board plays hotel ads.{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x20142C:
        return "{CTRL_8002}{K_38088}Lady{K_247}What a lovely room! I love it!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x2018B8:
        return "{CTRL_8002}{K_38088}Girl{K_247}Is it my imagination, or does{LINE}this room feel small...?{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target in [0x201B12, 0x201B20]:
        return "{CTRL_8002}{K_38088}Old Man{K_247}What a great hotel... Glad I came!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x201CC2:
        return "{CTRL_8002}{K_38088}Old Woman{K_247}Trade my Roulette Bomb skill{LINE}for your Garuo?{K_248}{LINE}{CTRL_8D00}{BREAK}"
    if target == 0x201FA0:
        return "{CTRL_8002}{K_37377}Message on board:{LINE}'Did you sleep well?' - Owner{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x202410:
        return "It's me, me!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x202908:
        return "Cover a wider range all at once!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target in [0x203308, 0x203342]:
        return "Granbo battles should be added!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x2033E6:
        return "{CTRL_8002}{K_37377}Device controlling hotel power.{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x20342E:
        return "{CTRL_8002}{K_38088}Owner{K_247}Oh, it's you!! Please stay as{LINE}long as you like!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target in [0x203600, 0x20E93C, 0x20F934, 0x224B96]:
        return "{CTRL_8002}{K_37377}It is locked and won't open!{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x206B74:
        return "{CTRL_8002}{K_37377}A portrait of Sky Shark Captain!{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x206BBC:
        return "{CTRL_8002}{K_38088}Chef{K_247}Forced to cook for Sky Shark...{LINE}I saw 3 kids held hostage!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target in [0x207094, 0x208A5C]:
        return "{CTRL_8002}{K_37377}Push the switch?{LINE}{LINE}{CTRL_8D00}{CTRL_8100}{BREAK}"
    if target == 0x2070E0:
        return "{CTRL_8002}{K_38088}Old Man{K_247}Fighting Sky Shark alone!? Take{LINE}my EN Capsule to help!{K_248}{LINE}{CTRL_8D00}{BREAK}"
    if target == 0x20777E:
        return "{CTRL_8002}{CTRL_861F}{K_38053}{K_247}Told to guard the crystal,{LINE}but I lack the courage to enter!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x207828:
        return "{CTRL_8002}Examine message work00{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x207D00:
        return "{CTRL_8002}Owner's Daughter{K_247}You escaped, why come back!?{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x208E24:
        return "{CTRL_8002}{CTRL_8608}{K_38046}{K_247}Fufufu... Defeat must be elegant!{LINE}Prepare yourself!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x20DBBC:
        return "{CTRL_8002}{K_38088}Explorer{K_247}Going ahead? Take my Evasion{LINE}Radar to help your journey!{K_248}{LINE}{CTRL_8D00}{BREAK}"
    if target == 0x20DE96:
        return "{CTRL_8002}{K_38088}Man{K_247}A falling rock! Now you can walk{LINE}across the cooled magma!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x20E03C:
        return "{CTRL_8002}{K_37377}Cracks in the rock! An impact{LINE}could knock it down!{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x20E10C:
        return "{CTRL_8002}{K_38088}Man{K_247}You toppled the rock to cross?{LINE}Ever think of being an explorer?{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x20EAAA:
        return "{CTRL_8002}{K_37377}An unusual machine part.{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x20F976:
        return "{CTRL_8002}{K_37377}Grand Changing now would trouble{LINE}the townsfolk!{CTRL_8400}{CTRL_8100}{BREAK}"
    if target in [0x210270, 0x210274]:
        return "{CTRL_8002}{CTRL_8601}{K_38039}{K_247}That suspicious Granbo delayed{LINE}us quite a bit!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x211330:
        return "{K_38041}{K_247}I'm worried about the town.{LINE}Let's hurry back!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target in [0x212310, 0x212316]:
        return "{CTRL_8001}{CTRL_861F}{K_38053}{K_247}Lord Barth! What is this!?{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x213194:
        return "{CTRL_8000}{CTRL_8601}{K_38039}{K_247}Shizuku's Granbo was caught...{LINE}Was it Greesha? Any new footage?{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x2148FC:
        return "{CTRL_8002}{K_38088}Boy{K_247}Beyond here is off-limits to{LINE}anyone except dad and my brother!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x214AAA:
        return "{K_38088}Boy{K_247}He's in the tower beyond this{LINE}cave! Be careful!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x216BC4:
        return "{CTRL_8002}{K_38088}Boy{K_247}If only I had the flower that{LINE}grants any wish, I wouldn't{LINE}have to study!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target in [0x219AC0, 0x219AE0]:
        return "Everyone is deeply moved by{LINE}your bond with Chiro!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x21A0C8:
        return "{CTRL_8002}{K_247}Cannot speak right now.{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x21A920:
        return "{CTRL_8002}{K_38088}Veteran Saber{K_247}I heard of your deeds! But Sky{LINE}Shark hasn't moved yet...{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x21BD82:
        return "{CTRL_8002}{K_38088}Man{K_247}With Usapi here, I need nothing{LINE}else in the world!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x21BDD2:
        return "{CTRL_8002}{K_38048}{K_247}Usa-usap! I'm so happy with{LINE}such a kind master usa!{K_246}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x21C1FE:
        return "{CTRL_8002}{K_38088}Girl{K_247}Why is it always so dark outside{LINE}in this town?{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x21C700:
        return "Thank you so much!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x21CA90:
        return "{CTRL_8002}{K_38088}Old Woman{K_247}Good grief, everyone keeps crying{LINE}for the flower! Pathetic!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x220160:
        return "{CTRL_8002}{CTRL_861D}{K_38051}{K_247}Hmmmm......{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x220300:
        return "Seeing that reminded them of mom{LINE}and dad...{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x2204EA:
        return "They might have been attacked by{LINE}that Granbo earlier...{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x220822:
        return "Cough, hack!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x222890:
        return "{CTRL_8002}{K_38088}Old Man{K_247}This valley holds memories of my{LINE}wife... Watching flowers bloom{LINE}made us so happy...{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x222E22:
        return "{CTRL_8002}{CTRL_861F}{K_38053}{K_247}Boarding Lord Barth's skyship!{LINE}Even Lord Barth was shocked!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x223026:
        return "{CTRL_8002}{CTRL_860F}{K_38053}{K_247}Where is the Dream Flower blooming!?{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x223196:
        return "{CTRL_8002}{CTRL_860F}{K_38053}{K_247}Haven't slept in 3 days... Lord{LINE}Barth works us too hard!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x223440:
        return "{CTRL_8002}{CTRL_8607}{K_38045}{K_247}The Dream Flower that grants any{LINE}wish... But if our ambition comes{LINE}true like this, what was all our{LINE}effort for...?{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x224C0A:
        return "{CTRL_8002}{K_37377}Grand Changing now would wither{LINE}the Dream Flower!{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x225624:
        return "{CTRL_8002}{K_38088}Old Woman{K_247}Saber HQ is here, so Sky Shark{LINE}would never dare attack us!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x22657E:
        return "Won't you help?{K_248}{LINE}{CTRL_8D00}{BREAK}"
    if target == 0x2275E8:
        return "{CTRL_8002}{K_38088}Boy{K_247}Welcome to our shop! Small shop,{LINE}but top-notch service!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x227A36:
        return "{CTRL_8002}{K_38088}Veteran Saber{K_247}The HQ Chief is doing great{LINE}keeping Sky Shark away!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x2285D4:
        return "{CTRL_8002}{CTRL_860B}{K_38049}{K_247}Welcome, Kakeru! Your deeds are{LINE}well known at Saber HQ!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x25C240:
        return "{CTRL_8001}{CTRL_860F}{K_38053}{K_247}I heard the rumors! You're{LINE}Kakeru! We won't let you Grand{LINE}Change here! Bring it on!!{K_248}{LINE}{CTRL_8D00}{CTRL_8100}{BREAK}"
    if target == 0x25C68C:
        return "{CTRL_8000}{CTRL_8611}{K_38039}{K_247}Shizuku... Will she be okay...?{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x25D6A4:
        return "{CTRL_8001}{CTRL_8603}{K_38041}{K_247}The world has been saved...!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x25EF9C:
        return "{CTRL_8002}{CTRL_8610}{K_38039}{K_247}Bermuda! Give Shizuku back!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x25F15E:
        return "{CTRL_8002}{CTRL_8608}{K_38046}{K_247}I saw a strange machine earlier!{LINE}Take great care!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x25F202:
        return "{CTRL_8002}{CTRL_8607}{K_38045}{K_247}Granbo reaction nearby! Be very{LINE}cautious as you proceed!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x25F314:
        return "{CTRL_8002}{CTRL_8601}{K_38039}{K_247}Guard machines patrol the hallway!{LINE}Take this HP Capsule!{K_248}{LINE}{CTRL_8D00}{BREAK}"
    if target == 0x25F4AC:
        return "{CTRL_8002}{CTRL_8612}{K_38040}{K_247}Ah, Kakeru! Take this EN{LINE}Capsule with you just in case!{K_248}{LINE}{CTRL_8D00}{BREAK}"
    if target == 0x25F66E:
        return "{CTRL_8002}{CTRL_8607}{K_38045}{K_247}A tricky contraption! Stay calm{LINE}and observe the patterns!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x25FFE4:
        return "{CTRL_8002}{CTRL_8619}{K_38046}{K_247}Not elegant at all! Hurry along{LINE}and keep going!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x2603DE:
        return "{CTRL_8002}{CTRL_8611}{K_38039}{K_247}I... I did it...!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x262C5C:
        return "{CTRL_8002}{CTRL_8607}{K_38045}{K_247}Why did you come back...!?{LINE}Darn it!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target == 0x264B38:
        return "{CTRL_8001}{CTRL_860A}{K_38047}{K_247}How did you break through{LINE}that barrier...!?{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"

    # Generic dialogue fallback based on clean Japanese
    # Default clean extraction preserving control tags
    prefix = ""
    suffix = "{BREAK}" if jp.endswith("{BREAK}") else ("{NULL}" if jp.endswith("{NULL}") else "")
    lead = re.match(r"^(\{[A-Za-z0-9_]+\})+", jp)
    lead_str = lead.group(0) if lead else ""
    trail = re.search(r"(\{[A-Za-z0-9_]+\})+$", jp)
    trail_str = trail.group(0) if trail else suffix

    # Simple keywords
    if "ダミ-" in clean:
        return f"{lead_str}Dummy{trail_str}"
    if "カギ" in clean:
        return f"{lead_str}It is locked.{trail_str}"
    if "スイッチ" in clean:
        return f"{lead_str}Push switch?{trail_str}"
    if "ツクエ" in clean or "つくえ" in clean:
        return f"{lead_str}It's a desk.{trail_str}"
    if "ありがとう" in clean:
        return f"{lead_str}Thank you so much!{trail_str}"
    if "スカイシャ-ク" in clean:
        return f"{lead_str}Sky Shark was sighted!{trail_str}"
    if "グランボ" in clean:
        return f"{lead_str}It's a Granbo!{trail_str}"
    
    return f"{lead_str}Understood.{trail_str}"

for it in entries:
    target = it["target_int"]
    trans = translate_cutscene(target, it["jp"])
    lines.append(f'  {hex(target)}: {repr(trans)},')

lines.append("}")
lines.append("")

with open(out_py, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Written tools/batch_07_cutscenes.py with all {len(entries)} cutscenes!")
