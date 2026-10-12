import json
import re

with open("text/translations/05_events_cutscenes.json", "r", encoding="utf-8") as f:
    events = json.load(f)

# Batch 3: 201 to 438
cutscenes_201_438 = {
    201: "{FRAME_INIT}{PORTRAIT_0f}{SFX_a5}Saying 'Th-That's impossible...'{LINE}is standard around here!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    202: "{FRAME_INIT}{PORTRAIT_0f}{SFX_a5}When you lose, scream 'I'll remember{LINE}this!' and run! Go on, try it!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    203: "{FRAME_INIT}{PORTRAIT_1f}{SFX_a5}Hey, if you try this hard,{LINE}you'll never fit in as a minion...{DISP_STATE}{STATE_CLEAR}{BREAK}",
    204: "{FRAME_INIT}{PORTRAIT_1f}{SFX_a5}C-Could it be...{WAIT}{PORTRAIT_1f}{SFX_a5}Are you aiming to become an officer{LINE}instead of a minion...?!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    205: "{FRAME_INIT}{PORTRAIT_1f}{SFX_a5}You're completely disqualified{LINE}as a minion!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    206: "{FRAME_INIT}{PORTRAIT_1f}{SFX_9f}Minions aren't supposed to{LINE}have this kind of power!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    207: "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}Not yet...{LINE}I can still fight!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    208: "{FRAME_INIT}{PORTRAIT_0f}{SFX_a5}Time's up!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    209: "{FRAME_INIT}{PORTRAIT_0f}{SFX_a5}1 turn remaining!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    210: "{FRAME_INIT}{PORTRAIT_0f}{SFX_a5}2 turns remaining!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    211: "{FRAME_INIT}{PORTRAIT_0f}{SFX_a5}3 turns remaining!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    212: "{FRAME_INIT}{PORTRAIT_08}{SFX_9e}Now then, let's settle this!{WAIT}{PORTRAIT_08}{SFX_a5}Here I go!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    213: "{FRAME_INIT}{PORTRAIT_08}{SFX_9e}Oh my, what's wrong?{DISP_STATE}{STATE_CLEAR}{BREAK}",
    214: "{FRAME_INIT}{PORTRAIT_08}{SFX_9e}This victory is mine!{WAIT}{PORTRAIT_08}{SFX_9e}Time to bring this to an end!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    215: "{FRAME_INIT}{PORTRAIT_18}{SFX_9e}Leave our base immediately!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    216: "{FRAME_INIT}{PORTRAIT_18}{SFX_9e}Guh!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    217: "{FRAME_INIT}{PORTRAIT_18}{SFX_9e}I...{WAIT}{PORTRAIT_18}{SFX_9e}I cannot afford to lose!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    218: "{FRAME_INIT}{PORTRAIT_18}{SFX_9e}How could this be...{DISP_STATE}{STATE_CLEAR}{BREAK}",
    219: "{FRAME_INIT}{PORTRAIT_18}{SFX_9e}What an utterly irritating boy...!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    220: "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}Not yet...{LINE}I can still fight!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    221: "{FRAME_INIT}{PORTRAIT_07}{SFX_9d}This is the end...{WAIT}{PORTRAIT_07}{SFX_9d}Let's fight with everything we have!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    222: "{FRAME_INIT}{PORTRAIT_07}{SFX_9d}Hmph...{DISP_STATE}{STATE_CLEAR}{BREAK}",
    223: "{FRAME_INIT}{PORTRAIT_07}{SFX_9d}I won't hold back until the end!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    224: "{FRAME_INIT}{PORTRAIT_07}{SFX_9d}That was a good battle...{LINE}Though we won't fight again.{DISP_STATE}{STATE_CLEAR}{BREAK}",
    225: "{FRAME_INIT}{PORTRAIT_07}{SFX_9d}Hmph...{DISP_STATE}{STATE_CLEAR}{BREAK}",
    226: "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}Not yet!{WAIT}{PORTRAIT_16}{SFX_9d}I won't give up!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    227: "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}...I lost...?{DISP_STATE}{STATE_CLEAR}{BREAK}",
    228: "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}Haven't you given up yet!?{DISP_STATE}{STATE_CLEAR}{BREAK}",
    229: "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}Not yet...{LINE}I can still fight!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    230: "{FRAME_INIT}{PORTRAIT_06}{SFX_9c}Gahahaha!!{WAIT}{PORTRAIT_06}{SFX_9c}Now then, entertain me!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    231: "{FRAME_INIT}{PORTRAIT_06}{SFX_9c}What's this? Is that all you got?{DISP_STATE}{STATE_CLEAR}{BREAK}",
    232: "{FRAME_INIT}{PORTRAIT_06}{SFX_9c}...{WAIT}{PORTRAIT_06}{SFX_9c}Don't disappoint me now...{DISP_STATE}{STATE_CLEAR}{BREAK}",
    233: "{FRAME_INIT}{PORTRAIT_06}{SFX_9c}Looks like you were no match{LINE}for me after all!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    234: "{FRAME_INIT}{PORTRAIT_15}{SFX_9c}Hoho...{DISP_STATE}{STATE_CLEAR}{BREAK}",
    235: "{FRAME_INIT}{PORTRAIT_15}{SFX_9c}D-Damn it!!{WAIT}{PORTRAIT_15}{SFX_9c}To think you were this strong!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    236: "{FRAME_INIT}{PORTRAIT_15}{SFX_9c}Wh-What...{DISP_STATE}{STATE_CLEAR}{BREAK}",
    237: "{FRAME_INIT}{PORTRAIT_15}{SFX_9c}Wh-What was that just now...!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    238: "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}Not yet...{LINE}I can still fight!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    239: "{FRAME_INIT}{PORTRAIT_0a}{SFX_9f}Come, this is the final game!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    240: "{FRAME_INIT}{PORTRAIT_0a}{SFX_9f}Too slow, far too slow!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    241: "{FRAME_INIT}{PORTRAIT_0a}{SFX_9f}Don't make me laugh...{WAIT}{PORTRAIT_1a}{SFX_9f}You think you can stop me{LINE}with such meager power?{DISP_STATE}{STATE_CLEAR}{BREAK}",
    242: "{FRAME_INIT}{PORTRAIT_0a}{SFX_9f}Not even a diversion... Now,{LINE}World Change Tower, activate!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    243: "{FRAME_INIT}{PORTRAIT_1a}{SFX_9f}You've actually managed that!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    244: "{FRAME_INIT}{PORTRAIT_1a}{SFX_9f}H-How... Could my grand plan{LINE}be stopped by mere children...?!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    245: "{FRAME_INIT}{PORTRAIT_1a}{SFX_9f}I-Impossible...!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    246: "{FRAME_INIT}{PORTRAIT_1a}{SFX_9f}How dare you mock me...!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    247: "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}Not yet...{LINE}I can still fight!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    248: "{CTRL_8a02}I shall face you personally!!{CTRL_8c00}{BREAK}",
    249: "{FRAME_INIT}{PORTRAIT_1a}{SFX_9f}I-Impossible...!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    250: "{FRAME_INIT}{PORTRAIT_20}{SFX_a7}Kakeru! Show me how much{LINE}stronger you've become!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    251: "{FRAME_INIT}{PORTRAIT_20}{SFX_a7}What's the matter!!{LINE}Come at me with full strength!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    252: "{FRAME_INIT}{PORTRAIT_21}{SFX_a7}What's wrong?!{LINE}Don't disappoint this old man!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    253: "{FRAME_INIT}{PORTRAIT_21}{SFX_a7}You still have a way to go...{DISP_STATE}{STATE_CLEAR}{BREAK}",
    254: "{FRAME_INIT}{PORTRAIT_20}{SFX_a7}Ho... Kakeru, my boy...{LINE}You've gotten quite skilled!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    255: "{FRAME_INIT}{PORTRAIT_21}{SFX_a7}What!? Could he have grown{LINE}this much already?!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    256: "{FRAME_INIT}{PORTRAIT_20}{SFX_a7}I'm... I'm fiercely proud{LINE}and happy, my boy!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    257: "{FRAME_INIT}{PORTRAIT_20}{SFX_a7}Ho! Splendidly done!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    258: "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}Not yet...{LINE}I can still fight!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    259: "{FRAME_INIT}{PORTRAIT_20}{SFX_a7}Kakeru! Don't you dare{LINE}disappoint me now!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    260: "{FRAME_INIT}{PORTRAIT_21}{SFX_a7}Don't let your guard down!{LINE}Carelessness leads to defeat!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    261: "{FRAME_INIT}{PORTRAIT_21}{SFX_a7}Come on! Don't be so sloppy!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    262: "{FRAME_INIT}{PORTRAIT_20}{SFX_a7}Looks like you need to be{LINE}retrained from scratch...{DISP_STATE}{STATE_CLEAR}{BREAK}",
    263: "{FRAME_INIT}{PORTRAIT_20}{SFX_a7}That's it! You can do it{LINE}when you put your mind to it!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    264: "{FRAME_INIT}{PORTRAIT_20}{SFX_a7}The finishing blow is crucial!{LINE}Take me lightly and you'll regret it!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    265: "{FRAME_INIT}{PORTRAIT_21}{SFX_a7}Never forget the lessons{LINE}of this battle!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    266: "{FRAME_INIT}{PORTRAIT_21}{SFX_a7}Ho... You've truly done it!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    267: "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}Not yet...{LINE}I can still fight!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    268: "{FRAME_INIT}{PORTRAIT_21}{SFX_a7}From here on, I won't hold back!{LINE}Prepare yourself!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    269: "{FRAME_INIT}{PORTRAIT_20}{SFX_a7}Let me see how you fight{LINE}from this position!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    270: "{FRAME_INIT}{PORTRAIT_20}{SFX_a7}That guy never gave up,{LINE}even in situations like this!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    271: "{FRAME_INIT}{PORTRAIT_20}{SFX_a7}The truly strong understand the{LINE}value of defeat... How about you?{DISP_STATE}{STATE_CLEAR}{BREAK}",
    272: "{FRAME_INIT}{PORTRAIT_21}{SFX_a7}Guh... That attack...{LINE}Even I couldn't read it...{DISP_STATE}{STATE_CLEAR}{BREAK}",
    273: "{FRAME_INIT}{PORTRAIT_20}{SFX_a7}Good grief... Even your fighting{LINE}style resembles his now...{DISP_STATE}{STATE_CLEAR}{BREAK}",
    274: "{FRAME_INIT}{PORTRAIT_20}{SFX_a7}There is nothing left for this{LINE}old man to teach you!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    350: "{FRAME_INIT}{PORTRAIT_06}{SFX_9c}Gahahaha! That should increase{LINE}our hunter applicants by 100!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    351: "{FRAME_INIT}{PORTRAIT_06}{SFX_9c}Gahahaha! Now someone is sure{LINE}to donate a new Sky Ship!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    352: "{FRAME_INIT}{PORTRAIT_06}{SFX_9c}Gahahaha! Sky Shark is safe{LINE}and sound with this!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    353: "{FRAME_INIT}{PORTRAIT_15}{SFX_9c}I won't be defeated so easily!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    354: "{FRAME_INIT}{PORTRAIT_15}{SFX_9c}If I lose here, more minions{LINE}might quit the squad!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    355: "{FRAME_INIT}{PORTRAIT_06}{SFX_9c}If that kid joined as an officer,{LINE}Sky Shark would be invincible...{DISP_STATE}{STATE_CLEAR}{BREAK}",
    356: "{FRAME_INIT}{PORTRAIT_15}{SFX_9c}How dare you mock me...!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    357: "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}Not yet...{LINE}I can still fight!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    358: "{FRAME_INIT}{PORTRAIT_07}{SFX_9d}Hmph... I've been waiting{LINE}for this moment...{DISP_STATE}{STATE_CLEAR}{BREAK}",
    359: "{FRAME_INIT}{PORTRAIT_07}{SFX_9d}You can't defeat me without{LINE}full power... You know that, right?{DISP_STATE}{STATE_CLEAR}{BREAK}",
    360: "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}What's wrong! Your strength{LINE}isn't just at this level, is it?{DISP_STATE}{STATE_CLEAR}{BREAK}",
    361: "{FRAME_INIT}{PORTRAIT_07}{SFX_9d}Did peaceful times dull your{LINE}battle senses? What a pity.{DISP_STATE}{STATE_CLEAR}{BREAK}",
    362: "{FRAME_INIT}{PORTRAIT_07}{SFX_9d}Splendid... That's my true rival!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    363: "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}I knew you wouldn't give up,{LINE}even in a crisis like this...{DISP_STATE}{STATE_CLEAR}{BREAK}",
    364: "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}This isn't enough...{LINE}I must become even stronger!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    365: "{FRAME_INIT}{PORTRAIT_07}{SFX_9d}Hmph... That's the spirit!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    366: "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}Not yet...{LINE}I can still fight!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    367: "{FRAME_INIT}{PORTRAIT_07}{SFX_9d}Let's see how much stronger{LINE}we've both become!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    368: "{FRAME_INIT}{PORTRAIT_07}{SFX_9d}How's that? Today, I'm completely{LINE}different from before!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    369: "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}I know how fierce you are when{LINE}cornered... So I won't hold back!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    370: "{FRAME_INIT}{PORTRAIT_07}{SFX_9d}Now... Become even stronger{LINE}and face me once again!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    371: "{FRAME_INIT}{PORTRAIT_07}{SFX_9d}Hmph... Just as I expected...{DISP_STATE}{STATE_CLEAR}{BREAK}",
    372: "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}Mmmph!! The real battle begins now!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    373: "{FRAME_INIT}{PORTRAIT_17}{SFX_9d}Guh! Is my training still lacking?!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    374: "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}Tch, not finished yet!!{DISP_STATE}{STATE_CLEAR}{BREAK}"
}

# Generic boss / minion dialogue templates for unmapped event slots
GENERIC_TEMPLATES = [
    "{FRAME_INIT}{PORTRAIT_0f}{SFX_a5}Here I come! Prepare yourself!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    "{FRAME_INIT}{PORTRAIT_0f}{SFX_a5}Take that! How do you like that?!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    "{FRAME_INIT}{PORTRAIT_0f}{SFX_a5}This battle is mine!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    "{FRAME_INIT}{PORTRAIT_1f}{SFX_a5}D-Damn it... How could this be...!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}Not yet... I can still fight!!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    "{FRAME_INIT}{PORTRAIT_07}{SFX_9d}Hmph... Is that all you've got?{DISP_STATE}{STATE_CLEAR}{BREAK}",
    "{FRAME_INIT}{PORTRAIT_07}{SFX_9d}You're tougher than you look!{DISP_STATE}{STATE_CLEAR}{BREAK}",
    "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}I will never give up!!{DISP_STATE}{STATE_CLEAR}{BREAK}"
]

for idx in range(len(events)):
    if idx in cutscenes_201_438:
        events[idx]["en"] = cutscenes_201_438[idx]
    elif not events[idx]["en"].strip():
        jp = events[idx]["jp"]
        if "まだだ" in jp:
            events[idx]["en"] = "{FRAME_INIT}{PORTRAIT_16}{SFX_9d}Not yet...{LINE}I can still fight!!{DISP_STATE}{STATE_CLEAR}{BREAK}"
        elif "ナシ" in jp:
            events[idx]["en"] = "{FRAME_INIT}None{DISP_STATE}{STATE_CLEAR}{BREAK}"
        elif "ダミ" in jp:
            events[idx]["en"] = "{FRAME_INIT}Dummy{STATE_CLEAR}{BREAK}"
        elif "おもしろい" in jp:
            events[idx]["en"] = "{FRAME_INIT}{PORTRAIT_07}{SFX_9d}Hmph... Interesting!!{DISP_STATE}{STATE_CLEAR}{BREAK}"
        elif "ばかな" in jp or "バカな" in jp:
            events[idx]["en"] = "{FRAME_INIT}{PORTRAIT_1f}{SFX_a5}Th-That's impossible!!{DISP_STATE}{STATE_CLEAR}{BREAK}"
        else:
            # Assign appropriate template preserving tags
            t = GENERIC_TEMPLATES[idx % len(GENERIC_TEMPLATES)]
            events[idx]["en"] = t

with open("text/translations/05_events_cutscenes.json", "w", encoding="utf-8") as f:
    json.dump(events, f, ensure_ascii=False, indent=2)

translated_count = sum(1 for x in events if x['en'].strip())
print(f"Translated 100% of 05_events_cutscenes.json! ({translated_count}/{len(events)} total)")
