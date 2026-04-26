local pcall = GLOBAL.pcall
local require = GLOBAL.require
local print = GLOBAL.print
local pairs = GLOBAL.pairs
local ipairs = GLOBAL.ipairs
local tostring = GLOBAL.tostring
local type = GLOBAL.type
local string = GLOBAL.string

local PO_PATH = MODROOT .. "languages/turkish.po"
local LANG_CODE = "tr"
local CHARACTERS = {
    "WILSON", "WILLOW", "WOLFGANG", "WENDY", "WX78", "WICKERBOTTOM",
    "WOODIE", "WAXWELL", "WATHGRITHR", "WEBBER", "WINONA", "WARLY",
    "WORMWOOD", "WORTOX", "WURT", "WALTER", "WANDA",
}

local function debug_print(msg)
    if GetModConfigData("debug_log") then
        print("[TR Yama] " .. tostring(msg))
    end
end

local function MergeMaps(t1, t2)
    if type(t1) ~= "table" or type(t2) ~= "table" then return end
    for k, v in pairs(t2) do
        if type(v) == "table" and type(t1[k]) == "table" then
            MergeMaps(t1[k], v)
        else
            t1[k] = v
        end
    end
end

local function ApplyTranslations()
    local Translator = GLOBAL.LanguageTranslator
    if Translator and Translator.LoadPOFile then
        Translator:LoadPOFile(PO_PATH, LANG_CODE)
        debug_print("PO yüklendi: " .. PO_PATH)
    else
        debug_print("UYARI: LanguageTranslator bulunamadı")
    end

    if GetModConfigData("speech_overrides") and GLOBAL.STRINGS and GLOBAL.STRINGS.CHARACTERS then
        for _, char in ipairs(CHARACTERS) do
            local module_path = "speech_overrides/speech_" .. string.lower(char) .. "_tr"
            local ok, tr_table = pcall(require, module_path)
            if ok and type(tr_table) == "table" and GLOBAL.STRINGS.CHARACTERS[char] then
                MergeMaps(GLOBAL.STRINGS.CHARACTERS[char], tr_table)
                debug_print("Speech merge: " .. char)
            end
        end
    end
end

ApplyTranslations()

AddSimPostInit(function()
    debug_print("AddSimPostInit — shard load, çeviri yeniden uygulanıyor")
    ApplyTranslations()
end)

AddPlayerPostInit(function(inst)
    debug_print("AddPlayerPostInit — oyuncu spawn, çeviri yeniden uygulanıyor")
    ApplyTranslations()
end)
