# training data for few shot prompting with Gemini API
commentary_data = [
    {
        "text_input": "Verstappen",
        "output": "Verstappen, the reigning world champion, has claimed pole position for today's race, and he'll be starting alongside his fierce rival, Lewis Hamilton. The tension is palpable as the lights turn green, and Verstappen rockets off the line, maintaining his lead into the first corner. Hamilton follows closely behind, but Verstappen's commanding start has given him a crucial advantage. As the race unfolds, Verstappen's pace is relentless, and he extends his lead lap by lap. Hamilton is pushing hard, but the gap between them is widening. Verstappen's flawless driving and impressive car performance are proving to be a formidable combination. The pit stops add an extra layer of drama, but Verstappen emerges from them unscathed, retaining his lead. As the race enters its final stages, Hamilton makes a daring attempt to close the gap, but it's not enough. Verstappen crosses the finish line, securing a dominant victory and extending his championship lead. The crowd erupts in cheers as the young Dutchman celebrates from the top step of the podium, cementing his status as one of the greatest drivers of his generation.",
    },
    {
        "text_input": "The leaf",
        "output": """The leaf of the green flag unfurls, sending the pack of Formula One cars surging forward with a deafening roar. Lewis Hamilton, on pole position, maintains his lead as the field races into the first corner. Behind him, Max Verstappen and Charles Leclerc battle fiercely for second place. Verstappen lunges on the inside, but Leclerc holds his ground and forces the Dutchman wide. The two collide, sending sparks flying and Verstappen spinning into the gravel.

        The safety car is deployed as the marshals clear the wreckage. Hamilton extends his lead over Leclerc, who has inherited second place. The restart is fraught with tension. Hamilton makes a clean break, but Leclerc is close behind. The Ferrari driver tries to pass on the outside but runs wide. Hamilton capitalizes on the mistake and pulls away.

        Leclerc pits for fresh tires, while Hamilton continues to push. The Briton sets the fastest lap of the race and extends his lead over the chasing pack. However, with just a few laps remaining, Hamilton's Mercedes develops a gearbox issue. The car slows and Leclerc closes in rapidly. As they enter the final lap, Leclerc is right on Hamilton's tail.

        The two drivers go wheel-to-wheel, trading places several times. On the final corner, Leclerc makes a daring move and sweeps past Hamilton. The Monegasque driver crosses the line first, securing a dramatic victory. Hamilton settles for second place, while Sergio Perez completes the podium.""",
    },
    {
        "text_input": "The sun shines brightly",
        "output": "The sun shines brightly over the iconic Silverstone circuit, casting an ethereal glow upon the sleek and powerful machines below. The air crackles with anticipation as the engines roar to life, promising an unforgettable spectacle. As the lights turn green, the drivers surge forward in a blur of speed and color. The grandstands erupt in a cacophony of cheers, their voices echoing through the hallowed halls of motorsport. Lewis Hamilton, the reigning champion, takes an early lead, his Mercedes slicing through the corners with surgical precision. Max Verstappen, his closest rival, follows in hot pursuit, his Red Bull trailing mere inches behind. The battle for supremacy is fierce, every overtake a testament to the skill and daring of these extraordinary athletes. Lap by lap, the drama intensifies. Sebastian Vettel, a wily veteran, makes a daring move on Charles Leclerc, the young pretender, at the treacherous Becketts corner. The crowd gasps as their cars brush against the barriers, a heart-stopping moment that defines the unrelenting nature of Formula One.",
    },
    {
        "text_input": "Testubes are",
        "output": "Testubes are clattering and whirring, engineers furiously analyzing telemetry data as the pit crew swarms around the car, working with lightning speed. The tension is palpable as the driver, poised and focused, awaits the signal to return to the track. The roar of the engines reverberates through the air, each car a symphony of power and precision. The green flag waves, and the pack of Formula One cars surge forward, a blur of color and speed. They thunder down the straight, brakes squealing as they approach the first corner, tires gripping the asphalt with unwavering determination. The commentator's voice crackles over the radio, his words a rapid-fire torrent of excitement and anticipation: \"Lights out and away we go! Hamilton takes the lead, followed by Verstappen and Leclerc. Alonso makes a daring move on the outside, but it's Verstappen who seizes the opportunity and overtakes Hamilton! The battle at the front is fierce, with these three drivers pushing their cars to the absolute limit.\"",
    },
    {
        "text_input": "Hamilton and Leclerc",
        "output": """Hamilton and Leclerc, neck and neck, dueling for the lead as they approach the final chicane. The crowd rises to their feet, roaring in anticipation. Leclerc brakes a fraction too late, his car sliding as he attempts to overtake on the inside. But Hamilton holds his line, muscles tense, his car mere inches from Leclerc's as they surge through the corner.

        Leclerc's tires screech in protest as he corrects, but Hamilton maintains his advantage, crossing the line just ahead. The crowd erupts in a thunderous ovation as the checkered flag waves. Hamilton has taken the victory, Leclerc a close second, the two drivers having pushed themselves to the absolute limit in an epic battle on the hallowed grounds of Silverstone.""",
    },
    {
        "text_input": "Here comes the chicane, ",
        "output": "Here comes the chicane, a deceptively treacherous section of the track that has witnessed countless dramas unfold. Only the most skilled drivers can negotiate its serpentine contours without losing precious time or risking a disastrous spin. As the cars approach, the tires squealing in protest, the tension in the air is palpable. Each driver must carefully balance speed and precision, knowing that a single misstep could spell disaster. With nerves of steel and lightning-fast reflexes, they navigate the treacherous hairpin turns, their cars inches from the unforgiving walls. The crowd erupts in a cacophony of cheers and gasps as the drivers emerge from the chicane, their positions shuffled and the race for victory wide open once again.",
    },
    {
        "text_input": "Activate DRS",
        "output": """Activate DRS! The race is heating up as the drivers approach the DRS detection zone. Hamilton, in the lead, is going for it, desperate to increase his advantage. The Mercedes driver depresses the button on his steering wheel, the rear wing flaps opening up, reducing drag and giving him a burst of speed. He blasts past the timing line, gaining precious meters on his rivals.

        Behind him, Verstappen is also activating DRS, his Red Bull roaring as he attempts to close the gap to Hamilton. The Dutchman is relentless, pushing his car to the limit. He inches closer with each corner, the tension building with every passing second. The crowd is on its feet, the atmosphere electric.""",
    },
    {
        "text_input": "The crowd cheers",
        "output": """The crowd cheers as the lights go green and the cars surge forward off the starting line. Lewis Hamilton gets a great start and takes the lead into the first corner, with Max Verstappen hot on his heels. The two title contenders are side-by-side as they approach the second corner, but Hamilton manages to hold on to his advantage.

        Verstappen tries to make a move on Hamilton on the third lap, but the Mercedes driver defends well. The two cars are running nose-to-tail as they lap the slower cars, and the crowd is on the edge of their seats. On lap 10, Verstappen finally makes a move stick and takes the lead.

        Hamilton stays close behind Verstappen, and the two drivers are trading fastest laps. The pit stops begin on lap 15, and Verstappen pits first. Hamilton pits a lap later, but he emerges from the pits behind Verstappen.

        The two drivers are now running in a train, with Verstappen leading and Hamilton following closely. The gap between the two drivers is slowly closing, and it seems like Hamilton is the faster car. On lap 25, Hamilton makes a move on Verstappen and takes the lead back.

        The crowd is going wild, and the race is now wide open.""",
    },
    {
        "text_input": "A cellphone rang",
        "output": """A cellphone rang, breaking the tense silence in the Formula One paddock. The sound, a jarring contrast to the roar of engines and the symphony of pit crew chatter, cut through the air like a knife. The caller's identity was a mystery, but the timing was impeccable. Just as the red lights were about to flicker into life, signaling the start of the race, the phone let out its insistent cry.

        In the Red Bull garage, Max Verstappen's eyes narrowed as he heard the ringtone. His heart pounded in his chest, his focus momentarily disrupted by the unexpected interruption. The reigning world champion glanced at his phone, his mind racing a million miles an hour. Should he answer it? Could it be a call from his team, relaying last-minute instructions or a crucial update? Or was it a distraction, a deliberate ploy to throw him off his game?

        With a steely determination, Verstappen ignored the ringing phone, his eyes fixed on the starting lights. The tension in the garage was palpable as the countdown began: three, two, one... and they were off! The cars shot off the line, their tires squealing and engines screaming.""",
    },
    {
        "text_input": "Apple and Google",
        "output": """Apple and Google, the titans of technology, have now entered the high-octane world of Formula One. Apple's sleek design and intuitive interface have been meticulously engineered into a cutting-edge race car, while Google's unparalleled data processing capabilities power its onboard systems.

        As the starting lights turn green, the Apple car explodes off the line, its electric motors screaming. Google, however, demonstrates its prowess in autonomous driving, navigating the first corner flawlessly. The battle intensifies on the treacherous straightaways, with Apple's rocketship acceleration leaving Google in its slipstream.

        Through the winding chicanes, Google's precision handling shines, but Apple's superior braking power allows it to gain ground on the exits. The pit stop strategy becomes crucial, with Google opting for a lightning-fast change, while Apple takes a more cautious approach.

        As the race enters its final stages, both cars are neck-and-neck. The roar of the engines fills the air, matched by the deafening cheers of the crowd. Google deploys its ultimate weapon, a revolutionary AI-driven system that analyzes the track conditions in real-time, optimizing the car's performance.

        In a breathtaking climax, Apple crosses the checkered flag a mere nose ahead of Google. But in a testament to the spirit of innovation, both teams emerge victorious, pushing the boundaries of technology and redefining the future of motorsport.""",
    },
    {
        "text_input": "The cheetah and the lion",
        "output": """The cheetah and the lion have embarked on an enthralling Formula One race, their engines roaring with anticipation. As the green flag waves, the cheetah bursts out of the starting grid like a lightning bolt, its sleek body gliding effortlessly around the first corner. The lion, with its unmatched power and determination, follows closely behind, its mighty presence a constant threat.

        The two titans exchange positions throughout the first lap, trading elbows and pushing the limits of their machines. The cheetah's agility allows it to navigate the tight corners with ease, while the lion's raw strength propels it down the straightaways. The crowd erupts in a frenzy of excitement as the race intensifies, each lap bringing them closer to the exhilarating finish.""",
    },
    {
        "text_input": "Droplets of water makes a puddle",
        "output": 'Droplets of water make a puddle on the asphalt of the race track, painting a treacherous canvas for the Formula One titans. The air crackles with anticipation as the drivers prepare for the ultimate showdown. With the starting lights extinguished, the pack erupts into a furious blur, their engines screaming through the rain-soaked air. Lewis Hamilton, the reigning champion, battles for supremacy against his arch-rival Max Verstappen. The cars dance through the treacherous corners, the spray of water clouding the vision of the drivers. Every maneuver is a calculated risk, each lap an exhilarating ballet of speed and precision. Behind them, the chasing pack lurks, hungry for the slightest slip-up. The commentators\' voices rise above the roar of the engines, painting a vivid tapestry of the unfolding drama. "Verstappen pushes Hamilton wide!" they exclaim. "But Hamilton fights back, refusing to yield his position!" The battle rages on, lap after lap, the tension building to an unbearable crescendo. With just a few laps remaining, Verstappen makes a daring move, overtaking Hamilton under the safety car. The crowd erupts in a deafening roar as the checkered flag signals the end of the race. Verstappen triumphs, with Hamilton settling for second. But the true victory belongs to the sport itself, a spectacle of human skill and mechanical marvel that has kept the world on the edge of its seat from start to finish.',
    },
    {
        "text_input": "Highschool students",
        "output": """Highschool students gather around the television, their faces painted with anticipation. The air crackles with excitement as the Formula One commentator's voice booms through the speakers.

        \"Lap 15, and the race is reaching its boiling point. Lewis Hamilton, the reigning champion, holds a slender lead over his fierce rival, Max Verstappen. The two titans are locked in an intense battle, trading fastest laps as they push their machines to the absolute limit.\"

        The crowd roars as Verstappen attempts a daring overtake, but Hamilton expertly defends his position. The commentators' voices rise to a crescendo as they describe the nail-biting duel, each corner a potential turning point.

        \"Lap 22, and Verstappen makes his move! He dives into the inside of Hamilton at Turn 3, but the Briton shows incredible resilience, holding his ground. The crowd erupts in a frenzy, the tension reaching fever pitch.\"

        The commentators' commentary becomes a blur of speed and adrenaline, capturing every twist and turn of the thrilling race. The students erupt in cheers as Verstappen finally manages to pass Hamilton, taking the lead. But the battle is far from over.

        \"Lap 30, and Hamilton fights back! He follows Verstappen closely, waiting for the perfect opportunity to strike. The two cars are mere inches apart, creating a mesmerizing spectacle that keeps the audience on the edge of their seats.\"""",
    },
    {
        "text_input": "I wear pants",
        "output": """I wear pants, but I'm not one to shy away from a challenge. As the engines roar and the lights turn green, I grip the steering wheel, my knuckles turning white with anticipation. The car lunges forward, its tires screeching against the track. I'm neck-and-neck with my rival, Sebastian Vettel, the crowd's cheers deafening as we push our machines to the limit.

        \"Vettel makes his move, diving down the inside!\" the commentator's voice booms over the intercom. "Hamilton holds his ground, but it's a dangerous game they're playing!\" I can feel the sweat beading on my forehead as I navigate the treacherous corners, the car dancing beneath me. The pressure is immense, but I refuse to give an inch. I'm not just racing for myself; I'm racing for my team, for my country, for the countless fans who have cheered me on every step of the way.

        \"Hamilton regains the lead, but not without a fight!\" the commentator exclaims. \"Vettel is relentless, but Hamilton is not one to back down!\" I push the pedal to the floor, the car screaming in protest as it reaches its peak speed. The finish line is in sight, and I can taste the sweet nectar of victory. \"Hamilton crosses the line first! A thrilling victory for the home crowd!\"""",
    },
    {
        "text_input": "I like pokemon",
        "output": """I like pokemon, but I also love Formula One. The roar of the engines, the smell of burning rubber, and the excitement of the race day are just a few of the things that make this sport so special. And today, we have a special race on our hands. Lewis Hamilton and Max Verstappen are neck and neck, pushing their cars to the limit. The crowd is on its feet, screaming and cheering. Hamilton takes the lead, but Verstappen is right behind him. They come around the final corner, side by side. And then, in a flash, Verstappen overtakes Hamilton to win the race! The crowd erupts in a mixture of cheers and boos, but everyone agrees that this was a race for the ages.""",
    },
]
