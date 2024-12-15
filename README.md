# Create Songs with LoveAIAPI Suno API

## Get API Key

https://loveaiapi.com/app/key-management

Get your API key from the LoveAIAPI website. Set it in the `configs.py` file.

## Create Song

```bash
python create_song.py
```

Output received:

```
loveaiapi-suno-api % python create_song.py 
Creating song...
{'task_id': 'b2658c16-fe01-4214-bfd1-222e01db43b4'}

Checking task status...
{
    "task_id": "b2658c16-fe01-4214-bfd1-222e01db43b4",
    "task_model": "suno",
    "cost_points": 10.0,
    "input_data": {
        "style": "",
        "title": "",
        "custom": false,
        "prompt": "A happy and uplifting pop song",
        "task_id": "b2658c16-fe01-4214-bfd1-222e01db43b4",
        "metadata": {
            "auto_suno_task_id": "0c1f0293-1d3d-4fde-839e-2e44fe887e83"
        },
        "callback_url": "https://example.com/webhook/?some_thing_your_need=xxx",
        "instrumental": false
    },
    "output_data": {
        "msg": "Running... ",
        "code": 200,
        "data": [
            {
                "id": "a02d2a76-d535-4605-a115-da81a3c590c9",
                "tags": "happy, uplifting, bright, pop",
                "title": "Sunny Days",
                "prompt": "[Verse]\nWoke up this morning with a smile on my face\nSunlight is dancing all over the place\nThe world is spinning it's a brand new day\nHeart's full of laughter come what may\n\n[Verse 2]\nBirds are singing just for you and me\nClouds are waving like they’re meant to be\nFriends are calling let's go take a ride\nWith open hearts let’s forget the guide\n\n[Chorus]\nThese sunny days just take my breath away\nLet's make some memories no need to delay\nHand in hand we'll chase the sky so blue\nIn this moment it's just me and you\n\n[Verse 3]\nEvery step we take feels so light and free\nSmiling faces everywhere we see\nKites are soaring like our dreams so high\nReaching out gotta touch the sky\n\n[Bridge]\nLife is brighter when we’re side by side\nThrough every low and every high\nNothing’s too big nothing's too small\nTogether we can conquer all\n\n[Chorus]\nThese sunny days just take my breath away\nLet's make some memories no need to delay\nHand in hand we'll chase the sky so blue\nIn this moment it's just me and you",
                "status": "streaming",
                "duration": null,
                "audio_url": "",
                "image_url": "https://cdn1.suno.ai/image_a02d2a76-d535-4605-a115-da81a3c590c9.jpeg",
                "createTime": "2024-12-15T04:09:45.759Z",
                "model_name": "v4",
                "error_message": null,
                "gpt_description_prompt": "A happy and uplifting pop song"
            },
            {
                "id": "f81a839d-09fc-48e5-902e-c798428d3b56",
                "tags": "happy, uplifting, bright, pop",
                "title": "Sunny Days",
                "prompt": "[Verse]\nWoke up this morning with a smile on my face\nSunlight is dancing all over the place\nThe world is spinning it's a brand new day\nHeart's full of laughter come what may\n\n[Verse 2]\nBirds are singing just for you and me\nClouds are waving like they’re meant to be\nFriends are calling let's go take a ride\nWith open hearts let’s forget the guide\n\n[Chorus]\nThese sunny days just take my breath away\nLet's make some memories no need to delay\nHand in hand we'll chase the sky so blue\nIn this moment it's just me and you\n\n[Verse 3]\nEvery step we take feels so light and free\nSmiling faces everywhere we see\nKites are soaring like our dreams so high\nReaching out gotta touch the sky\n\n[Bridge]\nLife is brighter when we’re side by side\nThrough every low and every high\nNothing’s too big nothing's too small\nTogether we can conquer all\n\n[Chorus]\nThese sunny days just take my breath away\nLet's make some memories no need to delay\nHand in hand we'll chase the sky so blue\nIn this moment it's just me and you",
                "status": "streaming",
                "duration": null,
                "audio_url": "",
                "image_url": "https://cdn1.suno.ai/image_f81a839d-09fc-48e5-902e-c798428d3b56.jpeg",
                "createTime": "2024-12-15T04:09:45.759Z",
                "model_name": "v4",
                "error_message": null,
                "gpt_description_prompt": "A happy and uplifting pop song"
            }
        ],
        "callbackType": "text"
    }
}
```


## Extend Song

```bash
python extend_song.py
```

Output received:

```
loveaiapi-suno-api % python extend_song.py 
{'task_id': '4ae8f281-e363-4e04-98be-b6b22376d862'}

Checking task status...
{'task_id': '4ae8f281-e363-4e04-98be-b6b22376d862', 'task_model': 'suno', 'cost_points': 10.0, 'input_data': {'style': 'pop', 'title': 'Extend Song Title', 'prompt': 'Extend Song Description', 'task_id': '4ae8f281-e363-4e04-98be-b6b22376d862', 'audio_id': 'a7fddd29-47dd-4d8c-843c-c718ffde570d', 'metadata': {'audio_id': 'a7fddd29-47dd-4d8c-843c-c718ffde570d', 'continue_at': 60}, 'continue_at': 60, 'callback_url': 'https://example.com/webhook'}, 'output_data': {'msg': 'Running... ', 'code': 200, 'data': [{'id': '546425e5-aa6c-40c7-9de9-d675f35cb181', 'tags': 'pop', 'title': 'Extend Song Title', 'prompt': 'Extend Song Description', 'status': 'submitted', 'duration': None, 'audio_url': '', 'image_url': None, 'createTime': '2024-12-15T03:58:24.617Z', 'model_name': 'v4', 'error_message': None, 'gpt_description_prompt': None}, {'id': '008cd40b-9734-4c0f-8e89-439c6bcd6a20', 'tags': 'pop', 'title': 'Extend Song Title', 'prompt': 'Extend Song Description', 'status': 'submitted', 'duration': None, 'audio_url': '', 'image_url': None, 'createTime': '2024-12-15T03:58:24.617Z', 'model_name': 'v4', 'error_message': None, 'gpt_description_prompt': None}], 'callbackType': 'text'}}
```

## Concat Song

```bash
python concat_song.py
```

Output received:

```
loveaiapi-suno-api % python concat_song.py 
{'task_id': '75494bca-85ce-4b42-9747-cc09ac2f874e'}

Checking task status...
{'task_id': '75494bca-85ce-4b42-9747-cc09ac2f874e', 'task_model': 'suno', 'cost_points': 5.0, 'input_data': {'task_id': '75494bca-85ce-4b42-9747-cc09ac2f874e', 'audio_id': '546425e5-aa6c-40c7-9de9-d675f35cb181', 'metadata': {'clip_id': '546425e5-aa6c-40c7-9de9-d675f35cb181'}, 'callback_url': 'https://example.com/webhook'}, 'output_data': {'msg': 'Running... ', 'code': 200, 'data': [{'id': '242bf86a-dcdc-47d0-8f58-b32f2b873b7e', 'tags': '90s gangster rap, smooth flow, tupac, dre, singing chorus, 808s, strings, piano, Dre, tupac, trap', 'title': 'Vladdy Z', 'prompt': '(Chorus)\nYa’ll don’t know AZ, like we do\nworkin’ for a dictator, yeah it’s true\n“Dawg, it’s 80 and sunny, lets leave in a few”\nNaw man, AZ Hillary lookin’ right at you\n…\n“Please sire! Another Wheel spin?”\nEh!\n\n\n(Verse 1)\nShid, that AZ, or Vladdy P?\nA Russian, Italian stallion,\nSo why’s he got a Polish name ending in skii?\nThe text message Tsar, bomba\nAsk Christoffison Lark,\nHe’ll reply with his mantra, \n“yeah, babe, hundy-p”\nStick tap to the nut sack,\nIf ya’ll don’t respond to those textie texts,\nMa fuckin’  Text Meyer, \nLark meyer\nYa can’t fire\nStock-meyer,\nthe fire starter…\nTee-meyer,\nChristine meyer,\nOur HOUSE is,\nOn fire, \nSo,\nplease a-spire,\nTo close up that case,\nOr comrade’ll give chase\nand ya’ll will NEVER escape\nI mean look at his shape,\nHe’s built for SPEED! \nThe Russian Italian STEED!\nAnd the ma’ fucka lookin’ to FEED!\nRun you down in some Hey Dudes,\nAnd a high performance, wicking, Callaway, golf T\nAin’t no regular YT\nYou shall see,\nThe Kremlin resemblin’\nAn adrenalin fueled gremlin,\nUp in your Slack D-M’s,\nwhile hummin’ communist an-thems,\nSo don’t get a text while you’re clocked out\nWait, is it clock in or clock out?\nI’m try-na find out,\nThis meeting was only posta be 30\nSee, we not tryna be dirty,\nOnly D-T-R-T ,\n but the rules be all murk-y\nYa’lll want me to trust dis ma’ fucka, \ndat don’t even like turk-ey?\nListen, this meeting still goin’, we at an hour and 5, \nmeanwhile Vladdy going into my drive\nHe’s messin round with my e-val\nHe’s tryin’ to conceal\nHis Kremlin intentions, cause I didn’t clock in when,\naww shit, just got another slack mention…\n\n\n\n(Chorus)\nYa’ll don’t know AZ, like we do\nworkin’ for a dictator, yeah it’s true\n“Dawg, it’s 80 and sunny, lets leave in a few”\nNaw man, AZ Hillary lookin’ right at you\n…\n“Please sire! Another Wheel spin?”\nEh!\n\n\nAnd what’s a Russian got against jarred sauce?\nMa’ fucka should be happy just ta,\nget a break from Moscow’s beef stroganoff, \nSo quit showin’ off \nwith pretentious and haughty scoffs,\n\nwe bout to show up to your place,\nwith Ragu by the case,\nand some, \nBertolli covered in ravioli,\nAnd possibly Classico on stromboli, or Rao’s for Fusilli,\nI suggest you don’t test me, cause this will get messy\nWe’ll even stoop to some Newmans Own,\nNot talkin about Eric or Jerry’s neighbor he meats with a groan,\nBut that ma’a fucka coss playin’ his little clone\nOn every bottle or jar, from salad dressing to Pomadone\nAnd listen man, \ncutting corners on food isn’t something that I condone, \nbut the only real food comes off of a bone,\nand I’d like to atone,\nbut I’m not tryna waste,\nmy time,\nworryin’ about the state of tomato paste,\nconsidering Vladdy is only tryna save face\nwhen we know the real disgrace,\nma’ fucka over here watching “love is blind”,\nmust be out of his mind,\nthat’s a show for teen girls,\nor middle-aged divorcee’s puttin’ their hair in curls,\nI simply wouldn’t expect,\nA dictator to select,\nA show men completely reject\nBut hey, \nthat’s the Benign Violation Effect\n\n\n\n(Chorus)\nYa’ll don’t\n\nExtend Song Description', 'status': 'streaming', 'duration': None, 'audio_url': None, 'image_url': 'https://cdn1.suno.ai/image_546425e5-aa6c-40c7-9de9-d675f35cb181.jpeg', 'createTime': '2024-12-15T04:02:08.690Z', 'model_name': 'v4', 'concat_history': [{'id': 'a7fddd29-47dd-4d8c-843c-c718ffde570d', 'type': 'gen', 'infill': False, 'source': 'web', 'continue_at': 60.0}, {'id': '546425e5-aa6c-40c7-9de9-d675f35cb181'}]}], 'callbackType': 'text'}}
```