import random

# Dictionary of kaomoji (text-based emoticon) categories
EMOJI_CATEGORIES = {
    "cute": ["(✿◠‿◠)", "ʕ•ᴥ•ʔ", "(•◡•)", "(｡◕‿◕｡)", "(*≧ω≦)", "(◕‿◕✿)", "♡(◡‿◡✿)", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧", "(●´ω｀●)", "≧◡≦", "(づ｡◕‿‿◕｡)づ", "ヽ(o＾▽＾o)ノ", "ヾ(☆◡☆)ノ", "(✿╹◡╹)", "(◠﹏◠✿)"],
    "cuddly": ["(づ￣ ³￣)づ", "(つ≧▽≦)つ", "(づ｡◕‿‿◕｡)づ", "(⊃｡•́‿•̀｡)⊃", "ʕっ•ᴥ•ʔっ", "⊂(◉‿◉)つ", "⊂((・▽・))⊃", "(っ^_^)っ", "＼(^o^)／", "(づ￣ ³￣)づ", "⊂(・﹏・⊂)", "(>^_^)>", "(つ▀¯▀)つ", "〆(・∀・＠)", "⊂（♡⌂♡）⊃"],
    "sleepy": ["(￣o￣) zzZZzzZZ", "(-.-)Zzz...", "(∪｡∪)｡｡｡zzZ", "(≧ω≦)zzz", "☆⌒ヽ(･_･)ゝ", "(҂⌣̀_⌣́)", "(-_-) zzz", "(＿　＿*) Z z z", "(*´～｀*)", "【:εО⊂】", "*<:0)_( ̄0 ̄)zz", "(¬᷄-¬᷅)", "(-_-)ρ゜zｚ", "( ु⁎ᴗ_ᴗ⁎)ु.｡oO", "(:3_ヽ)_"],
    "fluffy": ["(´• ω •`)", "ʕ·ᴥ·ʔ", "ʕᵔᴥᵔʔ", "ʕ•ᴥ•ʔ", "(=^･ω･^=)", "꒰^･ิ_･ิ^꒱", "(≡•̀ㅂ•́)و", "=^._.^= ∫", "(/・・)ノ", "(´･ω･`)", "(ﾉ≧∀≦)ﾉ", "~(=^‥^)_旦~", "(*^.^*)", "ヾ(・ω・)メ", "(｡･ω･｡)"],
    "flutter": ["ヾ(◍'౪`◍)ﾉﾞ♡", "♪(´ε｀ )", "(ﾉ≧∀≦)ﾉ ‥…━━━★", "ヾ(・ω・)ノ", "(ノ・∀・)ノ", "⸜(* ॑꒳ ॑* )⸝", "✧*。ヾ(｡>﹏<｡)ﾉﾞ✧*。", "ヾ(＾∇＾)", "ヾ(☆▽☆)", "(´｡• ᵕ •｡`)", "ヽ(*・ω・)ﾉ", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧", "ヾ(〃^∇^)ﾉ", "╰(*°▽°*)╯", "(ノ°∀°)ノ⌒･*:.｡. .｡.:*･゜ﾟ･*☆"],
    "shy": ["(⁄ ⁄•⁄ω⁄•⁄ ⁄)", "(⁄ ⁄>⁄ ▽ ⁄<⁄ ⁄)", "(≧﹏≦)", "(〃ω〃)", "(⁄ ⁄^⁄ᗨ⁄^⁄ ⁄)", "(//ω//)", "(｡•́︿•̀｡)", "(/へ＼*)", "(*ﾉωﾉ)", "(/∇＼*)", "(⁄ ⁄•⁄_⁄•⁄ ⁄)⁄", "(；⌣̀_⌣́)", "｡(*^▽^*)ゞ", "(〃▽〃)", "(〃ー〃)"],
    "happy": ["(≧∇≦)/", "( ´ ▽ ` )", "ヽ(・∀・)ﾉ", "(≧◡≦)", "(o˘◡˘o)", "(*≧▽≦)", "(●⌒∇⌒●)", "(─‿‿─)", "(*^‿^*)", "(◕‿◕)", "(*≧∀≦*)", "(￣▽￣)", "(⌒▽⌒)☆", "〜(꒪꒳꒪)〜", "(★^O^★)"],
    "sad": ["(´；ω；`)", "(´;︵;`)", "｡･ﾟﾟ*(>д<)*ﾟﾟ･｡", "(T_T)", "( ; ω ; )", "(╥_╥)", "(⋟﹏⋞)", "(ToT)", "(┬┬﹏┬┬)", "(◞‸◟；)", "(ノ_<。)", "(-_-｡)", "(μ_μ)", "(┯_┯)", "(≖͞_≖̥)"],
    "excited": ["((o(^∇^)o))", "o(≧∇≦o)", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧", "ヽ(゜∇゜)ノ", "(*≧∀≦*)", "(*^▽^*)", "(☆▽☆)", "(/^▽^)/", "(/◕ヮ◕)/", "(ﾉ´ヮ`)ﾉ*: ･ﾟ", "（*＾-＾*）", "ヽ(;^o^ヽ)", "(ﾉﾟ0ﾟ)ﾉ~", "o(* ̄▽ ̄*)ブ", "(＾◡＾)"],
    "angry": ["(＃`Д´)", "(`皿´＃)", "( ` ω ´ )", "(｀Д´)", "ヽ( `д´*)ノ", "(・`ω´・)", "(`ー´)", "ヽ(≧Д≦)ノ", "(>_<)", "(╬ಠ益ಠ)", "٩(╬ʘ益ʘ╬)۶", "(ノಠ益ಠ)ノ", "(ﾒ` ﾛ ´)", "┌∩┐(◣_◢)┌∩┐", "凸ಠ益ಠ)凸"],
    "surprised": ["(⊙_⊙)", "（゜◇゜）", "（￣□￣；）", "(´⊙ω⊙`)", "°o°", "(ʘ_ʘ)", "(ʘ_ʘ;)", "(ꗞ_ꗞ)", "(；⌣̀_⌣́)", "(●__●)", "(☉_☉)", "(⊙.☉)7", "(ﾟДﾟ;)", "щ(゜ロ゜щ)", "Σ(°ロ°)"],
    "love": ["(｡♥‿♥｡)", "(◍•ᴗ•◍)❤", "♡( ◡‿◡ )", "(≧◡≦) ♡", "( ´ ▽ ` ).｡ｏ♡", "♡( ◡‿◡ )", "♡ ～('▽^人)", "(｡･ω･｡)ﾉ♡", "(◕‿◕)♡", "( ˘ ³˘)♥", "(´｡• ᵕ •｡`) ♡", "♥(´∀`●)", "ლ(́◉◞౪◟◉‵ლ)", "(♡˙︶˙♡)", "( ˘ ³˘)❤"]
}

# Description for each kaomoji category
CATEGORY_DESCRIPTIONS = {
    "cute": "Adorable and charming text faces",
    "cuddly": "Soft, sweet, and hugging text faces",
    "sleepy": "Tired and dozing off text faces",
    "fluffy": "Soft and gentle text faces",
    "flutter": "Excited and fluttery text faces",
    "shy": "Bashful and timid text faces",
    "happy": "Joyful and cheerful text faces",
    "sad": "Unhappy and tearful text faces",
    "excited": "Enthusiastic and eager text faces",
    "angry": "Upset and furious text faces",
    "surprised": "Astonished and shocked text faces", 
    "love": "Romantic and affectionate text faces"
}

def generate_emojis(category, count=10):
    """Generate emojis based on category and count"""
    if category == "random":
        # Choose a random category
        category = random.choice(list(EMOJI_CATEGORIES.keys()))
    
    # Get the list of emojis for the category
    if category in EMOJI_CATEGORIES:
        emoji_list = EMOJI_CATEGORIES[category]
        # Ensure we don't exceed the available emojis
        count = min(count, len(emoji_list))
        # Select random emojis from the category
        selected_emojis = random.sample(emoji_list, count)
        return selected_emojis
    else:
        # If category not found, return some default kaomojis
        default_emojis = ["(●'◡'●)", "(◕‿◕)", "( ͡° ͜ʖ ͡°)", "＼(＾▽＾)／", "(＾▽＾)", "(・∀・)", "(^_^)", "^_^", "^.^", "(•‿•)"]
        return random.sample(default_emojis, min(count, 10))

def get_emoji_description(emoji_char):
    """Get description for a kaomoji"""
    # Try to find which category the kaomoji belongs to
    for category, emoji_list in EMOJI_CATEGORIES.items():
        if emoji_char in emoji_list:
            return f"{category.capitalize()} kaomoji: {CATEGORY_DESCRIPTIONS.get(category, '')}"
    
    # If not found in our categories
    return "Unknown kaomoji"
