# -*- coding: utf-8 -*-
"""
translate_all_07_complete.py
Generates 100% complete English translations for all 636 entries of text/translations/07_system_menus_events.json.
Formats and word-wraps lines to <= 27 characters.
"""

import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

TAG_RE = re.compile(r"\{[A-Za-z0-9_]+\}")

def wrap_lines(text, max_len=27):
    if not text:
        return text
    suffix = ""
    if text.endswith("{BREAK}"):
        suffix = "{BREAK}"
        text = text[:-7]
    elif text.endswith("{NULL}"):
        suffix = "{NULL}"
        text = text[:-6]
        
    parts = text.split("{LINE}")
    wrapped_parts = []
    for part in parts:
        # Extract leading tags
        lead_tags = []
        while True:
            m = TAG_RE.match(part)
            if m:
                lead_tags.append(m.group(0))
                part = part[m.end():].lstrip()
            else:
                break
        lead_str = "".join(lead_tags)

        # Extract trailing tags
        trail_tags = []
        while True:
            m = re.search(r"\{[A-Za-z0-9_]+\}$", part)
            if m:
                trail_tags.insert(0, m.group(0))
                part = part[:m.start()].rstrip()
            else:
                break
        trail_str = "".join(trail_tags)

        # Split words
        words = part.split()
        if not words:
            wrapped_parts.append(lead_str + trail_str)
            continue

        lines = []
        cur_line = []
        cur_len = 0
        for w in words:
            # Length of visible word
            w_vis = re.sub(r"\{[A-Za-z0-9_]+\}", "", w)
            added_len = len(w_vis) + (1 if cur_line else 0)
            if cur_len + added_len <= max_len:
                cur_line.append(w)
                cur_len += added_len
            else:
                if cur_line:
                    lines.append(" ".join(cur_line))
                cur_line = [w]
                cur_len = len(w_vis)
        if cur_line:
            lines.append(" ".join(cur_line))

        if lines:
            lines[0] = lead_str + lines[0]
            lines[-1] = lines[-1] + trail_str
            wrapped_parts.append("{LINE}".join(lines))
        else:
            wrapped_parts.append(lead_str + trail_str)

    res = "{LINE}".join(wrapped_parts) + suffix
    return res

with open("text/translations/07_system_menus_events.json", "r", encoding="utf-8") as f:
    entries = json.load(f)

print(f"Loaded {len(entries)} entries to translate.")

# Exact mapping table by offset or ID
MAP = {}

# Field Inspection & Tournament Ranks (IDs 319-349)
MAP[0x26E348] = "Tribe{BREAK}"
MAP[0x26E370] = "EN Cost{BREAK}"
MAP[0x26E396] = "Attack... AT{BREAK}"
MAP[0x26E3A8] = "Defense... DF{BREAK}"
MAP[0x26E3BA] = "Speed... SP{BREAK}"
MAP[0x26E3CC] = "Origin{BREAK}"
MAP[0x26E428] = "Examined it.{CTRL_8300}{BREAK}"
MAP[0x26E436] = "Obtained it!{CTRL_8400}{BREAK}"
MAP[0x26E446] = "However, nothing was found.{BREAK}"
MAP[0x26E494] = "The effect wore off.{BREAK}"
MAP[0x26E4AE] = "Recovered from Stop!{BREAK}"
MAP[0x26E4E0] = "Recovered from Virus!{BREAK}"
MAP[0x26E4FA] = "{CTRL_8002}{K_37377}Grand Change complete!{CTRL_8300}Retracting Data Ball.{CTRL_8400}{CTRL_8100}{BREAK}"
MAP[0x26E542] = "{CTRL_8002}{K_37377}For security purposes,{LINE}this elevator only moves{LINE}to authorized floors.{CTRL_8400}{CTRL_8100}{BREAK}"
MAP[0x26E59C] = "{CTRL_8002}{K_37377}Changed clothes!{CTRL_8400}{CTRL_8100}{BREAK}"
MAP[0x26E5B8] = "Kakeru{BREAK}"
MAP[0x26E6C6] = "World Map{BREAK}"
MAP[0x26ECC8] = "Fledgling Saber{BREAK}"
MAP[0x26ECDE] = "2-match knockout{LINE}Qualified{NULL}"
MAP[0x26ED2C] = "Novice Saber{BREAK}"
MAP[0x26ED42] = "2-match knockout{LINE}Qualified{NULL}"
MAP[0x26ED9A] = "Amateur Saber{BREAK}"
MAP[0x26EDB0] = "2-match knockout{LINE}Qualified{NULL}"
MAP[0x26EE0A] = "Veteran Saber{BREAK}"
MAP[0x26EE20] = "3-match knockout{LINE}Qualified{NULL}"
MAP[0x26EE78] = "Three-Star Saber{BREAK}"
MAP[0x26EE8E] = "4-match knockout{LINE}Qualified{NULL}"
MAP[0x26EEE2] = "Master Saber{BREAK}"
MAP[0x26EEF8] = "4-match knockout{LINE}Qualified{NULL}"
MAP[0x26EF4A] = "Grand Saber{BREAK}"
MAP[0x26EF60] = "4-match knockout{LINE}Qualified{NULL}"

MAP[0x26EFBC] = "Super Saber{BREAK}"
MAP[0x26EFD2] = "5-match knockout{LINE}Qualified{NULL}"
MAP[0x26F02E] = "Ultra Saber{BREAK}"
MAP[0x26F044] = "5-match knockout{LINE}Qualified{NULL}"
MAP[0x26F09C] = "King Saber{BREAK}"
MAP[0x26F0B0] = "5-match knockout{LINE}Qualified{NULL}"
MAP[0x26F108] = "God Saber{BREAK}"
MAP[0x26F11C] = "6-match knockout{LINE}Qualified{NULL}"
MAP[0x26F170] = "All-Star{BREAK}"
MAP[0x26F182] = "7-match knockout{LINE}Qualified{NULL}"
MAP[0x26F21E] = "Defeated in match.{BREAK}"
MAP[0x26F230] = "Won the tournament!{BREAK}"
MAP[0x26F25E] = "Victory!{BREAK}"
MAP[0x26F26C] = "Select opponent class.{BREAK}"
MAP[0x26F286] = "Item Locker{BREAK}"
MAP[0x26F2F6] = "How much to deposit?{BREAK}"
MAP[0x26F316] = "How much to withdraw?{BREAK}"
MAP[0x26F336] = "Cannot deposit any more.{BREAK}"
MAP[0x26F358] = "Cannot withdraw any more.{BREAK}"
MAP[0x26F37C] = "You have no money to deposit.{BREAK}"
MAP[0x26F39C] = "No money currently deposited.{BREAK}"
MAP[0x26F3C0] = "Deposited Money{BREAK}"
MAP[0x26F3D8] = "Deposited Count{BREAK}"
MAP[0x26F3EE] = "How many to deposit?{BREAK}"
MAP[0x26F40E] = "How many to withdraw?{BREAK}"
MAP[0x26F42E] = "No items to deposit.{BREAK}"
MAP[0x26F452] = "No items currently deposited.{BREAK}"
MAP[0x26F47A] = "Deposit anything else?{BREAK}"
MAP[0x26F496] = "Withdraw anything else?{BREAK}"
MAP[0x26F4DC] = "Select a Data Ball to Grand Change.{BREAK}"
MAP[0x26F512] = "Grand Change with this?{NULL}"
MAP[0x26F54A] = "Cancel Grand Change?{NULL}"
MAP[0x26F582] = "No spare Data Balls to Grand Change.{BREAK}"
MAP[0x26F5B6] = "Cannot carry more spare Data Balls.{BREAK}"
MAP[0x26F5E2] = "Cannot Grand Change with this.{BREAK}"
MAP[0x26F606] = "Cannot Grand Change with 0 HP.{BREAK}"
MAP[0x26F63C] = "Data Ball System{BREAK}"
MAP[0x26F6B0] = "No spare Data Balls to deposit.{BREAK}"
MAP[0x26F6D8] = "No spare Data Balls deposited.{BREAK}"
MAP[0x26F704] = "Cannot carry more spare Data Balls.{BREAK}"
MAP[0x26F730] = "Select a Data Ball to swap.{BREAK}"
MAP[0x26F784] = "Select a Data Ball to withdraw.{BREAK}"
MAP[0x26F7AC] = "Select a Data Ball to delete.{BREAK}"
MAP[0x26F7DA] = "Select a Data Ball to initialize.{BREAK}"
MAP[0x26F806] = "Select a Data Ball to rename.{BREAK}"
MAP[0x26F836] = "Select Data Ball to evolve.{BREAK}"
MAP[0x26F864] = "Select Data Ball to insert.{BREAK}"
MAP[0x26F894] = "Select Data Ball to use.{BREAK}"
MAP[0x26F8C6] = "Insert this Data Ball?{NULL}"
MAP[0x26F8FE] = "Evolve into this Granbo?{NULL}"
MAP[0x26F936] = "Evolve into this Granbo?{NULL}"
MAP[0x26F96E] = "Cannot evolve any further.{BREAK}"
MAP[0x26F98E] = "How would you like to sort?{BREAK}"
MAP[0x26F9BA] = "Sorted.{BREAK}"
MAP[0x26F9CE] = "Initialized.{BREAK}"
MAP[0x26F9E2] = "Deleted.{BREAK}"
MAP[0x26F9F8] = "Deposited.{BREAK}"
MAP[0x26FA08] = "Withdrawn.{BREAK}"
MAP[0x26FA84] = "Is this okay?{NULL}"
MAP[0x26FABC] = "Select Granbo to appraise.{BREAK}"
MAP[0x26FAEA] = "Retracting Data Ball.{BREAK}"
MAP[0x26FB04] = "Enter name.{BREAK}"
MAP[0x26FB40] = "End{BREAK}"
MAP[0x26FB48] = "Back{BREAK}"
MAP[0x26FBEC] = "Not enough money.{BREAK}"
MAP[0x26FBFE] = "Inventory full. Cannot hold more.{BREAK}"
MAP[0x26FC1E] = "No items to sell.{BREAK}"
MAP[0x26FC58] = "Won the battle!!!{BREAK}"
MAP[0x26FC6C] = "G obtained!{BREAK}"
MAP[0x26FC7C] = "obtained!{BREAK}"
MAP[0x26FC8C] = "Skill item obtained!{BREAK}"
MAP[0x26FCAA] = "Learned a new skill!{BREAK}"
MAP[0x26FCC2] = "Rank points acquired!{BREAK}"
MAP[0x26FCF2] = "EXP points acquired!{BREAK}"
MAP[0x26FD2E] = "Select a skill to delete.{BREAK}"
MAP[0x26FD56] = "deleted.{BREAK}"
MAP[0x26FD6A] = "Gave up learning.{BREAK}"
MAP[0x26FD86] = "Did not learn.{BREAK}"
MAP[0x26FD94] = "Obtained new Data Ball.{BREAK}"
MAP[0x26FDB4] = "Is this okay?{NULL}"
MAP[0x26FDEC] = "Select Data Ball to transfer.{BREAK}"
MAP[0x26FE2C] = "Hunted Data Ball{BREAK}"
MAP[0x26FE4C] = "obtained.{BREAK}"
MAP[0x26FE5A] = "Select Granbo to trade.{BREAK}"
MAP[0x26FEAC] = "Inventory full.{BREAK}"
MAP[0x26FEF0] = "Gave up.{BREAK}"
MAP[0x26FEFE] = "Discarded.{BREAK}"
MAP[0x26FF0A] = "Select Data Ball to send to system.{BREAK}"
MAP[0x26FF3A] = "Received Data Ball{BREAK}"
MAP[0x26FF64] = "Cannot send to system. Delete Data Balls.{BREAK}"
MAP[0x270008] = "Who will use this?{BREAK}"
MAP[0x27001E] = "Use this?{BREAK}"
MAP[0x27002E] = "No items.{BREAK}"
MAP[0x270044] = "Cannot use this item now.{BREAK}"
MAP[0x270062] = "Using it here has no effect.{BREAK}"
MAP[0x27007C] = "Cannot learn this skill.{BREAK}"
MAP[0x270098] = "Discard this?{BREAK}"
MAP[0x2700A8] = "Discarded.{BREAK}"
MAP[0x2700B6] = "Granbo command.{BREAK}"
MAP[0x2700CE] = "Use item.{BREAK}"
MAP[0x2700E2] = "Display information.{BREAK}"
MAP[0x2700FE] = "System command.{BREAK}"
MAP[0x270114] = "Use skill.{BREAK}"
MAP[0x270124] = "Transform.{BREAK}"
MAP[0x270134] = "Check status.{BREAK}"
MAP[0x270150] = "Use standard item.{BREAK}"
MAP[0x27016E] = "Use key item.{BREAK}"
MAP[0x27018C] = "Learn skill.{BREAK}"
MAP[0x2701A4] = "What will you do?{BREAK}"
MAP[0x2701CE] = "View map.{BREAK}"
MAP[0x2701EA] = "Database.{BREAK}"
MAP[0x2701FC] = "Display player data.{BREAK}"
MAP[0x27021E] = "Save game.{BREAK}"
MAP[0x270238] = "Link battle.{BREAK}"
MAP[0x27024C] = "Change settings.{BREAK}"
MAP[0x270268] = "Whose skill will you use?{BREAK}"
MAP[0x270282] = "Cannot use now.{BREAK}"
MAP[0x270292] = "Has no skills.{BREAK}"
MAP[0x2702A8] = "Not enough EN.{BREAK}"
MAP[0x2702BA] = "Which Mecha Egg to Transform?{BREAK}"
MAP[0x2702E0] = "Transform into what?{BREAK}"
MAP[0x2702F8] = "No spare Data Ball to Transform.{BREAK}"
MAP[0x270328] = "Is this okay?{NULL}"
MAP[0x270360] = "Whose stats to view?{BREAK}"
MAP[0x2703A0] = "Creator Name{BREAK}"
MAP[0x2703DA] = "Evolution List{BREAK}"
MAP[0x270408] = "Standby{NULL}"
MAP[0x270430] = "Standby{NULL}"
MAP[0x270458] = "Standby{NULL}"
MAP[0x27047C] = "Used.{BREAK}"
MAP[0x270486] = "Learn this new skill?{BREAK}"
MAP[0x27049E] = "Select a skill to delete.{BREAK}"
MAP[0x2704C6] = "Delete skill. Is this okay?{NULL}"
MAP[0x270512] = "Who will learn this?{BREAK}"
MAP[0x27052E] = "Learned skill.{BREAK}"
MAP[0x27053E] = "Already knows this skill.{BREAK}"
MAP[0x270562] = "Save game?{BREAK}"
MAP[0x270574] = "Saving...{BREAK}"
MAP[0x270586] = "Save complete.{BREAK}"
MAP[0x27059C] = "Save failed.{BREAK}"
MAP[0x2705E0] = "Type{BREAK}"
MAP[0x2705EA] = "Play Time{BREAK}"
MAP[0x270600] = "SFX{BREAK}"
MAP[0x27060C] = "BGM{BREAK}"
MAP[0x270630] = "Text Speed{BREAK}"
MAP[0x2707E8] = "Connecting...{BREAK}"
MAP[0x2707FA] = "Begin link battle with{LINE}these rules?{BREAK}"
MAP[0x270812] = "Begin?{BREAK}"
MAP[0x270826] = "Please wait.{BREAK}"
MAP[0x270854] = "Waiting for opponent...{BREAK}"
MAP[0x270874] = "Decide on rules once more.{BREAK}"
MAP[0x270892] = "Won the match!{BREAK}"
MAP[0x2708A0] = "Lost the match!{BREAK}"
MAP[0x2708AE] = "Starting match.{BREAK}"
MAP[0x2708EE] = "Connection failed.{BREAK}"
MAP[0x270902] = "Select Data Ball to wager.{BREAK}"
MAP[0x270928] = "Are these terms okay?{NULL}"
MAP[0x270960] = "obtained!{BREAK}"
MAP[0x270970] = "lost!{BREAK}"
MAP[0x27097C] = "Won!{BREAK}"
MAP[0x27098C] = "Could not win!{BREAK}"
MAP[0x2709A2] = "Is this okay?{BREAK}"
MAP[0x2709B6] = "Are these conditions okay?{BREAK}"
MAP[0x2709D8] = "Select Data Ball.{BREAK}"
MAP[0x270A16] = "From opponent:{BREAK}"
MAP[0x270A24] = "Can take.{BREAK}"
MAP[0x270A3C] = "Will be taken.{BREAK}"
MAP[0x270A4A] = "Skill{BREAK}"
MAP[0x270A50] = "Granbo{BREAK}"
MAP[0x270A5A] = "Item{BREAK}"
MAP[0x270A64] = "Match aborted.{BREAK}"
MAP[0x270A76] = "Save before battle. Is this okay?{NULL}"
MAP[0x270AC2] = "Declined by opponent.{BREAK}"
MAP[0x270B2A] = "GBA Game Link Cable not connected,{LINE}or opponent is not ready.{BREAK}"
MAP[0x270BA4] = "Rule Settings{BREAK}"
MAP[0x270BB4] = "Battle Style{NULL}"
MAP[0x270BC8] = "Item Usage{NULL}"
MAP[0x270BDE] = "Turn Limit{NULL}"
MAP[0x270C5C] = "Skill Battle{NULL}"
MAP[0x270C6E] = "Granbo Battle{NULL}"
MAP[0x270C80] = "Item Battle{NULL}"
MAP[0x270C92] = "Present Battle{BREAK}"
MAP[0x270CA4] = "Wager skills and battle.{BREAK}"
MAP[0x270CC4] = "Wager Granbos and battle.{BREAK}"
MAP[0x270CE8] = "Wager items and battle.{BREAK}"
MAP[0x270D0C] = "Battle for random presents.{BREAK}"
MAP[0x270D3A] = "Set item usage limit.{BREAK}"
MAP[0x270D58] = "Set number of battle turns.{BREAK}"
MAP[0x270D70] = "Settings complete.{BREAK}"
MAP[0x270D86] = "Take any reward from opponent.{BREAK}"
MAP[0x270DAC] = "Take wagered prizes from each other.{BREAK}"
MAP[0x270DD0] = "Your wagered skill{BREAK}"
MAP[0x270DE4] = "Opponent's wagered skill{BREAK}"
MAP[0x270E10] = "Opponent's wagered Granbo{BREAK}"
MAP[0x270E28] = "Your wagered item{BREAK}"
MAP[0x270E58] = "Present Item{BREAK}"
MAP[0x270E8A] = "{CTRL_8001}{CTRL_8602}{K_38040}{K_247}Now let's explain{LINE}{CTRL_8833}Evolution{CTRL_8800}!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
MAP[0x270ECE] = "{CTRL_8001}{CTRL_8602}{K_38040}{K_247}Suppose you carry these{LINE}Data Balls...{WAIT}{CTRL_8602}{K_38040}{K_247}Choose which Data Ball{LINE}you wish to evolve!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
MAP[0x270F7A] = "{CTRL_8001}{CTRL_8602}{K_38040}{K_247}Let's use {CTRL_8877}Boton{CTRL_8800} as an{LINE}example!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
MAP[0x270FB8] = "{CTRL_8001}{CTRL_8602}{K_38040}{K_247}Information on the Data Ball{LINE}to evolve is shown here!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"

# Credits (IDs 564-599)
MAP[0x2722E0] = "Granbo Development Staff{BREAK}"
MAP[0x2722FA] = "{CTRL_8833}Planning{CTRL_8800}{BREAK}"
MAP[0x272306] = "Yoshimatsu{NULL}"
MAP[0x272328] = "Yamada{NULL}"
MAP[0x27233A] = "{CTRL_8855}Programmers{CTRL_8800}{BREAK}"
MAP[0x27234C] = "Bandou{NULL}"
MAP[0x27235E] = "Enomoto{NULL}"
MAP[0x272370] = "Yamanouchi{NULL}"
MAP[0x272386] = "Ootani{NULL}"
MAP[0x27239A] = "Yamamura{NULL}"
MAP[0x2723AC] = "{CTRL_8877}Characters{CTRL_8800}{BREAK}"
MAP[0x2723BE] = "Tazaki{NULL}"
MAP[0x2723D0] = "Araki{NULL}"
MAP[0x2723E0] = "Kai{NULL}"
MAP[0x2723F0] = "{CTRL_8899}Backgrounds{CTRL_8800}{BREAK}"
MAP[0x2723FE] = "Nakadai{NULL}"
MAP[0x272410] = "Gotou{NULL}"
MAP[0x272422] = "Iwamoto{NULL}"
MAP[0x272436] = "Suekane{NULL}"
MAP[0x272448] = "{CTRL_88BB}Design{CTRL_8800}{BREAK}"
MAP[0x272456] = "Tsukada{NULL}"
MAP[0x272466] = "{CTRL_8855}Sound Effects{CTRL_8800}{BREAK}"
MAP[0x272476] = "Hama{NULL}"
MAP[0x272484] = "{CTRL_8877}Music{CTRL_8800}{BREAK}"
MAP[0x272492] = "Fujita{NULL}"
MAP[0x2724A2] = "{CTRL_8899}Bug Management{CTRL_8800}{BREAK}"
MAP[0x2724B2] = "Okamoto{NULL}"
MAP[0x2724C6] = "Miyazaki{NULL}"
MAP[0x2724D6] = "{CTRL_88BB}Promotional Producer{CTRL_8800}{BREAK}"
MAP[0x2724F2] = "Inaba{NULL}"
MAP[0x272502] = "{CTRL_8833}General Producer{CTRL_8800}{BREAK}"
MAP[0x27251E] = "Mikami{NULL}"
MAP[0x27252E] = "{CTRL_8855}Director{CTRL_8800}{BREAK}"
MAP[0x272540] = "Matsushita{NULL}"
MAP[0x27257E] = "{CTRL_8A02}Gahahahaha!{NULL}"
MAP[0x2725B2] = "{CTRL_8A02}Hmph...{NULL}"

# Evolution tutorials (IDs 550-563)
MAP[0x271026] = "{CTRL_8001}{CTRL_8602}{K_38040}{K_247}Here, {CTRL_8877}Boton{CTRL_8800}'s{LINE}{CTRL_8833}evolution form{CTRL_8800} is shown{LINE}in silhouette!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
MAP[0x27108C] = "{CTRL_8001}{CTRL_8602}{K_38040}{K_247}Here, the Data Balls{LINE}needed for {CTRL_8833}evolution{CTRL_8800}{LINE}are displayed!{WAIT}{CTRL_8602}{K_38040}{K_247}Let's select {CTRL_8877}Hopper{CTRL_8800}!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
MAP[0x27111A] = "{CTRL_8001}{CTRL_8602}{K_38040}{K_247}From your stored balls,{LINE}{CTRL_8877}Hopper{CTRL_8800} is shown.{LINE}Choose it for {CTRL_8833}evolution{CTRL_8800}!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
MAP[0x2711A2] = "{CTRL_8001}{CTRL_8602}{K_38040}{K_247}Remember: once inserted,{LINE}a ball cannot be removed!{WAIT}{CTRL_8602}{K_38040}{K_247}Only stored Data Balls{LINE}can be inserted!{WAIT}{CTRL_8602}{K_38040}{K_247}So verify carefully{LINE}before inserting!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
MAP[0x2712B2] = "{CTRL_8001}{CTRL_8602}{K_38040}{K_247}Hopper is now set!{WAIT}{CTRL_8602}{K_38040}{K_247}Now insert the remaining{LINE}Data Balls the same way!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
MAP[0x271324] = "{CTRL_8001}{CTRL_8602}{K_38040}{K_247}All balls needed for{LINE}{CTRL_8833}evolution{CTRL_8800} are inserted!{WAIT}{CTRL_8602}{K_38040}{K_247}And then...!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
MAP[0x271396] = "{CTRL_8001}{CTRL_8602}{K_38040}{K_247}{CTRL_8877}Boton{CTRL_8800} evolved into{LINE}{CTRL_8877}Mokumon{CTRL_8800}! Success!{WAIT}{CTRL_8602}{K_38040}{K_247}Evolving raises HP, EN,{LINE}AT, DF, and SP by 10%!{WAIT}{CTRL_8602}{K_38040}{K_247}There's one more thing{LINE}you need to know!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
MAP[0x271492] = "{CTRL_8001}{CTRL_8602}{K_38040}{K_247}Let's use {CTRL_8833}Piyorika{CTRL_8800}{LINE}as an example!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
MAP[0x2714CA] = "{CTRL_8001}{CTRL_8602}{K_38040}{K_247}To insert into {CTRL_8899}?{CTRL_8800},{LINE}all other slots must be{LINE}filled first!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
MAP[0x271544] = "{CTRL_8001}{CTRL_8602}{K_38040}{K_247}Now that Ohm and Salab are{LINE}set, {CTRL_8899}?{CTRL_8800} is unlocked!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
MAP[0x2715BC] = "{CTRL_8001}{CTRL_8602}{K_38040}{K_247}You can insert any ball{LINE}into {CTRL_8899}?{CTRL_8800}!{WAIT}{CTRL_8602}{K_38040}{K_247}Special combinations cause{LINE}a unique {CTRL_8833}Mutation{CTRL_8800}!{WAIT}{CTRL_8602}{K_38040}{K_247}Try inserting various{LINE}balls to discover them!{WAIT}{CTRL_8602}{K_38040}{K_247}This special evolution is{LINE}called a {CTRL_8833}Branch{CTRL_8800}!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
MAP[0x27171E] = "{CTRL_8001}{CTRL_8602}{K_38040}{K_247}That covers {CTRL_8833}evolution{CTRL_8800}!{WAIT}{CTRL_8602}{K_38040}{K_247}Try evolving various{LINE}Granbos!{WAIT}{CTRL_8602}{K_38040}{K_247}The Data Pad lets you view{LINE}evolutions anytime!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
MAP[0x271812] = "{K_37377}Got a {CTRL_8833}new Mecha Egg{CTRL_8800}!{LINE}{CTRL_8855}Tamajan{CTRL_8800}'s Data Ball{LINE}is set inside!{BREAK}"
MAP[0x27186E] = "{K_37377}Got a {CTRL_8833}new Mecha Egg{CTRL_8800}!{LINE}{CTRL_8877}Hopper{CTRL_8800}'s Data Ball{LINE}is set inside!{BREAK}"

# Battle & Hunt tutorials (IDs 600-635)
MAP[0x2725D8] = "{CTRL_8A02}Ohohohoho!{NULL}"
MAP[0x272624] = "{CTRL_8A02}Fwahahaha!{NULL}"
MAP[0x272720] = "{CTRL_8A02}Alright! It's time{LINE}to battle!!!{CTRL_8C00}{BREAK}"
MAP[0x27273A] = "{CTRL_8A02}I will definitely get{LINE}my hands on it!!{CTRL_8C00}{BREAK}"
MAP[0x272758] = "{CTRL_8A02}Great!! Obtained the{LINE}Data Ball!!{CTRL_8C00}{BREAK}"
MAP[0x27278C] = "{CTRL_8A02}Too bad... Couldn't get{LINE}the Data Ball...{CTRL_8C00}{BREAK}"
MAP[0x2727C6] = "{CTRL_8A02}Great!! Got the Data Ball!{LINE}Taking it by force reset{LINE}it to LV1...{CTRL_8C00}{BREAK}"
MAP[0x27282E] = "{CTRL_8A02}Found item in pocket!{CTRL_8C00}{BREAK}"
MAP[0x272856] = "{CTRL_8A02}Found nothing in pocket...{CTRL_8C00}{BREAK}"
MAP[0x272888] = "{CTRL_8A02}Remembered forgotten skill!{CTRL_8C00}{BREAK}"
MAP[0x2729B0] = "{CTRL_8A01}{K_37377}You were wiped out!{LINE}Your money was cut{LINE}in half!{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x272CDC] = "Stats{BREAK}"
MAP[0x272CF2] = "To Next LV{NULL}"
MAP[0x272FD8] = "{CTRL_8A01}{CTRL_8620}{K_38055}{K_247}Thanks to the Hunt Glove,{LINE}you can use {CTRL_8833}Hunt Skills{CTRL_8800}!{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x273028] = "{CTRL_8A01}{CTRL_8620}{K_38055}{K_247}Use Hunt Skills to capture{LINE}enemy Data Balls!{WAIT}{CTRL_8620}{K_38055}{K_247}Using it right at the start{LINE}won't succeed!!{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x2730B4] = "{CTRL_8A01}{CTRL_8620}{K_38055}{K_247}This is the {CTRL_8833}Hunt Gauge{CTRL_8800}.{LINE}Dealing damage fills it!{WAIT}{CTRL_8620}{K_38055}{K_247}The fuller the gauge,{LINE}the easier the capture!{WAIT}{CTRL_8620}{K_38055}{K_247}Now attack and fill{LINE}the Hunt Gauge!{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x273198] = "{CTRL_8A01}{CTRL_8620}{K_38055}{K_247}That bar on the right is{LINE}the {CTRL_8833}Hunt Gauge{CTRL_8800}.{LINE}See it filling up?{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x2731F8] = "{CTRL_8A01}{CTRL_8620}{K_38055}{K_247}The gauge is red and full!{LINE}This is your {CTRL_8833}Hunt Chance{CTRL_8800}!{WAIT}{CTRL_8620}{K_38055}{K_247}Use a Hunt Skill now!{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x273274] = "{CTRL_8A01}{CTRL_8620}{K_38055}{K_247}The enemy is paralyzed!{LINE}Now, take the Data Ball!{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x2732CA] = "{CTRL_8A01}{CTRL_8620}{K_38055}{K_247}Hunt Success! Splendid!!{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x2732FA] = "{CTRL_8A01}{CTRL_8620}{K_38055}{K_247}You defeated it...{LINE}This hunt failed.{WAIT}{CTRL_8620}{K_38055}{K_247}Fill the gauge while{LINE}leaving plenty of HP!{WAIT}{CTRL_8620}{K_38055}{K_247}That way your hunts will{LINE}surely succeed!{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x2733E6] = "{CTRL_8A01}{CTRL_8620}{K_38055}{K_247}With a spare Data Ball,{LINE}you can {CTRL_8833}Transform{CTRL_8800} here!{WAIT}{CTRL_8620}{K_38055}{K_247}Transforming gives you an{LINE}advantage in battle.{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x27347E] = "{CTRL_8A01}{CTRL_8620}{K_38055}{K_247}With a spare Data Ball,{LINE}you can {CTRL_8833}Transform{CTRL_8800} here!{WAIT}{CTRL_8620}{K_38055}{K_247}Transforming lets you fight{LINE}with an advantage.{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x273512] = "{CTRL_8A01}{CTRL_8620}{K_38055}{K_247}Looks dangerous!{LINE}Let me heal you!{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x27354A] = "{CTRL_8A01}{CTRL_8620}{K_38055}{K_247}One last thing...{WAIT}{CTRL_8620}{K_38055}{K_247}Gauge fill speed depends{LINE}on elemental affinity!{WAIT}{CTRL_8620}{K_38055}{K_247}Using effective Granbos{LINE}makes hunting easier!{WAIT}{CTRL_8620}{K_38055}{K_247}Ask other Sabers for tips{LINE}to learn more!{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x274BFC] = "{CTRL_8A01}{CTRL_8614}{K_38043}{K_247}Listen closely, okay?{LINE}Remember what I say!{WAIT}{CTRL_8614}{K_38043}{K_247}First, fight normally!{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x274C62] = "{CTRL_8A01}{CTRL_8614}{K_38043}{K_247}It came!!{WAIT}{CTRL_8614}{K_38043}{K_247}When Waon was in danger,{LINE}a Fire Granbo came to help!{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x274CD6] = "{CTRL_8A01}{CTRL_8614}{K_38043}{K_247}That is {CTRL_8833}Grand Help{CTRL_8800}!!{WAIT}{CTRL_8614}{K_38043}{K_247}Now let's do our best and{LINE}defeat the enemy!!{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x274D4A] = "{CTRL_8A01}{CTRL_8614}{K_38043}{K_247}So frustrating===!!{LINE}Almost had it defeated!!{WAIT}{CTRL_8614}{K_38043}{K_247}Won't someone come to help{LINE}one more time?{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x274DC0] = "{CTRL_8A01}{CTRL_8614}{K_38043}{K_247}Eeeek===!! It came!!{WAIT}{CTRL_8614}{K_38043}{K_247}So lucky====!!{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x275010] = "{CTRL_8A01}{CTRL_8614}{K_38043}{K_247}Let's keep this momentum{LINE}going!!{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x27503E] = "{CTRL_8A01}{CTRL_8609}{K_38047}{K_247}I admire your courage...{WAIT}{CTRL_8609}{K_38047}{K_247}Let me teach you difference{LINE}between bravery and folly!{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x2750BE] = "{CTRL_8A01}{CTRL_8609}{K_38047}{K_247}Better than expected.{WAIT}{CTRL_8609}{K_38047}{K_247}However, the real fight{LINE}begins right now.{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x27510C] = "{CTRL_8A01}{CTRL_8609}{K_38047}{K_247}What's the matter?{LINE}Show me what you've got.{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x27514A] = "{CTRL_8A01}{CTRL_8609}{K_38047}{K_247}Haven't you realized?{WAIT}{CTRL_8609}{K_38047}{K_247}Without a spare Data Ball,{LINE}you can't do anything more.{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"
MAP[0x2751C8] = "{CTRL_8A01}{CTRL_8609}{K_38047}{K_247}Playtime is officially over!{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}"

# Now import the full cutscenes dictionary generator
sys.path.append("tools")
import batch_07_cutscenes as cutscene_data

# Merge all mappings
all_maps = {**MAP, **cutscene_data.CUTSCENE_MAP}

applied = 0
for it in entries:
    target = it["target_int"]
    if target in all_maps:
        it["en"] = wrap_lines(all_maps[target])
        applied += 1
    elif it.get("en", "").strip():
        it["en"] = wrap_lines(it["en"])
        applied += 1

print(f"Total translated entries: {applied}/{len(entries)}")

# Save updated dataset
with open("text/translations/07_system_menus_events.json", "w", encoding="utf-8") as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

print("Saved to text/translations/07_system_menus_events.json!")
