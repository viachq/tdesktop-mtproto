"""
Auto-generated TL schema from Telegram API schema (api.tl).
DO NOT EDIT — regenerate with tools/generate_code.py
"""

TYPES = {
    "AccountDaysTTL": {
        "accountDaysTTL": 0xb8d0afdf,
    },
    "AiComposeTone": {
        "aiComposeTone": 0xcff63ea9,
        "aiComposeToneDefault": 0x9bad6414,
    },
    "AiComposeToneExample": {
        "aiComposeToneExample": 0xf1d628ec,
    },
    "AttachMenuBot": {
        "attachMenuBot": 0xd90d8dfe,
    },
    "AttachMenuBotIcon": {
        "attachMenuBotIcon": 0xb2a7386b,
    },
    "AttachMenuBotIconColor": {
        "attachMenuBotIconColor": 0x4576f3f0,
    },
    "AttachMenuBots": {
        "attachMenuBotsNotModified": 0xf1d88a5c,
        "attachMenuBots": 0x3c4301c0,
    },
    "AttachMenuBotsBot": {
        "attachMenuBotsBot": 0x93bf667f,
    },
    "AttachMenuPeerType": {
        "attachMenuPeerTypeSameBotPM": 0x7d6be90e,
        "attachMenuPeerTypeBotPM": 0xc32bfa1a,
        "attachMenuPeerTypePM": 0xf146d31f,
        "attachMenuPeerTypeChat": 0x509113f,
        "attachMenuPeerTypeBroadcast": 0x7bfbdefc,
    },
    "AuctionBidLevel": {
        "auctionBidLevel": 0x310240cc,
    },
    "Authorization": {
        "authorization": 0xad01d61d,
    },
    "AutoDownloadSettings": {
        "autoDownloadSettings": 0xbaa57628,
    },
    "AutoSaveException": {
        "autoSaveException": 0x81602d47,
    },
    "AutoSaveSettings": {
        "autoSaveSettings": 0xc84834ce,
    },
    "AvailableEffect": {
        "availableEffect": 0x93c3e27e,
    },
    "AvailableReaction": {
        "availableReaction": 0xc077ec01,
    },
    "BankCardOpenUrl": {
        "bankCardOpenUrl": 0xf568028a,
    },
    "BaseTheme": {
        "baseThemeClassic": 0xc3a12462,
        "baseThemeDay": 0xfbd81688,
        "baseThemeNight": 0xb7b31ea8,
        "baseThemeTinted": 0x6d5f77ee,
        "baseThemeArctic": 0x5b11125a,
    },
    "Birthday": {
        "birthday": 0x6c8e1e06,
    },
    "Bool": {
        "boolFalse": 0xbc799737,
        "boolTrue": 0x997275b5,
    },
    "Boost": {
        "boost": 0x4b3e14d6,
    },
    "BotApp": {
        "botAppNotModified": 0x5da674b7,
        "botApp": 0x95fcd1d6,
    },
    "BotAppSettings": {
        "botAppSettings": 0xc99b1950,
    },
    "BotBusinessConnection": {
        "botBusinessConnection": 0x8f34b2f5,
    },
    "BotCommand": {
        "botCommand": 0xc27ac8c7,
    },
    "BotCommandScope": {
        "botCommandScopeDefault": 0x2f6cb2ab,
        "botCommandScopeUsers": 0x3c4f04d8,
        "botCommandScopeChats": 0x6fe1a881,
        "botCommandScopeChatAdmins": 0xb9aa606a,
        "botCommandScopePeer": 0xdb9d897d,
        "botCommandScopePeerAdmins": 0x3fd863d1,
        "botCommandScopePeerUser": 0xa1321f3,
    },
    "BotInfo": {
        "botInfo": 0x4d8a0299,
    },
    "BotInlineMessage": {
        "botInlineMessageMediaAuto": 0x764cf810,
        "botInlineMessageText": 0x8c7f65e2,
        "botInlineMessageMediaGeo": 0x51846fd,
        "botInlineMessageMediaVenue": 0x8a86659c,
        "botInlineMessageMediaContact": 0x18d1cdc2,
        "botInlineMessageMediaInvoice": 0x354a9b09,
        "botInlineMessageMediaWebPage": 0x809ad9a6,
        "botInlineMessageRichMessage": 0xa617e7b,
    },
    "BotInlineResult": {
        "botInlineResult": 0x11965f3a,
        "botInlineMediaResult": 0x17db940b,
    },
    "BotMenuButton": {
        "botMenuButtonDefault": 0x7533a588,
        "botMenuButtonCommands": 0x4258c205,
        "botMenuButton": 0xc7b57ce6,
    },
    "BotPreviewMedia": {
        "botPreviewMedia": 0x23e91ba3,
    },
    "BotVerification": {
        "botVerification": 0xf93cd45c,
    },
    "BotVerifierSettings": {
        "botVerifierSettings": 0xb0cd6617,
    },
    "BusinessAwayMessage": {
        "businessAwayMessage": 0xef156a5c,
    },
    "BusinessAwayMessageSchedule": {
        "businessAwayMessageScheduleAlways": 0xc9b9e2b9,
        "businessAwayMessageScheduleOutsideWorkHours": 0xc3f2f501,
        "businessAwayMessageScheduleCustom": 0xcc4d9ecc,
    },
    "BusinessBotRecipients": {
        "businessBotRecipients": 0xb88cf373,
    },
    "BusinessBotRights": {
        "businessBotRights": 0xa0624cf7,
    },
    "BusinessChatLink": {
        "businessChatLink": 0xb4ae666f,
    },
    "BusinessGreetingMessage": {
        "businessGreetingMessage": 0xe519abab,
    },
    "BusinessIntro": {
        "businessIntro": 0x5a0a066d,
    },
    "BusinessLocation": {
        "businessLocation": 0xac5c1af7,
    },
    "BusinessRecipients": {
        "businessRecipients": 0x21108ff7,
    },
    "BusinessWeeklyOpen": {
        "businessWeeklyOpen": 0x120b1ab9,
    },
    "BusinessWorkHours": {
        "businessWorkHours": 0x8c92b098,
    },
    "CdnConfig": {
        "cdnConfig": 0x5725e40a,
    },
    "CdnPublicKey": {
        "cdnPublicKey": 0xc982eaba,
    },
    "ChannelAdminLogEvent": {
        "channelAdminLogEvent": 0x1fad68cd,
    },
    "ChannelAdminLogEventAction": {
        "channelAdminLogEventActionChangeTitle": 0xe6dfb825,
        "channelAdminLogEventActionChangeAbout": 0x55188a2e,
        "channelAdminLogEventActionChangeUsername": 0x6a4afc38,
        "channelAdminLogEventActionChangePhoto": 0x434bd2af,
        "channelAdminLogEventActionToggleInvites": 0x1b7907ae,
        "channelAdminLogEventActionToggleSignatures": 0x26ae0971,
        "channelAdminLogEventActionUpdatePinned": 0xe9e82c18,
        "channelAdminLogEventActionEditMessage": 0x709b2405,
        "channelAdminLogEventActionDeleteMessage": 0x42e047bb,
        "channelAdminLogEventActionParticipantJoin": 0x183040d3,
        "channelAdminLogEventActionParticipantLeave": 0xf89777f2,
        "channelAdminLogEventActionParticipantInvite": 0xe31c34d8,
        "channelAdminLogEventActionParticipantToggleBan": 0xe6d83d7e,
        "channelAdminLogEventActionParticipantToggleAdmin": 0xd5676710,
        "channelAdminLogEventActionChangeStickerSet": 0xb1c3caa7,
        "channelAdminLogEventActionTogglePreHistoryHidden": 0x5f5c95f1,
        "channelAdminLogEventActionDefaultBannedRights": 0x2df5fc0a,
        "channelAdminLogEventActionStopPoll": 0x8f079643,
        "channelAdminLogEventActionChangeLinkedChat": 0x50c7ac8,
        "channelAdminLogEventActionChangeLocation": 0xe6b76ae,
        "channelAdminLogEventActionToggleSlowMode": 0x53909779,
        "channelAdminLogEventActionStartGroupCall": 0x23209745,
        "channelAdminLogEventActionDiscardGroupCall": 0xdb9f9140,
        "channelAdminLogEventActionParticipantMute": 0xf92424d2,
        "channelAdminLogEventActionParticipantUnmute": 0xe64429c0,
        "channelAdminLogEventActionToggleGroupCallSetting": 0x56d6a247,
        "channelAdminLogEventActionParticipantJoinByInvite": 0xfe9fc158,
        "channelAdminLogEventActionExportedInviteDelete": 0x5a50fca4,
        "channelAdminLogEventActionExportedInviteRevoke": 0x410a134e,
        "channelAdminLogEventActionExportedInviteEdit": 0xe90ebb59,
        "channelAdminLogEventActionParticipantVolume": 0x3e7f6847,
        "channelAdminLogEventActionChangeHistoryTTL": 0x6e941a38,
        "channelAdminLogEventActionParticipantJoinByRequest": 0xafb6144a,
        "channelAdminLogEventActionToggleNoForwards": 0xcb2ac766,
        "channelAdminLogEventActionSendMessage": 0x278f2868,
        "channelAdminLogEventActionChangeAvailableReactions": 0xbe4e0ef8,
        "channelAdminLogEventActionChangeUsernames": 0xf04fb3a9,
        "channelAdminLogEventActionToggleForum": 0x2cc6383,
        "channelAdminLogEventActionCreateTopic": 0x58707d28,
        "channelAdminLogEventActionEditTopic": 0xf06fe208,
        "channelAdminLogEventActionDeleteTopic": 0xae168909,
        "channelAdminLogEventActionPinTopic": 0x5d8d353b,
        "channelAdminLogEventActionToggleAntiSpam": 0x64f36dfc,
        "channelAdminLogEventActionChangePeerColor": 0x5796e780,
        "channelAdminLogEventActionChangeProfilePeerColor": 0x5e477b25,
        "channelAdminLogEventActionChangeWallpaper": 0x31bb5d52,
        "channelAdminLogEventActionChangeEmojiStatus": 0x3ea9feb1,
        "channelAdminLogEventActionChangeEmojiStickerSet": 0x46d840ab,
        "channelAdminLogEventActionToggleSignatureProfiles": 0x60a79c79,
        "channelAdminLogEventActionParticipantSubExtend": 0x64642db3,
        "channelAdminLogEventActionToggleAutotranslation": 0xc517f77e,
        "channelAdminLogEventActionParticipantEditRank": 0x5806b4ec,
    },
    "ChannelAdminLogEventsFilter": {
        "channelAdminLogEventsFilter": 0xea107ae4,
    },
    "ChannelLocation": {
        "channelLocationEmpty": 0xbfb5ad8b,
        "channelLocation": 0x209b82db,
    },
    "ChannelMessagesFilter": {
        "channelMessagesFilterEmpty": 0x94d42ee7,
        "channelMessagesFilter": 0xcd77d957,
    },
    "ChannelParticipant": {
        "channelParticipant": 0x1bd54456,
        "channelParticipantSelf": 0xa9478a1a,
        "channelParticipantCreator": 0x2fe601d3,
        "channelParticipantAdmin": 0x34c3bb53,
        "channelParticipantBanned": 0xd5f0ad91,
        "channelParticipantLeft": 0x1b03f006,
    },
    "ChannelParticipantsFilter": {
        "channelParticipantsRecent": 0xde3f3c79,
        "channelParticipantsAdmins": 0xb4608969,
        "channelParticipantsKicked": 0xa3b54985,
        "channelParticipantsBots": 0xb0d1865b,
        "channelParticipantsBanned": 0x1427a5e1,
        "channelParticipantsSearch": 0x656ac4b,
        "channelParticipantsContacts": 0xbb6ae88d,
        "channelParticipantsMentions": 0xe04b5ceb,
    },
    "Chat": {
        "chatEmpty": 0x29562865,
        "chat": 0x41cbf256,
        "chatForbidden": 0x6592a1a7,
        "channel": 0x1c32b11c,
        "channelForbidden": 0x17d493d5,
    },
    "ChatAdminRights": {
        "chatAdminRights": 0x5fb224d5,
    },
    "ChatAdminWithInvites": {
        "chatAdminWithInvites": 0xf2ecef23,
    },
    "ChatBannedRights": {
        "chatBannedRights": 0x9f120418,
    },
    "ChatFull": {
        "chatFull": 0x2633421b,
        "channelFull": 0xa04e8d3a,
    },
    "ChatInvite": {
        "chatInviteAlready": 0x5a686d7c,
        "chatInvite": 0x5c9d3702,
        "chatInvitePeek": 0x61695cb0,
    },
    "ChatInviteImporter": {
        "chatInviteImporter": 0x8c5adfd9,
    },
    "ChatOnlines": {
        "chatOnlines": 0xf041e250,
    },
    "ChatParticipant": {
        "chatParticipant": 0x38e79fde,
        "chatParticipantCreator": 0xe1f867b8,
        "chatParticipantAdmin": 0x360d5d2,
    },
    "ChatParticipants": {
        "chatParticipantsForbidden": 0x8763d3e1,
        "chatParticipants": 0x3cbc93f8,
    },
    "ChatPhoto": {
        "chatPhotoEmpty": 0x37c1011c,
        "chatPhoto": 0x1c6e1c11,
    },
    "ChatReactions": {
        "chatReactionsNone": 0xeafc32bc,
        "chatReactionsAll": 0x52928bca,
        "chatReactionsSome": 0x661d4037,
    },
    "ChatTheme": {
        "chatTheme": 0xc3dffc04,
        "chatThemeUniqueGift": 0x3458f9c8,
    },
    "CodeSettings": {
        "codeSettings": 0xad253d78,
    },
    "Config": {
        "config": 0xcc1a241e,
    },
    "ConnectedBot": {
        "connectedBot": 0x33ed001,
    },
    "ConnectedBotStarRef": {
        "connectedBotStarRef": 0x19a13f71,
    },
    "Contact": {
        "contact": 0x145ade0b,
    },
    "ContactBirthday": {
        "contactBirthday": 0x1d998733,
    },
    "ContactStatus": {
        "contactStatus": 0x16d9703b,
    },
    "DataJSON": {
        "dataJSON": 0x7d748d04,
    },
    "DcOption": {
        "dcOption": 0x18b7a10d,
    },
    "DefaultHistoryTTL": {
        "defaultHistoryTTL": 0x43b46b20,
    },
    "Dialog": {
        "dialog": 0xfc89f7f3,
        "dialogFolder": 0x71bd134c,
    },
    "DialogFilter": {
        "dialogFilter": 0xaa472651,
        "dialogFilterDefault": 0x363293ae,
        "dialogFilterChatlist": 0x96537bd7,
    },
    "DialogFilterSuggested": {
        "dialogFilterSuggested": 0x77744d4a,
    },
    "DialogPeer": {
        "dialogPeer": 0xe56dbf05,
        "dialogPeerFolder": 0x514519e2,
    },
    "DisallowedGiftsSettings": {
        "disallowedGiftsSettings": 0x71f276c4,
    },
    "Document": {
        "documentEmpty": 0x36f8c871,
        "document": 0x8fd4c4d8,
    },
    "DocumentAttribute": {
        "documentAttributeImageSize": 0x6c37c15c,
        "documentAttributeAnimated": 0x11b58939,
        "documentAttributeSticker": 0x6319d612,
        "documentAttributeVideo": 0x43c57c48,
        "documentAttributeAudio": 0x9852f9c6,
        "documentAttributeFilename": 0x15590068,
        "documentAttributeHasStickers": 0x9801d2f7,
        "documentAttributeCustomEmoji": 0xfd149899,
    },
    "DraftMessage": {
        "draftMessageEmpty": 0x1b0c841a,
        "draftMessage": 0x60fe3294,
    },
    "EmailVerification": {
        "emailVerificationCode": 0x922e55a9,
        "emailVerificationGoogle": 0xdb909ec2,
        "emailVerificationApple": 0x96d074fd,
    },
    "EmailVerifyPurpose": {
        "emailVerifyPurposeLoginSetup": 0x4345be73,
        "emailVerifyPurposeLoginChange": 0x527d22eb,
        "emailVerifyPurposePassport": 0xbbf51685,
    },
    "EmojiGroup": {
        "emojiGroup": 0x7a9abda9,
        "emojiGroupGreeting": 0x80d26cc7,
        "emojiGroupPremium": 0x93bcf34,
    },
    "EmojiKeyword": {
        "emojiKeyword": 0xd5b3b9f9,
        "emojiKeywordDeleted": 0x236df622,
    },
    "EmojiKeywordsDifference": {
        "emojiKeywordsDifference": 0x5cc761bd,
    },
    "EmojiLanguage": {
        "emojiLanguage": 0xb3fb5361,
    },
    "EmojiList": {
        "emojiListNotModified": 0x481eadfa,
        "emojiList": 0x7a1e11d1,
    },
    "EmojiStatus": {
        "emojiStatusEmpty": 0x2de11aae,
        "emojiStatus": 0xe7ff068a,
        "emojiStatusCollectible": 0x7184603b,
        "inputEmojiStatusCollectible": 0x7141dbf,
    },
    "EmojiURL": {
        "emojiURL": 0xa575739d,
    },
    "EncryptedChat": {
        "encryptedChatEmpty": 0xab7ec0a0,
        "encryptedChatWaiting": 0x66b25953,
        "encryptedChatRequested": 0x48f1d94c,
        "encryptedChat": 0x61f0d4c7,
        "encryptedChatDiscarded": 0x1e1c7c45,
    },
    "EncryptedFile": {
        "encryptedFileEmpty": 0xc21f497e,
        "encryptedFile": 0xa8008cd8,
    },
    "EncryptedMessage": {
        "encryptedMessage": 0xed18c118,
        "encryptedMessageService": 0x23734b06,
    },
    "Error": {
        "error": 0xc4b9f9bb,
    },
    "ExportedChatInvite": {
        "chatInviteExported": 0xa22cbd96,
        "chatInvitePublicJoinRequests": 0xed107ab7,
    },
    "ExportedChatlistInvite": {
        "exportedChatlistInvite": 0xc5181ac,
    },
    "ExportedContactToken": {
        "exportedContactToken": 0x41bf109b,
    },
    "ExportedMessageLink": {
        "exportedMessageLink": 0x5dab1af4,
    },
    "ExportedStoryLink": {
        "exportedStoryLink": 0x3fc9053b,
    },
    "FactCheck": {
        "factCheck": 0xb89bfccf,
    },
    "FileHash": {
        "fileHash": 0xf39b035c,
    },
    "Folder": {
        "folder": 0xff544e65,
    },
    "FolderPeer": {
        "folderPeer": 0xe9baa668,
    },
    "ForumTopic": {
        "forumTopicDeleted": 0x23f109b,
        "forumTopic": 0xfcdad815,
    },
    "FoundStory": {
        "foundStory": 0xe87acbc0,
    },
    "Game": {
        "game": 0xbdf9653b,
    },
    "GeoPoint": {
        "geoPointEmpty": 0x1117dd5f,
        "geoPoint": 0xb2a2f663,
    },
    "GeoPointAddress": {
        "geoPointAddress": 0xde4c5d93,
    },
    "GlobalPrivacySettings": {
        "globalPrivacySettings": 0xfe41b34f,
    },
    "GroupCall": {
        "groupCallDiscarded": 0x7780bcb4,
        "groupCall": 0xefb2b617,
    },
    "GroupCallDonor": {
        "groupCallDonor": 0xee430c85,
    },
    "GroupCallMessage": {
        "groupCallMessage": 0x1a8afc7e,
    },
    "GroupCallParticipant": {
        "groupCallParticipant": 0x2a3dc7ac,
    },
    "GroupCallParticipantVideo": {
        "groupCallParticipantVideo": 0x67753ac8,
    },
    "GroupCallParticipantVideoSourceGroup": {
        "groupCallParticipantVideoSourceGroup": 0xdcb118b7,
    },
    "GroupCallStreamChannel": {
        "groupCallStreamChannel": 0x80eb48af,
    },
    "HighScore": {
        "highScore": 0x73a379eb,
    },
    "ImportedContact": {
        "importedContact": 0xc13e3c50,
    },
    "InlineBotSwitchPM": {
        "inlineBotSwitchPM": 0x3c20629f,
    },
    "InlineBotWebView": {
        "inlineBotWebView": 0xb57295d5,
    },
    "InlineQueryPeerType": {
        "inlineQueryPeerTypeSameBotPM": 0x3081ed9d,
        "inlineQueryPeerTypePM": 0x833c0fac,
        "inlineQueryPeerTypeChat": 0xd766c50a,
        "inlineQueryPeerTypeMegagroup": 0x5ec4be43,
        "inlineQueryPeerTypeBroadcast": 0x6334ee9a,
        "inlineQueryPeerTypeBotPM": 0xe3b2d0c,
    },
    "InputAiComposeTone": {
        "inputAiComposeToneDefault": 0x1fe9a9bf,
        "inputAiComposeToneID": 0x773c080,
        "inputAiComposeToneSlug": 0x1fa01357,
    },
    "InputAppEvent": {
        "inputAppEvent": 0x1d1b1245,
    },
    "InputBotApp": {
        "inputBotAppID": 0xa920bd7a,
        "inputBotAppShortName": 0x908c0407,
    },
    "InputBotInlineMessage": {
        "inputBotInlineMessageMediaAuto": 0x3380c786,
        "inputBotInlineMessageText": 0x3dcd7a87,
        "inputBotInlineMessageMediaGeo": 0x96929a85,
        "inputBotInlineMessageMediaVenue": 0x417bbf11,
        "inputBotInlineMessageMediaContact": 0xa6edbffd,
        "inputBotInlineMessageGame": 0x4b425864,
        "inputBotInlineMessageMediaInvoice": 0xd7e78225,
        "inputBotInlineMessageMediaWebPage": 0xbddcc510,
        "inputBotInlineMessageRichMessage": 0xb43df56c,
    },
    "InputBotInlineMessageID": {
        "inputBotInlineMessageID": 0x890c3d89,
        "inputBotInlineMessageID64": 0xb6d915d7,
    },
    "InputBotInlineResult": {
        "inputBotInlineResult": 0x88bf9319,
        "inputBotInlineResultPhoto": 0xa8d864a7,
        "inputBotInlineResultDocument": 0xfff8fdc4,
        "inputBotInlineResultGame": 0x4fa417f2,
    },
    "InputBusinessAwayMessage": {
        "inputBusinessAwayMessage": 0x832175e0,
    },
    "InputBusinessBotRecipients": {
        "inputBusinessBotRecipients": 0xc4e5921e,
    },
    "InputBusinessChatLink": {
        "inputBusinessChatLink": 0x11679fa7,
    },
    "InputBusinessGreetingMessage": {
        "inputBusinessGreetingMessage": 0x194cb3b,
    },
    "InputBusinessIntro": {
        "inputBusinessIntro": 0x9c469cd,
    },
    "InputBusinessRecipients": {
        "inputBusinessRecipients": 0x6f8b32aa,
    },
    "InputChannel": {
        "inputChannelEmpty": 0xee8c1e86,
        "inputChannel": 0xf35aec28,
        "inputChannelFromMessage": 0x5b934f9d,
    },
    "InputChatPhoto": {
        "inputChatPhotoEmpty": 0x1ca48f57,
        "inputChatUploadedPhoto": 0xbdcdaec0,
        "inputChatPhoto": 0x8953ad37,
    },
    "InputChatTheme": {
        "inputChatThemeEmpty": 0x83268483,
        "inputChatTheme": 0xc93de95c,
        "inputChatThemeUniqueGift": 0x87e5dfe4,
    },
    "InputChatlist": {
        "inputChatlistDialogFilter": 0xf3e0da33,
    },
    "InputCheckPasswordSRP": {
        "inputCheckPasswordEmpty": 0x9880f658,
        "inputCheckPasswordSRP": 0xd27ff082,
    },
    "InputClientProxy": {
        "inputClientProxy": 0x75588b3f,
    },
    "InputCollectible": {
        "inputCollectibleUsername": 0xe39460a9,
        "inputCollectiblePhone": 0xa2e214a4,
    },
    "InputContact": {
        "inputPhoneContact": 0x6a1dc4be,
    },
    "InputDialogPeer": {
        "inputDialogPeer": 0xfcaafeb7,
        "inputDialogPeerFolder": 0x64600527,
    },
    "InputDocument": {
        "inputDocumentEmpty": 0x72f0eaae,
        "inputDocument": 0x1abfb575,
    },
    "InputEncryptedChat": {
        "inputEncryptedChat": 0xf141b5e1,
    },
    "InputEncryptedFile": {
        "inputEncryptedFileEmpty": 0x1837c364,
        "inputEncryptedFileUploaded": 0x64bd0306,
        "inputEncryptedFile": 0x5a17b5e5,
        "inputEncryptedFileBigUploaded": 0x2dc173c8,
    },
    "InputFile": {
        "inputFile": 0xf52ff27f,
        "inputFileBig": 0xfa4f0bb5,
        "inputFileStoryDocument": 0x62dc8b48,
    },
    "InputFileLocation": {
        "inputFileLocation": 0xdfdaabe1,
        "inputEncryptedFileLocation": 0xf5235d55,
        "inputDocumentFileLocation": 0xbad07584,
        "inputSecureFileLocation": 0xcbc7ee28,
        "inputTakeoutFileLocation": 0x29be5899,
        "inputPhotoFileLocation": 0x40181ffe,
        "inputPhotoLegacyFileLocation": 0xd83466f3,
        "inputPeerPhotoFileLocation": 0x37257e99,
        "inputStickerSetThumb": 0x9d84f3db,
        "inputGroupCallStream": 0x598a92a,
    },
    "InputFolderPeer": {
        "inputFolderPeer": 0xfbd2c296,
    },
    "InputGame": {
        "inputGameID": 0x32c3e77,
        "inputGameShortName": 0xc331e80a,
    },
    "InputGeoPoint": {
        "inputGeoPointEmpty": 0xe4c123d6,
        "inputGeoPoint": 0x48222faf,
    },
    "InputGroupCall": {
        "inputGroupCall": 0xd8aa840f,
        "inputGroupCallSlug": 0xfe06823f,
        "inputGroupCallInviteMessage": 0x8c10603f,
    },
    "InputInvoice": {
        "inputInvoiceMessage": 0xc5b56859,
        "inputInvoiceSlug": 0xc326caef,
        "inputInvoicePremiumGiftCode": 0x98986c0d,
        "inputInvoiceStars": 0x65f00ce3,
        "inputInvoiceChatInviteSubscription": 0x34e793f1,
        "inputInvoiceStarGift": 0xe8625e92,
        "inputInvoiceStarGiftUpgrade": 0x4d818d5d,
        "inputInvoiceStarGiftTransfer": 0x4a5f5bd9,
        "inputInvoicePremiumGiftStars": 0xdabab2ef,
        "inputInvoiceBusinessBotTransferStars": 0xf4997e42,
        "inputInvoiceStarGiftResale": 0xc39f5324,
        "inputInvoiceStarGiftPrepaidUpgrade": 0x9a0b48b8,
        "inputInvoicePremiumAuthCode": 0x3e77f614,
        "inputInvoiceStarGiftDropOriginalDetails": 0x923d8d1,
        "inputInvoiceStarGiftAuctionBid": 0x1ecafa10,
    },
    "InputMedia": {
        "inputMediaEmpty": 0x9664f57f,
        "inputMediaUploadedPhoto": 0x7d8375da,
        "inputMediaPhoto": 0xe3af4434,
        "inputMediaGeoPoint": 0xf9c44144,
        "inputMediaContact": 0xf8ab7dfb,
        "inputMediaUploadedDocument": 0x37c9330,
        "inputMediaDocument": 0xa8763ab5,
        "inputMediaVenue": 0xc13d1c11,
        "inputMediaPhotoExternal": 0xe5bbfe1a,
        "inputMediaDocumentExternal": 0x779600f9,
        "inputMediaGame": 0xd33f43f3,
        "inputMediaInvoice": 0x405fef0d,
        "inputMediaGeoLive": 0x971fa843,
        "inputMediaPoll": 0x883a4108,
        "inputMediaDice": 0xe66fbf7b,
        "inputMediaStory": 0x89fdd778,
        "inputMediaWebPage": 0xc21b8849,
        "inputMediaPaidMedia": 0xc4103386,
        "inputMediaTodo": 0x9fc55fde,
        "inputMediaStakeDice": 0xf3a9244a,
    },
    "InputMessage": {
        "inputMessageID": 0xa676a322,
        "inputMessageReplyTo": 0xbad88395,
        "inputMessagePinned": 0x86872538,
        "inputMessageCallbackQuery": 0xacfa1a7e,
    },
    "InputMessageReadMetric": {
        "inputMessageReadMetric": 0x402b4495,
    },
    "InputNotifyPeer": {
        "inputNotifyPeer": 0xb8bc5b0c,
        "inputNotifyUsers": 0x193b4417,
        "inputNotifyChats": 0x4a95e84e,
        "inputNotifyBroadcasts": 0xb1db7c7e,
        "inputNotifyForumTopic": 0x5c467992,
    },
    "InputPasskeyCredential": {
        "inputPasskeyCredentialPublicKey": 0x3c27b78f,
        "inputPasskeyCredentialFirebasePNV": 0x5b1ccb28,
    },
    "InputPasskeyResponse": {
        "inputPasskeyResponseRegister": 0x3e63935c,
        "inputPasskeyResponseLogin": 0xc31fc14a,
    },
    "InputPaymentCredentials": {
        "inputPaymentCredentialsSaved": 0xc10eb2cf,
        "inputPaymentCredentials": 0x3417d728,
        "inputPaymentCredentialsApplePay": 0xaa1c39f,
        "inputPaymentCredentialsGooglePay": 0x8ac32801,
    },
    "InputPeer": {
        "inputPeerEmpty": 0x7f3b18ea,
        "inputPeerSelf": 0x7da07ec9,
        "inputPeerChat": 0x35a95cb9,
        "inputPeerUser": 0xdde8a54c,
        "inputPeerChannel": 0x27bcbbfc,
        "inputPeerUserFromMessage": 0xa87b0a1c,
        "inputPeerChannelFromMessage": 0xbd2a0840,
    },
    "InputPeerNotifySettings": {
        "inputPeerNotifySettings": 0xcacb6ae2,
    },
    "InputPhoneCall": {
        "inputPhoneCall": 0x1e36fded,
    },
    "InputPhoto": {
        "inputPhotoEmpty": 0x1cd7bf0d,
        "inputPhoto": 0x3bb3b94a,
    },
    "InputPrivacyKey": {
        "inputPrivacyKeyStatusTimestamp": 0x4f96cb18,
        "inputPrivacyKeyChatInvite": 0xbdfb0426,
        "inputPrivacyKeyPhoneCall": 0xfabadc5f,
        "inputPrivacyKeyPhoneP2P": 0xdb9e70d2,
        "inputPrivacyKeyForwards": 0xa4dd4c08,
        "inputPrivacyKeyProfilePhoto": 0x5719bacc,
        "inputPrivacyKeyPhoneNumber": 0x352dafa,
        "inputPrivacyKeyAddedByPhone": 0xd1219bdd,
        "inputPrivacyKeyVoiceMessages": 0xaee69d68,
        "inputPrivacyKeyAbout": 0x3823cc40,
        "inputPrivacyKeyBirthday": 0xd65a11cc,
        "inputPrivacyKeyStarGiftsAutoSave": 0xe1732341,
        "inputPrivacyKeyNoPaidMessages": 0xbdc597b4,
        "inputPrivacyKeySavedMusic": 0x4dbe9226,
    },
    "InputPrivacyRule": {
        "inputPrivacyValueAllowContacts": 0xd09e07b,
        "inputPrivacyValueAllowAll": 0x184b35ce,
        "inputPrivacyValueAllowUsers": 0x131cc67f,
        "inputPrivacyValueDisallowContacts": 0xba52007,
        "inputPrivacyValueDisallowAll": 0xd66b66c9,
        "inputPrivacyValueDisallowUsers": 0x90110467,
        "inputPrivacyValueAllowChatParticipants": 0x840649cf,
        "inputPrivacyValueDisallowChatParticipants": 0xe94f0f86,
        "inputPrivacyValueAllowCloseFriends": 0x2f453e49,
        "inputPrivacyValueAllowPremium": 0x77cdc9f1,
        "inputPrivacyValueAllowBots": 0x5a4fcce5,
        "inputPrivacyValueDisallowBots": 0xc4e57915,
    },
    "InputQuickReplyShortcut": {
        "inputQuickReplyShortcut": 0x24596d41,
        "inputQuickReplyShortcutId": 0x1190cf1,
    },
    "InputReplyTo": {
        "inputReplyToMessage": 0x3bd4b7c2,
        "inputReplyToStory": 0x5881323a,
        "inputReplyToMonoForum": 0x69d66c45,
    },
    "InputRichFile": {
        "inputRichFilePhoto": 0x9b00622b,
        "inputRichFileDocument": 0x83281dbd,
    },
    "InputRichMessage": {
        "inputRichMessage": 0xe4c449fc,
        "inputRichMessageHTML": 0xdacb836a,
        "inputRichMessageMarkdown": 0x4b572c,
    },
    "InputSavedStarGift": {
        "inputSavedStarGiftUser": 0x69279795,
        "inputSavedStarGiftChat": 0xf101aa7f,
        "inputSavedStarGiftSlug": 0x2085c238,
    },
    "InputSecureFile": {
        "inputSecureFileUploaded": 0x3334b0f0,
        "inputSecureFile": 0x5367e5be,
    },
    "InputSecureValue": {
        "inputSecureValue": 0xdb21d0a7,
    },
    "InputSingleMedia": {
        "inputSingleMedia": 0x1cc6e91f,
    },
    "InputStarGiftAuction": {
        "inputStarGiftAuction": 0x2e16c98,
        "inputStarGiftAuctionSlug": 0x7ab58308,
    },
    "InputStarsTransaction": {
        "inputStarsTransaction": 0x206ae6d1,
    },
    "InputStickerSet": {
        "inputStickerSetEmpty": 0xffb62b95,
        "inputStickerSetID": 0x9de7a269,
        "inputStickerSetShortName": 0x861cc8a0,
        "inputStickerSetAnimatedEmoji": 0x28703c8,
        "inputStickerSetDice": 0xe67f520e,
        "inputStickerSetAnimatedEmojiAnimations": 0xcde3739,
        "inputStickerSetPremiumGifts": 0xc88b3b02,
        "inputStickerSetEmojiGenericAnimations": 0x4c4d4ce,
        "inputStickerSetEmojiDefaultStatuses": 0x29d0f5ee,
        "inputStickerSetEmojiDefaultTopicIcons": 0x44c1f8e9,
        "inputStickerSetEmojiChannelDefaultStatuses": 0x49748553,
        "inputStickerSetTonGifts": 0x1cf671a0,
    },
    "InputStickerSetItem": {
        "inputStickerSetItem": 0x32da9e9c,
    },
    "InputStickeredMedia": {
        "inputStickeredMediaPhoto": 0x4a992157,
        "inputStickeredMediaDocument": 0x438865b,
    },
    "InputStorePaymentPurpose": {
        "inputStorePaymentPremiumSubscription": 0xa6751e66,
        "inputStorePaymentGiftPremium": 0x616f7fe8,
        "inputStorePaymentPremiumGiftCode": 0xfb790393,
        "inputStorePaymentPremiumGiveaway": 0x160544ca,
        "inputStorePaymentStarsTopup": 0xf9a2a6cb,
        "inputStorePaymentStarsGift": 0x1d741ef7,
        "inputStorePaymentStarsGiveaway": 0x751f08fa,
        "inputStorePaymentAuthCode": 0x3fc18057,
    },
    "InputTheme": {
        "inputTheme": 0x3c5693e9,
        "inputThemeSlug": 0xf5890df1,
    },
    "InputThemeSettings": {
        "inputThemeSettings": 0x8fde504f,
    },
    "InputUser": {
        "inputUserEmpty": 0xb98886cf,
        "inputUserSelf": 0xf7c1b13f,
        "inputUser": 0xf21158c6,
        "inputUserFromMessage": 0x1da448e2,
    },
    "InputWallPaper": {
        "inputWallPaper": 0xe630b979,
        "inputWallPaperSlug": 0x72091c80,
        "inputWallPaperNoFile": 0x967a462e,
    },
    "InputWebDocument": {
        "inputWebDocument": 0x9bed434d,
    },
    "InputWebFileLocation": {
        "inputWebFileLocation": 0xc239d686,
        "inputWebFileGeoPointLocation": 0x9f2221c9,
        "inputWebFileAudioAlbumThumbLocation": 0xf46fe924,
    },
    "Invoice": {
        "invoice": 0x49ee584,
    },
    "JSONObjectValue": {
        "jsonObjectValue": 0xc0de1bd9,
    },
    "JSONValue": {
        "jsonNull": 0x3f6d7b68,
        "jsonBool": 0xc7345e6a,
        "jsonNumber": 0x2be0dfa4,
        "jsonString": 0xb71e767a,
        "jsonArray": 0xf7444763,
        "jsonObject": 0x99c1d49d,
    },
    "JoinChatBotResult": {
        "joinChatBotResultApproved": 0xae152a69,
        "joinChatBotResultDeclined": 0xefa0194,
        "joinChatBotResultQueued": 0x98a3a840,
        "joinChatBotResultWebView": 0xd6e3b813,
    },
    "KeyboardButton": {
        "keyboardButton": 0x7d170cff,
        "keyboardButtonUrl": 0xd80c25ec,
        "keyboardButtonCallback": 0xe62bc960,
        "keyboardButtonRequestPhone": 0x417efd8f,
        "keyboardButtonRequestGeoLocation": 0xaa40f94d,
        "keyboardButtonSwitchInline": 0x991399fc,
        "keyboardButtonGame": 0x89c590f9,
        "keyboardButtonBuy": 0x3fa53905,
        "keyboardButtonUrlAuth": 0xf51006f9,
        "inputKeyboardButtonUrlAuth": 0x68013e72,
        "keyboardButtonRequestPoll": 0x7a11d782,
        "inputKeyboardButtonUserProfile": 0x7d5e07c7,
        "keyboardButtonUserProfile": 0xc0fd5d09,
        "keyboardButtonWebView": 0xe846b1a0,
        "keyboardButtonSimpleWebView": 0xe15c4370,
        "keyboardButtonRequestPeer": 0x5b0f15f5,
        "inputKeyboardButtonRequestPeer": 0x2b78156,
        "keyboardButtonCopy": 0xbcc4af10,
    },
    "KeyboardButtonRow": {
        "keyboardButtonRow": 0x77608b83,
    },
    "KeyboardButtonStyle": {
        "keyboardButtonStyle": 0x4fdd3430,
    },
    "LabeledPrice": {
        "labeledPrice": 0xcb296bf8,
    },
    "LangPackDifference": {
        "langPackDifference": 0xf385c1f6,
    },
    "LangPackLanguage": {
        "langPackLanguage": 0xeeca5ce3,
    },
    "LangPackString": {
        "langPackString": 0xcad181f6,
        "langPackStringPluralized": 0x6c47ac9f,
        "langPackStringDeleted": 0x2979eeb2,
    },
    "MaskCoords": {
        "maskCoords": 0xaed6dbb2,
    },
    "MediaArea": {
        "mediaAreaVenue": 0xbe82db9c,
        "inputMediaAreaVenue": 0xb282217f,
        "mediaAreaGeoPoint": 0xcad5452d,
        "mediaAreaSuggestedReaction": 0x14455871,
        "mediaAreaChannelPost": 0x770416af,
        "inputMediaAreaChannelPost": 0x2271f2bf,
        "mediaAreaUrl": 0x37381085,
        "mediaAreaWeather": 0x49a6549c,
        "mediaAreaStarGift": 0x5787686d,
    },
    "MediaAreaCoordinates": {
        "mediaAreaCoordinates": 0xcfc9e002,
    },
    "Message": {
        "messageEmpty": 0x90a6ca84,
        "message": 0x7600b9d3,
        "messageService": 0x7a800e0a,
    },
    "MessageAction": {
        "messageActionEmpty": 0xb6aef7b0,
        "messageActionChatCreate": 0xbd47cbad,
        "messageActionChatEditTitle": 0xb5a1ce5a,
        "messageActionChatEditPhoto": 0x7fcb13a8,
        "messageActionChatDeletePhoto": 0x95e3fbef,
        "messageActionChatAddUser": 0x15cefd00,
        "messageActionChatDeleteUser": 0xa43f30cc,
        "messageActionChatJoinedByLink": 0x31224c3,
        "messageActionChannelCreate": 0x95d2ac92,
        "messageActionChatMigrateTo": 0xe1037f92,
        "messageActionChannelMigrateFrom": 0xea3948e9,
        "messageActionPinMessage": 0x94bd38ed,
        "messageActionHistoryClear": 0x9fbab604,
        "messageActionGameScore": 0x92a72876,
        "messageActionPaymentSentMe": 0xffa00ccc,
        "messageActionPaymentSent": 0xc624b16e,
        "messageActionPhoneCall": 0x80e11a7f,
        "messageActionScreenshotTaken": 0x4792929b,
        "messageActionCustomAction": 0xfae69f56,
        "messageActionBotAllowed": 0xc516d679,
        "messageActionSecureValuesSentMe": 0x1b287353,
        "messageActionSecureValuesSent": 0xd95c6154,
        "messageActionContactSignUp": 0xf3f25f76,
        "messageActionGeoProximityReached": 0x98e0d697,
        "messageActionGroupCall": 0x7a0d7f42,
        "messageActionInviteToGroupCall": 0x502f92f7,
        "messageActionSetMessagesTTL": 0x3c134d7b,
        "messageActionGroupCallScheduled": 0xb3a07661,
        "messageActionSetChatTheme": 0xb91bbd3a,
        "messageActionChatJoinedByRequest": 0xebbca3cb,
        "messageActionWebViewDataSentMe": 0x47dd8079,
        "messageActionWebViewDataSent": 0xb4c38cb5,
        "messageActionGiftPremium": 0x48e91302,
        "messageActionTopicCreate": 0xd999256,
        "messageActionTopicEdit": 0xc0944820,
        "messageActionSuggestProfilePhoto": 0x57de635e,
        "messageActionRequestedPeer": 0x31518e9b,
        "messageActionSetChatWallPaper": 0x5060a3f4,
        "messageActionGiftCode": 0x31c48347,
        "messageActionGiveawayLaunch": 0xa80f51e4,
        "messageActionGiveawayResults": 0x87e2f155,
        "messageActionBoostApply": 0xcc02aa6d,
        "messageActionRequestedPeerSentMe": 0x93b31848,
        "messageActionPaymentRefunded": 0x41b3e202,
        "messageActionGiftStars": 0x45d5b021,
        "messageActionPrizeStars": 0xb00c47a2,
        "messageActionStarGift": 0xea2c31d3,
        "messageActionStarGiftUnique": 0xe6c31522,
        "messageActionPaidMessagesRefunded": 0xac1f1fcd,
        "messageActionPaidMessagesPrice": 0x84b88578,
        "messageActionConferenceCall": 0x2ffe2f7a,
        "messageActionTodoCompletions": 0xcc7c5c89,
        "messageActionTodoAppendTasks": 0xc7edbc83,
        "messageActionSuggestedPostApproval": 0xee7a1596,
        "messageActionSuggestedPostSuccess": 0x95ddcf69,
        "messageActionSuggestedPostRefund": 0x69f916f8,
        "messageActionGiftTon": 0xa8a3c699,
        "messageActionSuggestBirthday": 0x2c8f2a25,
        "messageActionStarGiftPurchaseOffer": 0x774278d4,
        "messageActionStarGiftPurchaseOfferDeclined": 0x73ada76b,
        "messageActionNewCreatorPending": 0xb07ed085,
        "messageActionChangeCreator": 0xe188503b,
        "messageActionNoForwardsToggle": 0xbf7d6572,
        "messageActionNoForwardsRequest": 0x3e2793ba,
        "messageActionPollAppendAnswer": 0x9da1cd6c,
        "messageActionPollDeleteAnswer": 0x399674dc,
        "messageActionManagedBotCreated": 0x16605e3e,
    },
    "MessageEntity": {
        "messageEntityUnknown": 0xbb92ba95,
        "messageEntityMention": 0xfa04579d,
        "messageEntityHashtag": 0x6f635b0d,
        "messageEntityBotCommand": 0x6cef8ac7,
        "messageEntityUrl": 0x6ed02538,
        "messageEntityEmail": 0x64e475c2,
        "messageEntityBold": 0xbd610bc9,
        "messageEntityItalic": 0x826f8b60,
        "messageEntityCode": 0x28a20571,
        "messageEntityPre": 0x73924be0,
        "messageEntityTextUrl": 0x76a6d327,
        "messageEntityMentionName": 0xdc7b1140,
        "inputMessageEntityMentionName": 0x208e68c9,
        "messageEntityPhone": 0x9b69e34b,
        "messageEntityCashtag": 0x4c4e743f,
        "messageEntityUnderline": 0x9c4e7e8b,
        "messageEntityStrike": 0xbf0693d4,
        "messageEntityBankCard": 0x761e6af4,
        "messageEntitySpoiler": 0x32ca960f,
        "messageEntityCustomEmoji": 0xc8cf05f8,
        "messageEntityBlockquote": 0xf1ccaaac,
        "messageEntityFormattedDate": 0x904ac7c7,
        "messageEntityDiffInsert": 0x71777116,
        "messageEntityDiffReplace": 0xc6c1e5a7,
        "messageEntityDiffDelete": 0x652c1c5,
    },
    "MessageExtendedMedia": {
        "messageExtendedMediaPreview": 0xad628cc8,
        "messageExtendedMedia": 0xee479c64,
    },
    "MessageFwdHeader": {
        "messageFwdHeader": 0x4e4df4bb,
    },
    "MessageMedia": {
        "messageMediaEmpty": 0x3ded6320,
        "messageMediaPhoto": 0xe216eb63,
        "messageMediaGeo": 0x56e0d474,
        "messageMediaContact": 0x70322949,
        "messageMediaUnsupported": 0x9f84f49e,
        "messageMediaDocument": 0x52d8ccd9,
        "messageMediaWebPage": 0xddf10c3b,
        "messageMediaVenue": 0x2ec0533f,
        "messageMediaGame": 0xfdb19008,
        "messageMediaInvoice": 0xf6a548d3,
        "messageMediaGeoLive": 0xb940c666,
        "messageMediaPoll": 0x773f4e66,
        "messageMediaDice": 0x8cbec07,
        "messageMediaStory": 0x68cb6283,
        "messageMediaGiveaway": 0xaa073beb,
        "messageMediaGiveawayResults": 0xceaa3ea1,
        "messageMediaPaidMedia": 0xa8852491,
        "messageMediaToDo": 0x8a53b014,
        "messageMediaVideoStream": 0xca5cab89,
    },
    "MessagePeerReaction": {
        "messagePeerReaction": 0x8c79b63c,
    },
    "MessagePeerVote": {
        "messagePeerVote": 0xb6cc2d5c,
        "messagePeerVoteInputOption": 0x74cda504,
        "messagePeerVoteMultiple": 0x4628f6e6,
    },
    "MessageRange": {
        "messageRange": 0xae30253,
    },
    "MessageReactions": {
        "messageReactions": 0xa339f0b,
    },
    "MessageReactor": {
        "messageReactor": 0x4ba3a95a,
    },
    "MessageReplies": {
        "messageReplies": 0x83d60fc2,
    },
    "MessageReplyHeader": {
        "messageReplyHeader": 0x1b97dd66,
        "messageReplyStoryHeader": 0xe5af939,
    },
    "MessageReportOption": {
        "messageReportOption": 0x7903e3d9,
    },
    "MessageViews": {
        "messageViews": 0x455b853d,
    },
    "MessagesFilter": {
        "inputMessagesFilterEmpty": 0x57e2f66c,
        "inputMessagesFilterPhotos": 0x9609a51c,
        "inputMessagesFilterVideo": 0x9fc00e65,
        "inputMessagesFilterPhotoVideo": 0x56e9f0e4,
        "inputMessagesFilterDocument": 0x9eddf188,
        "inputMessagesFilterUrl": 0x7ef0dd87,
        "inputMessagesFilterGif": 0xffc86587,
        "inputMessagesFilterVoice": 0x50f5c392,
        "inputMessagesFilterMusic": 0x3751b49e,
        "inputMessagesFilterChatPhotos": 0x3a20ecb8,
        "inputMessagesFilterPhoneCalls": 0x80c99768,
        "inputMessagesFilterRoundVoice": 0x7a7c17a4,
        "inputMessagesFilterRoundVideo": 0xb549da53,
        "inputMessagesFilterMyMentions": 0xc1f8e69a,
        "inputMessagesFilterGeo": 0xe7026d0d,
        "inputMessagesFilterContacts": 0xe062db83,
        "inputMessagesFilterPinned": 0x1bb00451,
        "inputMessagesFilterPoll": 0xfa2bc90a,
    },
    "MissingInvitee": {
        "missingInvitee": 0x628c9224,
    },
    "MyBoost": {
        "myBoost": 0xc448415c,
    },
    "NearestDc": {
        "nearestDc": 0x8e1a1775,
    },
    "NotificationSound": {
        "notificationSoundDefault": 0x97e8bebe,
        "notificationSoundNone": 0x6f0c34df,
        "notificationSoundLocal": 0x830b9ae4,
        "notificationSoundRingtone": 0xff6c8049,
    },
    "NotifyPeer": {
        "notifyPeer": 0x9fd40bd8,
        "notifyUsers": 0xb4c83b4c,
        "notifyChats": 0xc007cec3,
        "notifyBroadcasts": 0xd612e8ef,
        "notifyForumTopic": 0x226e6308,
    },
    "Null": {
        "null": 0x56730bcc,
    },
    "OutboxReadDate": {
        "outboxReadDate": 0x3bb842ac,
    },
    "Page": {
        "page": 0x98657f0d,
    },
    "PageBlock": {
        "pageBlockUnsupported": 0x13567e8a,
        "pageBlockTitle": 0x70abc3fd,
        "pageBlockSubtitle": 0x8ffa9a1f,
        "pageBlockAuthorDate": 0xbaafe5e0,
        "pageBlockHeader": 0xbfd064ec,
        "pageBlockSubheader": 0xf12bb6e1,
        "pageBlockParagraph": 0x467a0766,
        "pageBlockPreformatted": 0xc070d93e,
        "pageBlockFooter": 0x48870999,
        "pageBlockDivider": 0xdb20b188,
        "pageBlockAnchor": 0xce0d37b0,
        "pageBlockList": 0xe4e88011,
        "pageBlockBlockquote": 0x263d7c26,
        "pageBlockPullquote": 0x4f4456d3,
        "pageBlockPhoto": 0x1759c560,
        "pageBlockVideo": 0x7c8fe7b6,
        "pageBlockCover": 0x39f23300,
        "pageBlockEmbed": 0xa8718dc5,
        "pageBlockEmbedPost": 0xf259a80b,
        "pageBlockCollage": 0x65a0fa4d,
        "pageBlockSlideshow": 0x31f9590,
        "pageBlockChannel": 0xef1751b5,
        "pageBlockAudio": 0x804361ea,
        "pageBlockKicker": 0x1e148390,
        "pageBlockTable": 0xbf4dea82,
        "pageBlockOrderedList": 0x1fd6f6c1,
        "pageBlockDetails": 0x76768bed,
        "pageBlockRelatedArticles": 0x16115a96,
        "pageBlockMap": 0xa44f3ef6,
        "pageBlockHeading1": 0xbaff072f,
        "pageBlockHeading2": 0x96b2aec,
        "pageBlockHeading3": 0x67e731ad,
        "pageBlockHeading4": 0xb532772b,
        "pageBlockHeading5": 0xdbbe6c6a,
        "pageBlockHeading6": 0x682a41a9,
        "pageBlockMath": 0x59080c20,
        "pageBlockThinking": 0x3c29a3e2,
        "inputPageBlockMap": 0x574b617f,
        "pageBlockBlockquoteBlocks": 0xe6e47c4,
    },
    "PageCaption": {
        "pageCaption": 0x6f747657,
    },
    "PageListItem": {
        "pageListItemText": 0x2f58683c,
        "pageListItemBlocks": 0x63ca67aa,
    },
    "PageListOrderedItem": {
        "pageListOrderedItemText": 0x15031189,
        "pageListOrderedItemBlocks": 0x8ff2d5f0,
    },
    "PageRelatedArticle": {
        "pageRelatedArticle": 0xb390dc08,
    },
    "PageTableCell": {
        "pageTableCell": 0x34566b6a,
    },
    "PageTableRow": {
        "pageTableRow": 0xe0c0c5e5,
    },
    "PaidReactionPrivacy": {
        "paidReactionPrivacyDefault": 0x206ad49e,
        "paidReactionPrivacyAnonymous": 0x1f0c1ad9,
        "paidReactionPrivacyPeer": 0xdc6cfcf0,
    },
    "Passkey": {
        "passkey": 0x98613ebf,
    },
    "PasswordKdfAlgo": {
        "passwordKdfAlgoUnknown": 0xd45ab096,
        "passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow": 0x3a912d4a,
    },
    "PaymentCharge": {
        "paymentCharge": 0xea02c27e,
    },
    "PaymentFormMethod": {
        "paymentFormMethod": 0x88f8f21b,
    },
    "PaymentRequestedInfo": {
        "paymentRequestedInfo": 0x909c3f94,
    },
    "PaymentSavedCredentials": {
        "paymentSavedCredentialsCard": 0xcdc27a1f,
    },
    "Peer": {
        "peerUser": 0x59511722,
        "peerChat": 0x36c6019a,
        "peerChannel": 0xa2a5371e,
    },
    "PeerBlocked": {
        "peerBlocked": 0xe8fd8014,
    },
    "PeerColor": {
        "peerColor": 0xb54b5acf,
        "peerColorCollectible": 0xb9c0639a,
        "inputPeerColorCollectible": 0xb8ea86a9,
    },
    "PeerLocated": {
        "peerLocated": 0xca461b5d,
        "peerSelfLocated": 0xf8ec284b,
    },
    "PeerNotifySettings": {
        "peerNotifySettings": 0x99622c0c,
    },
    "PeerSettings": {
        "peerSettings": 0xf47741f7,
    },
    "PeerStories": {
        "peerStories": 0x9a35e999,
    },
    "PendingSuggestion": {
        "pendingSuggestion": 0xe7e82e12,
    },
    "PhoneCall": {
        "phoneCallEmpty": 0x5366c915,
        "phoneCallWaiting": 0xc5226f17,
        "phoneCallRequested": 0x14b0ed0c,
        "phoneCallAccepted": 0x3660c311,
        "phoneCall": 0x30535af5,
        "phoneCallDiscarded": 0x50ca4de1,
    },
    "PhoneCallDiscardReason": {
        "phoneCallDiscardReasonMissed": 0x85e42301,
        "phoneCallDiscardReasonDisconnect": 0xe095c1a0,
        "phoneCallDiscardReasonHangup": 0x57adc690,
        "phoneCallDiscardReasonBusy": 0xfaf7e8c9,
        "phoneCallDiscardReasonMigrateConferenceCall": 0x9fbbf1f7,
    },
    "PhoneCallProtocol": {
        "phoneCallProtocol": 0xfc878fc8,
    },
    "PhoneConnection": {
        "phoneConnection": 0x9cc123c7,
        "phoneConnectionWebrtc": 0x635fe375,
    },
    "Photo": {
        "photoEmpty": 0x2331b22d,
        "photo": 0xfb197a65,
    },
    "PhotoSize": {
        "photoSizeEmpty": 0xe17e23c,
        "photoSize": 0x75c78e60,
        "photoCachedSize": 0x21e1ad6,
        "photoStrippedSize": 0xe0b0bc2e,
        "photoSizeProgressive": 0xfa3efb95,
        "photoPathSize": 0xd8214d41,
    },
    "Poll": {
        "poll": 0x966e2dbf,
    },
    "PollAnswer": {
        "pollAnswer": 0x4b7d786a,
        "inputPollAnswer": 0x199fed96,
    },
    "PollAnswerVoters": {
        "pollAnswerVoters": 0x3645230a,
    },
    "PollResults": {
        "pollResults": 0xba7bb15e,
    },
    "PopularContact": {
        "popularContact": 0x5ce14175,
    },
    "PostAddress": {
        "postAddress": 0x1e8caaeb,
    },
    "PostInteractionCounters": {
        "postInteractionCountersMessage": 0xe7058e7f,
        "postInteractionCountersStory": 0x8a480e27,
    },
    "PremiumGiftCodeOption": {
        "premiumGiftCodeOption": 0x257e962b,
    },
    "PremiumSubscriptionOption": {
        "premiumSubscriptionOption": 0x5f2d1df2,
    },
    "PrepaidGiveaway": {
        "prepaidGiveaway": 0xb2539d54,
        "prepaidStarsGiveaway": 0x9a9d77e0,
    },
    "PrivacyKey": {
        "privacyKeyStatusTimestamp": 0xbc2eab30,
        "privacyKeyChatInvite": 0x500e6dfa,
        "privacyKeyPhoneCall": 0x3d662b7b,
        "privacyKeyPhoneP2P": 0x39491cc8,
        "privacyKeyForwards": 0x69ec56a3,
        "privacyKeyProfilePhoto": 0x96151fed,
        "privacyKeyPhoneNumber": 0xd19ae46d,
        "privacyKeyAddedByPhone": 0x42ffd42b,
        "privacyKeyVoiceMessages": 0x697f414,
        "privacyKeyAbout": 0xa486b761,
        "privacyKeyBirthday": 0x2000a518,
        "privacyKeyStarGiftsAutoSave": 0x2ca4fdf8,
        "privacyKeyNoPaidMessages": 0x17d348d2,
        "privacyKeySavedMusic": 0xff7a571b,
    },
    "PrivacyRule": {
        "privacyValueAllowContacts": 0xfffe1bac,
        "privacyValueAllowAll": 0x65427b82,
        "privacyValueAllowUsers": 0xb8905fb2,
        "privacyValueDisallowContacts": 0xf888fa1a,
        "privacyValueDisallowAll": 0x8b73e763,
        "privacyValueDisallowUsers": 0xe4621141,
        "privacyValueAllowChatParticipants": 0x6b134e8e,
        "privacyValueDisallowChatParticipants": 0x41c87565,
        "privacyValueAllowCloseFriends": 0xf7e8d89b,
        "privacyValueAllowPremium": 0xece9814b,
        "privacyValueAllowBots": 0x21461b5d,
        "privacyValueDisallowBots": 0xf6a5f82f,
    },
    "ProfileTab": {
        "profileTabPosts": 0xb98cd696,
        "profileTabGifts": 0x4d4bd46a,
        "profileTabMedia": 0x72c64955,
        "profileTabFiles": 0xab339c00,
        "profileTabMusic": 0x9f27d26e,
        "profileTabVoice": 0xe477092e,
        "profileTabLinks": 0xd3656499,
        "profileTabGifs": 0xa2c0f695,
    },
    "PublicForward": {
        "publicForwardMessage": 0x1f2bf4a,
        "publicForwardStory": 0xedf3add0,
    },
    "QuickReply": {
        "quickReply": 0x697102b,
    },
    "Reaction": {
        "reactionEmpty": 0x79f5d419,
        "reactionEmoji": 0x1b2286b8,
        "reactionCustomEmoji": 0x8935fc73,
        "reactionPaid": 0x523da4eb,
    },
    "ReactionCount": {
        "reactionCount": 0xa3d1cb80,
    },
    "ReactionNotificationsFrom": {
        "reactionNotificationsFromContacts": 0xbac3a61a,
        "reactionNotificationsFromAll": 0x4b9e22a0,
    },
    "ReactionsNotifySettings": {
        "reactionsNotifySettings": 0x71e4ea58,
    },
    "ReadParticipantDate": {
        "readParticipantDate": 0x4a4ff172,
    },
    "ReceivedNotifyMessage": {
        "receivedNotifyMessage": 0xa384b779,
    },
    "RecentMeUrl": {
        "recentMeUrlUnknown": 0x46e1d13d,
        "recentMeUrlUser": 0xb92c09e2,
        "recentMeUrlChat": 0xb2da71d2,
        "recentMeUrlChatInvite": 0xeb49081d,
        "recentMeUrlStickerSet": 0xbc0a57dc,
    },
    "RecentStory": {
        "recentStory": 0x711d692d,
    },
    "ReplyMarkup": {
        "replyKeyboardHide": 0xa03e5b85,
        "replyKeyboardForceReply": 0x86b40b08,
        "replyKeyboardMarkup": 0x85dd99d1,
        "replyInlineMarkup": 0x48a30254,
    },
    "ReportReason": {
        "inputReportReasonSpam": 0x58dbcab8,
        "inputReportReasonViolence": 0x1e22c78d,
        "inputReportReasonPornography": 0x2e59d922,
        "inputReportReasonChildAbuse": 0xadf44ee3,
        "inputReportReasonOther": 0xc1e4a2b1,
        "inputReportReasonCopyright": 0x9b89f93a,
        "inputReportReasonGeoIrrelevant": 0xdbd4feed,
        "inputReportReasonFake": 0xf5ddd6e7,
        "inputReportReasonIllegalDrugs": 0xa8eb2be,
        "inputReportReasonPersonalDetails": 0x9ec7863d,
    },
    "ReportResult": {
        "reportResultChooseOption": 0xf0e4e0b6,
        "reportResultAddComment": 0x6f09ac31,
        "reportResultReported": 0x8db33c4b,
    },
    "RequestPeerType": {
        "requestPeerTypeUser": 0x5f3b8a00,
        "requestPeerTypeChat": 0xc9f06e1b,
        "requestPeerTypeBroadcast": 0x339bef6c,
        "requestPeerTypeCreateBot": 0x3e81e078,
    },
    "RequestedPeer": {
        "requestedPeerUser": 0xd62ff46a,
        "requestedPeerChat": 0x7307544f,
        "requestedPeerChannel": 0x8ba403e4,
    },
    "RequirementToContact": {
        "requirementToContactEmpty": 0x50a9839,
        "requirementToContactPremium": 0xe581e4e9,
        "requirementToContactPaidMessages": 0xb4f67e93,
    },
    "RestrictionReason": {
        "restrictionReason": 0xd072acb4,
    },
    "RichMessage": {
        "richMessage": 0xbaf39d8b,
    },
    "RichText": {
        "textEmpty": 0xdc3d824f,
        "textPlain": 0x744694e0,
        "textBold": 0x6724abc4,
        "textItalic": 0xd912a59c,
        "textUnderline": 0xc12622c4,
        "textStrike": 0x9bf8bb95,
        "textFixed": 0x6c3f19b9,
        "textUrl": 0x3c2884c1,
        "textEmail": 0xde5a0dd6,
        "textConcat": 0x7e6260d7,
        "textSubscript": 0xed6a8504,
        "textSuperscript": 0xc7fb5e01,
        "textMarked": 0x34b8621,
        "textPhone": 0x1ccb966a,
        "textImage": 0x81ccf4f,
        "textAnchor": 0x35553762,
        "textMath": 0x9d2eac97,
        "textCustomEmoji": 0xa26156c0,
        "textSpoiler": 0x4c2a5d62,
        "textMention": 0xcd24cf44,
        "textHashtag": 0x519524ea,
        "textBotCommand": 0x2ff29d3,
        "textCashtag": 0x7b9e1801,
        "textAutoUrl": 0xac6a83aa,
        "textAutoEmail": 0xc556a45d,
        "textAutoPhone": 0x24c26789,
        "textBankCard": 0xb956812d,
        "textMentionName": 0x1a9fbfc,
        "textDate": 0xa5b45e2b,
    },
    "SavedContact": {
        "savedPhoneContact": 0x1142bd56,
    },
    "SavedDialog": {
        "savedDialog": 0xbd87cb6c,
        "monoForumDialog": 0x64407ea7,
    },
    "SavedReactionTag": {
        "savedReactionTag": 0xcb6ff828,
    },
    "SavedStarGift": {
        "savedStarGift": 0x41df43fc,
    },
    "SearchPostsFlood": {
        "searchPostsFlood": 0x3e0b5b6a,
    },
    "SearchResultsCalendarPeriod": {
        "searchResultsCalendarPeriod": 0xc9b0539f,
    },
    "SearchResultsPosition": {
        "searchResultPosition": 0x7f648b67,
    },
    "SecureCredentialsEncrypted": {
        "secureCredentialsEncrypted": 0x33f0ea47,
    },
    "SecureData": {
        "secureData": 0x8aeabec3,
    },
    "SecureFile": {
        "secureFileEmpty": 0x64199744,
        "secureFile": 0x7d09c27e,
    },
    "SecurePasswordKdfAlgo": {
        "securePasswordKdfAlgoUnknown": 0x4a8537,
        "securePasswordKdfAlgoPBKDF2HMACSHA512iter100000": 0xbbf2dda0,
        "securePasswordKdfAlgoSHA512": 0x86471d92,
    },
    "SecurePlainData": {
        "securePlainPhone": 0x7d6099dd,
        "securePlainEmail": 0x21ec5a5f,
    },
    "SecureRequiredType": {
        "secureRequiredType": 0x829d99da,
        "secureRequiredTypeOneOf": 0x27477b4,
    },
    "SecureSecretSettings": {
        "secureSecretSettings": 0x1527bcac,
    },
    "SecureValue": {
        "secureValue": 0x187fa0ca,
    },
    "SecureValueError": {
        "secureValueErrorData": 0xe8a40bd9,
        "secureValueErrorFrontSide": 0xbe3dfa,
        "secureValueErrorReverseSide": 0x868a2aa5,
        "secureValueErrorSelfie": 0xe537ced6,
        "secureValueErrorFile": 0x7a700873,
        "secureValueErrorFiles": 0x666220e9,
        "secureValueError": 0x869d758f,
        "secureValueErrorTranslationFile": 0xa1144770,
        "secureValueErrorTranslationFiles": 0x34636dd8,
    },
    "SecureValueHash": {
        "secureValueHash": 0xed1ecdb0,
    },
    "SecureValueType": {
        "secureValueTypePersonalDetails": 0x9d2a81e3,
        "secureValueTypePassport": 0x3dac6a00,
        "secureValueTypeDriverLicense": 0x6e425c4,
        "secureValueTypeIdentityCard": 0xa0d0744b,
        "secureValueTypeInternalPassport": 0x99a48f23,
        "secureValueTypeAddress": 0xcbe31e26,
        "secureValueTypeUtilityBill": 0xfc36954e,
        "secureValueTypeBankStatement": 0x89137c0d,
        "secureValueTypeRentalAgreement": 0x8b883488,
        "secureValueTypePassportRegistration": 0x99e3806a,
        "secureValueTypeTemporaryRegistration": 0xea02ec33,
        "secureValueTypePhone": 0xb320aadb,
        "secureValueTypeEmail": 0x8e3ca7ee,
    },
    "SendAsPeer": {
        "sendAsPeer": 0xb81c7034,
    },
    "SendMessageAction": {
        "sendMessageTypingAction": 0x16bf744e,
        "sendMessageCancelAction": 0xfd5ec8f5,
        "sendMessageRecordVideoAction": 0xa187d66f,
        "sendMessageUploadVideoAction": 0xe9763aec,
        "sendMessageRecordAudioAction": 0xd52f73f7,
        "sendMessageUploadAudioAction": 0xf351d7ab,
        "sendMessageUploadPhotoAction": 0xd1d34a26,
        "sendMessageUploadDocumentAction": 0xaa0cd9e4,
        "sendMessageGeoLocationAction": 0x176f8ba1,
        "sendMessageChooseContactAction": 0x628cbc6f,
        "sendMessageGamePlayAction": 0xdd6a8f48,
        "sendMessageRecordRoundAction": 0x88f27fbc,
        "sendMessageUploadRoundAction": 0x243e1c66,
        "speakingInGroupCallAction": 0xd92c2285,
        "sendMessageHistoryImportAction": 0xdbda9246,
        "sendMessageChooseStickerAction": 0xb05ac6b1,
        "sendMessageEmojiInteraction": 0x25972bcb,
        "sendMessageEmojiInteractionSeen": 0xb665902e,
        "sendMessageTextDraftAction": 0x376d975c,
        "inputSendMessageRichMessageDraftAction": 0xe2b23b51,
        "sendMessageRichMessageDraftAction": 0xa2cb24f9,
    },
    "ShippingOption": {
        "shippingOption": 0xb6213cdf,
    },
    "SmsJob": {
        "smsJob": 0xe6a1eeb8,
    },
    "SponsoredMessage": {
        "sponsoredMessage": 0x7dbf8673,
    },
    "SponsoredMessageReportOption": {
        "sponsoredMessageReportOption": 0x430d3150,
    },
    "SponsoredPeer": {
        "sponsoredPeer": 0xc69708d3,
    },
    "StarGift": {
        "starGift": 0x313a9547,
        "starGiftUnique": 0x85f0a9cd,
    },
    "StarGiftActiveAuctionState": {
        "starGiftActiveAuctionState": 0xd31bc45d,
    },
    "StarGiftAttribute": {
        "starGiftAttributeModel": 0x565251e2,
        "starGiftAttributePattern": 0x4e7085ea,
        "starGiftAttributeBackdrop": 0x9f2504e4,
        "starGiftAttributeOriginalDetails": 0xe0bff26c,
    },
    "StarGiftAttributeCounter": {
        "starGiftAttributeCounter": 0x2eb1b658,
    },
    "StarGiftAttributeId": {
        "starGiftAttributeIdModel": 0x48aaae3c,
        "starGiftAttributeIdPattern": 0x4a162433,
        "starGiftAttributeIdBackdrop": 0x1f01c757,
    },
    "StarGiftAttributeRarity": {
        "starGiftAttributeRarity": 0x36437737,
        "starGiftAttributeRarityUncommon": 0xdbce6389,
        "starGiftAttributeRarityRare": 0xf08d516b,
        "starGiftAttributeRarityEpic": 0x78fbf3a8,
        "starGiftAttributeRarityLegendary": 0xcef7e7a8,
    },
    "StarGiftAuctionAcquiredGift": {
        "starGiftAuctionAcquiredGift": 0x42b00348,
    },
    "StarGiftAuctionRound": {
        "starGiftAuctionRound": 0x3aae0528,
        "starGiftAuctionRoundExtendable": 0xaa021e5,
    },
    "StarGiftAuctionState": {
        "starGiftAuctionStateNotModified": 0xfe333952,
        "starGiftAuctionState": 0x771a4e66,
        "starGiftAuctionStateFinished": 0x972dabbf,
    },
    "StarGiftAuctionUserState": {
        "starGiftAuctionUserState": 0x2eeed1c4,
    },
    "StarGiftBackground": {
        "starGiftBackground": 0xaff56398,
    },
    "StarGiftCollection": {
        "starGiftCollection": 0x9d6b13b0,
    },
    "StarGiftUpgradePrice": {
        "starGiftUpgradePrice": 0x99ea331d,
    },
    "StarRefProgram": {
        "starRefProgram": 0xdd0c66f2,
    },
    "StarsAmount": {
        "starsAmount": 0xbbb6b4a3,
        "starsTonAmount": 0x74aee3e0,
    },
    "StarsGiftOption": {
        "starsGiftOption": 0x5e0589f1,
    },
    "StarsGiveawayOption": {
        "starsGiveawayOption": 0x94ce852a,
    },
    "StarsGiveawayWinnersOption": {
        "starsGiveawayWinnersOption": 0x54236209,
    },
    "StarsRating": {
        "starsRating": 0x1b0e4f07,
    },
    "StarsRevenueStatus": {
        "starsRevenueStatus": 0xfebe5491,
    },
    "StarsSubscription": {
        "starsSubscription": 0x2e6eab1a,
    },
    "StarsSubscriptionPricing": {
        "starsSubscriptionPricing": 0x5416d58,
    },
    "StarsTopupOption": {
        "starsTopupOption": 0xbd915c0,
    },
    "StarsTransaction": {
        "starsTransaction": 0x13659eb0,
    },
    "StarsTransactionPeer": {
        "starsTransactionPeerUnsupported": 0x95f2bfe4,
        "starsTransactionPeerAppStore": 0xb457b375,
        "starsTransactionPeerPlayMarket": 0x7b560a0b,
        "starsTransactionPeerPremiumBot": 0x250dbaf8,
        "starsTransactionPeerFragment": 0xe92fd902,
        "starsTransactionPeer": 0xd80da15d,
        "starsTransactionPeerAds": 0x60682812,
        "starsTransactionPeerAPI": 0xf9677aad,
    },
    "StatsAbsValueAndPrev": {
        "statsAbsValueAndPrev": 0xcb43acde,
    },
    "StatsDateRangeDays": {
        "statsDateRangeDays": 0xb637edaf,
    },
    "StatsGraph": {
        "statsGraphAsync": 0x4a27eb2d,
        "statsGraphError": 0xbedc9822,
        "statsGraph": 0x8ea464b6,
    },
    "StatsGroupTopAdmin": {
        "statsGroupTopAdmin": 0xd7584c87,
    },
    "StatsGroupTopInviter": {
        "statsGroupTopInviter": 0x535f779d,
    },
    "StatsGroupTopPoster": {
        "statsGroupTopPoster": 0x9d04af9b,
    },
    "StatsPercentValue": {
        "statsPercentValue": 0xcbce2fe0,
    },
    "StatsURL": {
        "statsURL": 0x47a971e0,
    },
    "StickerKeyword": {
        "stickerKeyword": 0xfcfeb29c,
    },
    "StickerPack": {
        "stickerPack": 0x12b299d4,
    },
    "StickerSet": {
        "stickerSet": 0x2dd14edc,
    },
    "StickerSetCovered": {
        "stickerSetCovered": 0x6410a5d2,
        "stickerSetMultiCovered": 0x3407e51b,
        "stickerSetFullCovered": 0x40d13c0e,
        "stickerSetNoCovered": 0x77b15d1c,
    },
    "StoriesStealthMode": {
        "storiesStealthMode": 0x712e27fd,
    },
    "StoryAlbum": {
        "storyAlbum": 0x9325705a,
    },
    "StoryFwdHeader": {
        "storyFwdHeader": 0xb826e150,
    },
    "StoryItem": {
        "storyItemDeleted": 0x51e6ee4f,
        "storyItemSkipped": 0xffadc913,
        "storyItem": 0x16a4b93c,
    },
    "StoryReaction": {
        "storyReaction": 0x6090d6d5,
        "storyReactionPublicForward": 0xbbab2643,
        "storyReactionPublicRepost": 0xcfcd0f13,
    },
    "StoryView": {
        "storyView": 0xb0bdeac5,
        "storyViewPublicForward": 0x9083670b,
        "storyViewPublicRepost": 0xbd74cf49,
    },
    "StoryViews": {
        "storyViews": 0x8d595cd6,
    },
    "SuggestedPost": {
        "suggestedPost": 0xe8e37e5,
    },
    "TextWithEntities": {
        "textWithEntities": 0x751f3146,
    },
    "Theme": {
        "theme": 0xa00e67d6,
    },
    "ThemeSettings": {
        "themeSettings": 0xfa58b6d4,
    },
    "Timezone": {
        "timezone": 0xff9289f5,
    },
    "TodoCompletion": {
        "todoCompletion": 0x221bb5e4,
    },
    "TodoItem": {
        "todoItem": 0xcba9a52f,
    },
    "TodoList": {
        "todoList": 0x49b92a26,
    },
    "TopPeer": {
        "topPeer": 0xedcdc05b,
    },
    "TopPeerCategory": {
        "topPeerCategoryBotsPM": 0xab661b5b,
        "topPeerCategoryBotsInline": 0x148677e2,
        "topPeerCategoryCorrespondents": 0x637b7ed,
        "topPeerCategoryGroups": 0xbd17a14a,
        "topPeerCategoryChannels": 0x161d9628,
        "topPeerCategoryPhoneCalls": 0x1e76a78c,
        "topPeerCategoryForwardUsers": 0xa8406ca9,
        "topPeerCategoryForwardChats": 0xfbeec0f0,
        "topPeerCategoryBotsApp": 0xfd9e7bec,
        "topPeerCategoryBotsGuestChat": 0x6c24f3dd,
    },
    "TopPeerCategoryPeers": {
        "topPeerCategoryPeers": 0xfb834291,
    },
    "True": {
        "true": 0x3fedd339,
    },
    "Update": {
        "updateNewMessage": 0x1f2b0afd,
        "updateMessageID": 0x4e90bfd6,
        "updateDeleteMessages": 0xa20db0e5,
        "updateUserTyping": 0x2a17bf5c,
        "updateChatUserTyping": 0x83487af0,
        "updateChatParticipants": 0x7761198,
        "updateUserStatus": 0xe5bdf8de,
        "updateUserName": 0xa7848924,
        "updateNewAuthorization": 0x8951abef,
        "updateNewEncryptedMessage": 0x12bcbd9a,
        "updateEncryptedChatTyping": 0x1710f156,
        "updateEncryption": 0xb4a2e88d,
        "updateEncryptedMessagesRead": 0x38fe25b7,
        "updateChatParticipantAdd": 0x3dda5451,
        "updateChatParticipantDelete": 0xe32f3d77,
        "updateDcOptions": 0x8e5e9873,
        "updateNotifySettings": 0xbec268ef,
        "updateServiceNotification": 0xebe46819,
        "updatePrivacy": 0xee3b272a,
        "updateUserPhone": 0x5492a13,
        "updateReadHistoryInbox": 0x9e84bc99,
        "updateReadHistoryOutbox": 0x2f2f21bf,
        "updateWebPage": 0x7f891213,
        "updateReadMessagesContents": 0xf8227181,
        "updateChannelTooLong": 0x108d941f,
        "updateChannel": 0x635b4c09,
        "updateNewChannelMessage": 0x62ba04d9,
        "updateReadChannelInbox": 0x922e6e10,
        "updateDeleteChannelMessages": 0xc32d5b12,
        "updateChannelMessageViews": 0xf226ac08,
        "updateChatParticipantAdmin": 0xd7ca61a2,
        "updateNewStickerSet": 0x688a30aa,
        "updateStickerSetsOrder": 0xbb2d201,
        "updateStickerSets": 0x31c24808,
        "updateSavedGifs": 0x9375341e,
        "updateBotInlineQuery": 0x496f379c,
        "updateBotInlineSend": 0x12f12a07,
        "updateEditChannelMessage": 0x1b3f4df7,
        "updateBotCallbackQuery": 0xb9cfc48d,
        "updateEditMessage": 0xe40370a3,
        "updateInlineBotCallbackQuery": 0x691e9052,
        "updateReadChannelOutbox": 0xb75f99a9,
        "updateDraftMessage": 0xedfc111e,
        "updateReadFeaturedStickers": 0x571d2742,
        "updateRecentStickers": 0x9a422c20,
        "updateConfig": 0xa229dd06,
        "updatePtsChanged": 0x3354678f,
        "updateChannelWebPage": 0x2f2ba99f,
        "updateDialogPinned": 0x6e6fe51c,
        "updatePinnedDialogs": 0xfa0f3ca2,
        "updateBotWebhookJSON": 0x8317c0c3,
        "updateBotWebhookJSONQuery": 0x9b9240a6,
        "updateBotShippingQuery": 0xb5aefd7d,
        "updateBotPrecheckoutQuery": 0x8caa9a96,
        "updatePhoneCall": 0xab0f6b1e,
        "updateLangPackTooLong": 0x46560264,
        "updateLangPack": 0x56022f4d,
        "updateFavedStickers": 0xe511996d,
        "updateChannelReadMessagesContents": 0x25f324f7,
        "updateContactsReset": 0x7084a7be,
        "updateChannelAvailableMessages": 0xb23fc698,
        "updateDialogUnreadMark": 0xb658f23e,
        "updateMessagePoll": 0xd64c522b,
        "updateChatDefaultBannedRights": 0x54c01850,
        "updateFolderPeers": 0x19360dc0,
        "updatePeerSettings": 0x6a7e7366,
        "updatePeerLocated": 0xb4afcfb0,
        "updateNewScheduledMessage": 0x39a51dfb,
        "updateDeleteScheduledMessages": 0xf2a71983,
        "updateTheme": 0x8216fba3,
        "updateGeoLiveViewed": 0x871fb939,
        "updateLoginToken": 0x564fe691,
        "updateMessagePollVote": 0x7699f014,
        "updateDialogFilter": 0x26ffde7d,
        "updateDialogFilterOrder": 0xa5d72105,
        "updateDialogFilters": 0x3504914f,
        "updatePhoneCallSignalingData": 0x2661bf09,
        "updateChannelMessageForwards": 0xd29a27f4,
        "updateReadChannelDiscussionInbox": 0xd6b19546,
        "updateReadChannelDiscussionOutbox": 0x695c9e7c,
        "updatePeerBlocked": 0xebe07752,
        "updateChannelUserTyping": 0x8c88c923,
        "updatePinnedMessages": 0xed85eab5,
        "updatePinnedChannelMessages": 0x5bb98608,
        "updateChat": 0xf89a6a4e,
        "updateGroupCallParticipants": 0xf2ebdb4e,
        "updateGroupCall": 0x9d2216e0,
        "updatePeerHistoryTTL": 0xbb9bb9a5,
        "updateChatParticipant": 0xd087663a,
        "updateChannelParticipant": 0x985d3abb,
        "updateBotStopped": 0xc4870a49,
        "updateGroupCallConnection": 0xb783982,
        "updateBotCommands": 0x4d712f2e,
        "updatePendingJoinRequests": 0x7063c3db,
        "updateBotChatInviteRequester": 0x7cb34d79,
        "updateMessageReactions": 0x1e297bfa,
        "updateAttachMenuBots": 0x17b7a20b,
        "updateWebViewResultSent": 0x1592b79d,
        "updateBotMenuButton": 0x14b85813,
        "updateSavedRingtones": 0x74d8be99,
        "updateTranscribedAudio": 0x84cd5a,
        "updateReadFeaturedEmojiStickers": 0xfb4c496c,
        "updateUserEmojiStatus": 0x28373599,
        "updateRecentEmojiStatuses": 0x30f443db,
        "updateRecentReactions": 0x6f7863f4,
        "updateMoveStickerSetToTop": 0x86fccf85,
        "updateMessageExtendedMedia": 0xd5a41724,
        "updateUser": 0x20529438,
        "updateAutoSaveSettings": 0xec05b097,
        "updateStory": 0x75b3b798,
        "updateReadStories": 0xf74e932b,
        "updateStoryID": 0x1bf335b9,
        "updateStoriesStealthMode": 0x2c084dc1,
        "updateSentStoryReaction": 0x7d627683,
        "updateBotChatBoost": 0x904dd49c,
        "updateChannelViewForumAsMessages": 0x7b68920,
        "updatePeerWallpaper": 0xae3f101d,
        "updateBotMessageReaction": 0xac21d3ce,
        "updateBotMessageReactions": 0x9cb7759,
        "updateSavedDialogPinned": 0xaeaf9e74,
        "updatePinnedSavedDialogs": 0x686c85a6,
        "updateSavedReactionTags": 0x39c67432,
        "updateSmsJob": 0xf16269d4,
        "updateQuickReplies": 0xf9470ab2,
        "updateNewQuickReply": 0xf53da717,
        "updateDeleteQuickReply": 0x53e6f1ec,
        "updateQuickReplyMessage": 0x3e050d0f,
        "updateDeleteQuickReplyMessages": 0x566fe7cd,
        "updateBotBusinessConnect": 0x8ae5c97a,
        "updateBotNewBusinessMessage": 0x9ddb347c,
        "updateBotEditBusinessMessage": 0x7df587c,
        "updateBotDeleteBusinessMessage": 0xa02a982e,
        "updateNewStoryReaction": 0x1824e40b,
        "updateStarsBalance": 0x4e80a379,
        "updateBusinessBotCallbackQuery": 0x1ea2fda7,
        "updateStarsRevenueStatus": 0xa584b019,
        "updateBotPurchasedPaidMedia": 0x283bd312,
        "updatePaidReactionPrivacy": 0x8b725fce,
        "updateSentPhoneCode": 0x504aa18f,
        "updateGroupCallChainBlocks": 0xa477288f,
        "updateReadMonoForumInbox": 0x77b0e372,
        "updateReadMonoForumOutbox": 0xa4a79376,
        "updateMonoForumNoPaidException": 0x9f812b08,
        "updateGroupCallMessage": 0xd8326f0d,
        "updateGroupCallEncryptedMessage": 0xc957a766,
        "updatePinnedForumTopic": 0x683b2c52,
        "updatePinnedForumTopics": 0xdef143d0,
        "updateDeleteGroupCallMessages": 0x3e85e92c,
        "updateStarGiftAuctionState": 0x48e246c2,
        "updateStarGiftAuctionUserState": 0xdc58f31e,
        "updateEmojiGameInfo": 0xfb9c547a,
        "updateStarGiftCraftFail": 0xac072444,
        "updateChatParticipantRank": 0xbd8367b9,
        "updateManagedBot": 0x4880ed9a,
        "updateBotGuestChatQuery": 0xcdd4093d,
        "updateAiComposeTones": 0x8c0f91fb,
        "updateJoinChatWebViewDecision": 0xbdac7e70,
        "updateNewBotConnection": 0xb22083a6,
        "updateWebBrowserSettings": 0xc39a2ade,
        "updateWebBrowserException": 0x140502d1,
    },
    "Updates": {
        "updatesTooLong": 0xe317af7e,
        "updateShortMessage": 0x313bc7f8,
        "updateShortChatMessage": 0x4d6deea5,
        "updateShort": 0x78d4dec1,
        "updatesCombined": 0x725b04c3,
        "updates": 0x74ae4240,
        "updateShortSentMessage": 0x9015e101,
    },
    "UrlAuthResult": {
        "urlAuthResultRequest": 0x3cd623ec,
        "urlAuthResultAccepted": 0x623a8fa0,
        "urlAuthResultDefault": 0xa9d6db1f,
    },
    "User": {
        "userEmpty": 0xd3bc4b7a,
        "user": 0x31774388,
    },
    "UserFull": {
        "userFull": 0x6cbe645,
    },
    "UserProfilePhoto": {
        "userProfilePhotoEmpty": 0x4f11bae1,
        "userProfilePhoto": 0x82d1f706,
    },
    "UserStatus": {
        "userStatusEmpty": 0x9d05049,
        "userStatusOnline": 0xedb93949,
        "userStatusOffline": 0x8c703f,
        "userStatusRecently": 0x7b197dc8,
        "userStatusLastWeek": 0x541a1d1a,
        "userStatusLastMonth": 0x65899777,
    },
    "Username": {
        "username": 0xb4073647,
    },
    "VideoSize": {
        "videoSize": 0xde33b094,
        "videoSizeEmojiMarkup": 0xf85c413c,
        "videoSizeStickerMarkup": 0xda082fe,
    },
    "WallPaper": {
        "wallPaper": 0xa437c3ed,
        "wallPaperNoFile": 0xe0804116,
    },
    "WallPaperSettings": {
        "wallPaperSettings": 0x372efcd0,
    },
    "WebAuthorization": {
        "webAuthorization": 0xa6f8f452,
    },
    "WebDocument": {
        "webDocument": 0x1c570ed1,
        "webDocumentNoProxy": 0xf9c8bcc6,
    },
    "WebDomainException": {
        "webDomainException": 0x933ca597,
    },
    "WebPage": {
        "webPageEmpty": 0x211a1788,
        "webPagePending": 0xb0d13e47,
        "webPage": 0xe89c45b2,
        "webPageNotModified": 0x7311ca11,
    },
    "WebPageAttribute": {
        "webPageAttributeTheme": 0x54b56617,
        "webPageAttributeStory": 0x2e94c3e7,
        "webPageAttributeStickerSet": 0x50cc03d3,
        "webPageAttributeUniqueStarGift": 0xcf6f6db8,
        "webPageAttributeStarGiftCollection": 0x31cad303,
        "webPageAttributeStarGiftAuction": 0x1c641c2,
        "webPageAttributeAiComposeTone": 0x7781fe18,
    },
    "WebViewMessageSent": {
        "webViewMessageSent": 0xc94511c,
    },
    "WebViewResult": {
        "webViewResultUrl": 0x4d22ff98,
    },
    "X": {
        "invokeAfterMsgs": 0x3dc4b4f0,
        "initConnection": 0xc1cd5ea9,
        "invokeWithLayer": 0xda9b0d0d,
        "invokeWithoutUpdates": 0xbf9459b7,
        "invokeWithMessagesRange": 0x365275f2,
        "invokeWithTakeout": 0xaca9fd2e,
        "invokeWithBusinessConnection": 0xdd289f8e,
        "invokeWithGooglePlayIntegrity": 0x1df92984,
        "invokeWithApnsSecret": 0x0dae54f8,
        "invokeWithReCaptcha": 0xadbb0f94,
    },
}

FUNCTIONS = {
    "account.acceptAuthorization": 0xf3ed4c73,  # → Bool
    "account.cancelPasswordEmail": 0xc1cbd5b6,  # → Bool
    "account.changeAuthorizationSettings": 0x40f48462,  # → Bool
    "account.changePhone": 0x70c32edb,  # → User
    "account.checkUsername": 0x2714d86c,  # → Bool
    "account.clearRecentEmojiStatuses": 0x18201aae,  # → Bool
    "account.confirmBotConnection": 0x67ed1f68,  # → Bool
    "account.confirmPasswordEmail": 0x8fdf1920,  # → Bool
    "account.confirmPhone": 0x5f2178c3,  # → Bool
    "account.createBusinessChatLink": 0x8851e68e,  # → BusinessChatLink
    "account.createTheme": 0x652e4400,  # → Theme
    "account.declinePasswordReset": 0x4c9409f6,  # → Bool
    "account.deleteAccount": 0xa2c0cf74,  # → Bool
    "account.deleteAutoSaveExceptions": 0x53bc0020,  # → Bool
    "account.deleteBusinessChatLink": 0x60073674,  # → Bool
    "account.deletePasskey": 0xf5b5563f,  # → Bool
    "account.deleteSecureValue": 0xb880bc4b,  # → Bool
    "account.disablePeerConnectedBot": 0x5e437ed9,  # → Bool
    "account.editBusinessChatLink": 0x8c3410af,  # → BusinessChatLink
    "account.finishTakeoutSession": 0x1d2652ee,  # → Bool
    "account.getAccountTTL": 0x8fc711d,  # → AccountDaysTTL
    "account.getBotBusinessConnection": 0x76a86270,  # → Updates
    "account.getChannelRestrictedStatusEmojis": 0x35a9e0d5,  # → EmojiList
    "account.getContactSignUpNotification": 0x9f07c728,  # → Bool
    "account.getDefaultBackgroundEmojis": 0xa60ab9ce,  # → EmojiList
    "account.getDefaultGroupPhotoEmojis": 0x915860ae,  # → EmojiList
    "account.getDefaultProfilePhotoEmojis": 0xe2750328,  # → EmojiList
    "account.getGlobalPrivacySettings": 0xeb2b4cf6,  # → GlobalPrivacySettings
    "account.getNotifyExceptions": 0x53577479,  # → Updates
    "account.getNotifySettings": 0x12b3ad31,  # → PeerNotifySettings
    "account.getReactionsNotifySettings": 0x6dd654c,  # → ReactionsNotifySettings
    "account.getTheme": 0x3a5869ec,  # → Theme
    "account.getWallPaper": 0xfc8ddbea,  # → WallPaper
    "account.installTheme": 0xc727bb3b,  # → Bool
    "account.installWallPaper": 0xfeed5769,  # → Bool
    "account.invalidateSignInCodes": 0xca8ae8ba,  # → Bool
    "account.registerDevice": 0xec86017a,  # → Bool
    "account.registerPasskey": 0x55b41fd6,  # → Passkey
    "account.reorderUsernames": 0xef500eab,  # → Bool
    "account.reportPeer": 0xc5ba3d86,  # → Bool
    "account.reportProfilePhoto": 0xfa8cc6f5,  # → Bool
    "account.resendPasswordEmail": 0x7a7f2a15,  # → Bool
    "account.resetAuthorization": 0xdf77f3bc,  # → Bool
    "account.resetNotifySettings": 0xdb7e1747,  # → Bool
    "account.resetWallPapers": 0xbb3b9804,  # → Bool
    "account.resetWebAuthorization": 0x2d01b9ef,  # → Bool
    "account.resetWebAuthorizations": 0x682d2594,  # → Bool
    "account.saveAutoDownloadSettings": 0x76f36233,  # → Bool
    "account.saveAutoSaveSettings": 0xd69b8361,  # → Bool
    "account.saveMusic": 0xb26732a9,  # → Bool
    "account.saveSecureValue": 0x899fe31d,  # → SecureValue
    "account.saveTheme": 0xf257106c,  # → Bool
    "account.saveWallPaper": 0x6c5a5b37,  # → Bool
    "account.setAccountTTL": 0x2442485e,  # → Bool
    "account.setAuthorizationTTL": 0xbf899aa0,  # → Bool
    "account.setContactSignUpNotification": 0xcff43f61,  # → Bool
    "account.setContentSettings": 0xb574b16b,  # → Bool
    "account.setGlobalPrivacySettings": 0x1edaaac2,  # → GlobalPrivacySettings
    "account.setMainProfileTab": 0x5dee78b0,  # → Bool
    "account.setReactionsNotifySettings": 0x316ce548,  # → ReactionsNotifySettings
    "account.toggleConnectedBotPaused": 0x646e1097,  # → Bool
    "account.toggleNoPaidMessagesException": 0xfe2eda76,  # → Bool
    "account.toggleSponsoredMessages": 0xb9d9a38d,  # → Bool
    "account.toggleUsername": 0x58d6b376,  # → Bool
    "account.toggleWebBrowserSettingsException": 0x60ed4229,  # → Updates
    "account.unregisterDevice": 0x6a0d3206,  # → Bool
    "account.updateBirthday": 0xcc6e0c11,  # → Bool
    "account.updateBusinessAwayMessage": 0xa26a7fa5,  # → Bool
    "account.updateBusinessGreetingMessage": 0x66cdafc4,  # → Bool
    "account.updateBusinessIntro": 0xa614d034,  # → Bool
    "account.updateBusinessLocation": 0x9e6b131a,  # → Bool
    "account.updateBusinessWorkHours": 0x4b00e066,  # → Bool
    "account.updateColor": 0x684d214e,  # → Bool
    "account.updateConnectedBot": 0x66a08c7e,  # → Updates
    "account.updateDeviceLocked": 0x38df3532,  # → Bool
    "account.updateEmojiStatus": 0xfbd3de6b,  # → Bool
    "account.updateNotifySettings": 0x84be5b93,  # → Bool
    "account.updatePasswordSettings": 0xa59b102f,  # → Bool
    "account.updatePersonalChannel": 0xd94305e0,  # → Bool
    "account.updateProfile": 0x78515775,  # → User
    "account.updateStatus": 0x6628562c,  # → Bool
    "account.updateTheme": 0x2bf40ccc,  # → Theme
    "account.updateUsername": 0x3e0bdd7c,  # → User
    "account.uploadRingtone": 0x831a83a2,  # → Document
    "account.uploadTheme": 0x1c3db333,  # → Document
    "account.uploadWallPaper": 0xe39a8f03,  # → WallPaper
    "account.verifyPhone": 0x4dd3a7f6,  # → Bool
    "aicompose.createTone": 0x4aa83913,  # → AiComposeTone
    "aicompose.deleteTone": 0xdd39316a,  # → Bool
    "aicompose.getToneExample": 0xd1b4ab14,  # → AiComposeToneExample
    "aicompose.saveTone": 0x1782cbb1,  # → Bool
    "aicompose.updateTone": 0x903bcf59,  # → AiComposeTone
    "auth.acceptLoginToken": 0xe894ad4d,  # → Authorization
    "auth.bindTempAuthKey": 0xcdd42a05,  # → Bool
    "auth.cancelCode": 0x1f040578,  # → Bool
    "auth.checkRecoveryPassword": 0xd36bf79,  # → Bool
    "auth.dropTempAuthKeys": 0x8e48a188,  # → Bool
    "auth.reportMissingCode": 0xcb9deff6,  # → Bool
    "auth.requestFirebaseSms": 0x8e39261e,  # → Bool
    "auth.resetAuthorizations": 0x9fab0d1a,  # → Bool
    "bots.addPreviewMedia": 0x17aeb75a,  # → BotPreviewMedia
    "bots.allowSendMessage": 0xf132e3ef,  # → Updates
    "bots.answerWebhookJSONQuery": 0xe6213f4d,  # → Bool
    "bots.canSendMessage": 0x1359f4e6,  # → Bool
    "bots.checkDownloadFileParams": 0x50077589,  # → Bool
    "bots.checkUsername": 0x87f2219b,  # → Bool
    "bots.createBot": 0xe5b17f2b,  # → User
    "bots.deletePreviewMedia": 0x2d0135b3,  # → Bool
    "bots.editAccessSettings": 0x31813cd8,  # → Bool
    "bots.editPreviewMedia": 0x8525606f,  # → BotPreviewMedia
    "bots.getBotMenuButton": 0x9c60eb28,  # → BotMenuButton
    "bots.getRequestedWebViewButton": 0xbf25b7f3,  # → KeyboardButton
    "bots.invokeWebViewCustomMethod": 0x87fc5e7,  # → DataJSON
    "bots.reorderPreviewMedias": 0xb627f3aa,  # → Bool
    "bots.reorderUsernames": 0x9709b1c2,  # → Bool
    "bots.resetBotCommands": 0x3d8de0f9,  # → Bool
    "bots.sendCustomRequest": 0xaa2769ed,  # → DataJSON
    "bots.setBotBroadcastDefaultAdminRights": 0x788464e1,  # → Bool
    "bots.setBotCommands": 0x517165a,  # → Bool
    "bots.setBotGroupDefaultAdminRights": 0x925ec9ea,  # → Bool
    "bots.setBotInfo": 0x10cf3123,  # → Bool
    "bots.setBotMenuButton": 0x4504d54f,  # → Bool
    "bots.setCustomVerification": 0x8b89dfbd,  # → Bool
    "bots.setJoinChatResults": 0xe71a4810,  # → Bool
    "bots.toggleUserEmojiStatusPermission": 0x6de6392,  # → Bool
    "bots.toggleUsername": 0x53ca973,  # → Bool
    "bots.updateStarRefProgram": 0x778b5ab3,  # → StarRefProgram
    "bots.updateUserEmojiStatus": 0xed9f30c5,  # → Bool
    "channels.checkSearchPostsFlood": 0x22567115,  # → SearchPostsFlood
    "channels.checkUsername": 0x10e6bd2c,  # → Bool
    "channels.convertToGigagroup": 0xb290c69,  # → Updates
    "channels.createChannel": 0x91006707,  # → Updates
    "channels.deactivateAllUsernames": 0xa245dd3,  # → Bool
    "channels.deleteChannel": 0xc0111fe3,  # → Updates
    "channels.deleteHistory": 0x9baa9647,  # → Updates
    "channels.editAdmin": 0x9a98ad68,  # → Updates
    "channels.editBanned": 0x96e6cd81,  # → Updates
    "channels.editLocation": 0x58e63f6d,  # → Bool
    "channels.editPhoto": 0xf12e57c9,  # → Updates
    "channels.editTitle": 0x566decd0,  # → Updates
    "channels.exportMessageLink": 0xe63fadeb,  # → ExportedMessageLink
    "channels.getMessageAuthor": 0xece2a0e6,  # → User
    "channels.leaveChannel": 0xf836aa95,  # → Updates
    "channels.readHistory": 0xcc104937,  # → Bool
    "channels.readMessageContents": 0xeab5dc38,  # → Bool
    "channels.reorderUsernames": 0xb45ced1d,  # → Bool
    "channels.reportAntiSpamFalsePositive": 0xa850a693,  # → Bool
    "channels.reportSpam": 0xf44a8315,  # → Bool
    "channels.restrictSponsoredMessages": 0x9ae91519,  # → Updates
    "channels.setBoostsToUnblockRestrictions": 0xad399cee,  # → Updates
    "channels.setDiscussionGroup": 0x40582bb2,  # → Bool
    "channels.setEmojiStickers": 0x3cd930b7,  # → Bool
    "channels.setMainProfileTab": 0x3583fcb1,  # → Bool
    "channels.setStickers": 0xea8ca4f9,  # → Bool
    "channels.toggleAntiSpam": 0x68f3e4eb,  # → Updates
    "channels.toggleAutotranslation": 0x167fc0a1,  # → Updates
    "channels.toggleForum": 0x3ff75734,  # → Updates
    "channels.toggleJoinRequest": 0xecc2618,  # → Updates
    "channels.toggleJoinToSend": 0xe4cb9580,  # → Updates
    "channels.toggleParticipantsHidden": 0x6a6e7854,  # → Updates
    "channels.togglePreHistoryHidden": 0xeabbb94c,  # → Updates
    "channels.toggleSignatures": 0x418d549c,  # → Updates
    "channels.toggleSlowMode": 0xedd49ef0,  # → Updates
    "channels.toggleUsername": 0x50f24105,  # → Bool
    "channels.toggleViewForumAsMessages": 0x9738bb15,  # → Updates
    "channels.updateColor": 0xd8aa3671,  # → Updates
    "channels.updateEmojiStatus": 0xf0d3e6a8,  # → Updates
    "channels.updatePaidMessagesPrice": 0x4b12327b,  # → Updates
    "channels.updateUsername": 0x3514b3de,  # → Bool
    "chatlists.deleteExportedInvite": 0x719c5c5e,  # → Bool
    "chatlists.editExportedInvite": 0x653db63d,  # → ExportedChatlistInvite
    "chatlists.hideChatlistUpdates": 0x66e486fb,  # → Bool
    "chatlists.joinChatlistInvite": 0xa6b1e39a,  # → Updates
    "chatlists.joinChatlistUpdates": 0xe089f8f5,  # → Updates
    "chatlists.leaveChatlist": 0x74fae13a,  # → Updates
    "contacts.acceptContact": 0xf831a20f,  # → Updates
    "contacts.addContact": 0xd9ba2e54,  # → Updates
    "contacts.block": 0x2e2e8734,  # → Bool
    "contacts.blockFromReplies": 0x29a8962c,  # → Updates
    "contacts.deleteByPhones": 0x1013fd9e,  # → Bool
    "contacts.deleteContacts": 0x96a0e00,  # → Updates
    "contacts.editCloseFriends": 0xba6705f0,  # → Bool
    "contacts.exportContactToken": 0xf8654027,  # → ExportedContactToken
    "contacts.getLocated": 0xd348bc44,  # → Updates
    "contacts.importContactToken": 0x13005788,  # → User
    "contacts.resetSaved": 0x879537f1,  # → Bool
    "contacts.resetTopPeerRating": 0x1ae373ac,  # → Bool
    "contacts.setBlocked": 0x94c65c76,  # → Bool
    "contacts.toggleTopPeers": 0x8514bdda,  # → Bool
    "contacts.unblock": 0xb550d328,  # → Bool
    "contacts.updateContactNote": 0x139f63fb,  # → Bool
    "folders.editPeerFolders": 0x6847d0ab,  # → Updates
    "help.acceptTermsOfService": 0xee72f79a,  # → Bool
    "help.dismissSuggestion": 0xf50dbaa1,  # → Bool
    "help.getCdnConfig": 0x52029342,  # → CdnConfig
    "help.getConfig": 0xc4f9186b,  # → Config
    "help.getNearestDc": 0x1fb33026,  # → NearestDc
    "help.hidePromoData": 0x1e251c95,  # → Bool
    "help.saveAppLog": 0x6f02f748,  # → Bool
    "help.setBotUpdatesStatus": 0xec22cfcd,  # → Bool
    "langpack.getDifference": 0xcd984aa5,  # → LangPackDifference
    "langpack.getLangPack": 0xf2f2330a,  # → LangPackDifference
    "langpack.getLanguage": 0x6a596502,  # → LangPackLanguage
    "messages.acceptEncryption": 0x3dbc0415,  # → EncryptedChat
    "messages.acceptUrlAuth": 0x67a3f0de,  # → UrlAuthResult
    "messages.addPollAnswer": 0x19bc4b6d,  # → Updates
    "messages.appendTodoList": 0x21a61057,  # → Updates
    "messages.checkChatInvite": 0x3eadb1bb,  # → ChatInvite
    "messages.checkQuickReplyShortcut": 0xf1d0fbd3,  # → Bool
    "messages.checkUrlAuthMatchCode": 0xc9a47b0b,  # → Bool
    "messages.clearAllDrafts": 0x7e58ee9c,  # → Bool
    "messages.clearRecentReactions": 0x9dfeefb4,  # → Bool
    "messages.clearRecentStickers": 0x8999602d,  # → Bool
    "messages.clickSponsoredMessage": 0x8235057e,  # → Bool
    "messages.createForumTopic": 0x2f98c3d5,  # → Updates
    "messages.declineUrlAuth": 0x35436bbc,  # → Bool
    "messages.deleteChat": 0x5bd0ee50,  # → Bool
    "messages.deleteChatUser": 0xa2185cab,  # → Updates
    "messages.deleteExportedChatInvite": 0xd464a42b,  # → Bool
    "messages.deleteFactCheck": 0xd1da940c,  # → Updates
    "messages.deleteParticipantReaction": 0xe3b7f82c,  # → Updates
    "messages.deleteParticipantReactions": 0xa0b80cf8,  # → Bool
    "messages.deletePollAnswer": 0xac8505a5,  # → Updates
    "messages.deleteQuickReplyMessages": 0xe105e910,  # → Updates
    "messages.deleteQuickReplyShortcut": 0x3cc04740,  # → Bool
    "messages.deleteRevokedExportedChatInvites": 0x56987bd5,  # → Bool
    "messages.deleteScheduledMessages": 0x59ae2b16,  # → Updates
    "messages.discardEncryption": 0xf393aea0,  # → Bool
    "messages.editChatAbout": 0xdef60797,  # → Bool
    "messages.editChatAdmin": 0xa85bd1c2,  # → Bool
    "messages.editChatCreator": 0xf743b857,  # → Updates
    "messages.editChatDefaultBannedRights": 0xa5866b41,  # → Updates
    "messages.editChatParticipantRank": 0xa00f32b0,  # → Updates
    "messages.editChatPhoto": 0x35ddd674,  # → Updates
    "messages.editChatTitle": 0x73783ffd,  # → Updates
    "messages.editFactCheck": 0x589ee75,  # → Updates
    "messages.editForumTopic": 0xcecc1134,  # → Updates
    "messages.editInlineBotMessage": 0xa423bb51,  # → Bool
    "messages.editMessage": 0xb106e66c,  # → Updates
    "messages.editQuickReplyShortcut": 0x5c003cef,  # → Bool
    "messages.exportChatInvite": 0xa455de90,  # → ExportedChatInvite
    "messages.faveSticker": 0xb9ffc55b,  # → Bool
    "messages.forwardMessages": 0x13704a7c,  # → Updates
    "messages.getAllDrafts": 0x6a3f8d65,  # → Updates
    "messages.getAttachMenuBot": 0x77216192,  # → AttachMenuBotsBot
    "messages.getAttachMenuBots": 0x16fcc2cb,  # → AttachMenuBots
    "messages.getDefaultHistoryTTL": 0x658b7188,  # → DefaultHistoryTTL
    "messages.getDocumentByHash": 0xb1f2061f,  # → Document
    "messages.getEmojiKeywords": 0x35a0e062,  # → EmojiKeywordsDifference
    "messages.getEmojiKeywordsDifference": 0x1508b6af,  # → EmojiKeywordsDifference
    "messages.getEmojiURL": 0xd5b10c26,  # → EmojiURL
    "messages.getExtendedMedia": 0x84f80814,  # → Updates
    "messages.getFutureChatCreatorAfterLeave": 0x3b7d0ea6,  # → User
    "messages.getMessagesReactions": 0x8bba90e6,  # → Updates
    "messages.getOnlines": 0x6e2be050,  # → ChatOnlines
    "messages.getOutboxReadDate": 0x8c4bfe5d,  # → OutboxReadDate
    "messages.getPaidReactionPrivacy": 0x472455aa,  # → Updates
    "messages.getPollResults": 0xeda3e33b,  # → Updates
    "messages.hideAllChatJoinRequests": 0xe085f4ea,  # → Updates
    "messages.hideChatJoinRequest": 0x7fe7e815,  # → Updates
    "messages.hidePeerSettingsBar": 0x4facb138,  # → Bool
    "messages.markDialogUnread": 0x8c5006f8,  # → Bool
    "messages.migrateChat": 0xa2875319,  # → Updates
    "messages.prolongWebView": 0xb0d81a83,  # → Bool
    "messages.rateTranscribedAudio": 0x7f1d072f,  # → Bool
    "messages.readDiscussion": 0xf731a9f4,  # → Bool
    "messages.readEncryptedHistory": 0x7f4b690a,  # → Bool
    "messages.readFeaturedStickers": 0x5b118126,  # → Bool
    "messages.readSavedHistory": 0xba4a3b5b,  # → Bool
    "messages.reorderPinnedDialogs": 0x3b1adf37,  # → Bool
    "messages.reorderPinnedForumTopics": 0xe7841f0,  # → Updates
    "messages.reorderPinnedSavedDialogs": 0x8b716587,  # → Bool
    "messages.reorderQuickReplies": 0x60331907,  # → Bool
    "messages.reorderStickerSets": 0x78337739,  # → Bool
    "messages.report": 0xfc78af9b,  # → ReportResult
    "messages.reportEncryptedSpam": 0x4b0c8c0f,  # → Bool
    "messages.reportMessagesDelivery": 0x5a6d7395,  # → Bool
    "messages.reportMusicListen": 0xddbcd819,  # → Bool
    "messages.reportReaction": 0x3f64c076,  # → Bool
    "messages.reportReadMetrics": 0x4067c5e6,  # → Bool
    "messages.reportSpam": 0xcf1592db,  # → Bool
    "messages.requestAppWebView": 0x53618bce,  # → WebViewResult
    "messages.requestEncryption": 0xf64daf43,  # → EncryptedChat
    "messages.requestMainWebView": 0xc9e01e7b,  # → WebViewResult
    "messages.requestSimpleWebView": 0x413a3e73,  # → WebViewResult
    "messages.requestUrlAuth": 0x894cc99c,  # → UrlAuthResult
    "messages.requestWebView": 0x269dc2c1,  # → WebViewResult
    "messages.saveDefaultSendAs": 0xccfddf96,  # → Bool
    "messages.saveDraft": 0xad0fa15c,  # → Bool
    "messages.saveGif": 0x327a30cb,  # → Bool
    "messages.saveRecentSticker": 0x392718f8,  # → Bool
    "messages.searchCustomEmoji": 0x2c11c0d7,  # → EmojiList
    "messages.sendBotRequestedPeer": 0x6c5cf2a7,  # → Updates
    "messages.sendInlineBotResult": 0xc0cf7646,  # → Updates
    "messages.sendMedia": 0x330e77f,  # → Updates
    "messages.sendMessage": 0xfef48f62,  # → Updates
    "messages.sendMultiMedia": 0x1bf89d74,  # → Updates
    "messages.sendPaidReaction": 0x58bbcb50,  # → Updates
    "messages.sendQuickReplyMessages": 0x6c750de1,  # → Updates
    "messages.sendReaction": 0xd30d78d4,  # → Updates
    "messages.sendScheduledMessages": 0xbd38850a,  # → Updates
    "messages.sendScreenshotNotification": 0xa1405817,  # → Updates
    "messages.sendVote": 0x10ea6184,  # → Updates
    "messages.sendWebViewData": 0xdc0242c8,  # → Updates
    "messages.sendWebViewResultMessage": 0xa4314f5,  # → WebViewMessageSent
    "messages.setBotCallbackAnswer": 0xd58f130a,  # → Bool
    "messages.setBotGuestChatResult": 0xb8f106e3,  # → InputBotInlineMessageID
    "messages.setBotPrecheckoutResults": 0x9c2dd95,  # → Bool
    "messages.setBotShippingResults": 0xe5f672fa,  # → Bool
    "messages.setChatAvailableReactions": 0x864b2581,  # → Updates
    "messages.setChatTheme": 0x81202c9,  # → Updates
    "messages.setChatWallPaper": 0x8ffacae1,  # → Updates
    "messages.setDefaultHistoryTTL": 0x9eb51445,  # → Bool
    "messages.setDefaultReaction": 0x4f47a016,  # → Bool
    "messages.setEncryptedTyping": 0x791451ed,  # → Bool
    "messages.setGameScore": 0x8ef8ecc0,  # → Updates
    "messages.setHistoryTTL": 0xb80e5fe4,  # → Updates
    "messages.setInlineBotResults": 0xbb12a419,  # → Bool
    "messages.setInlineGameScore": 0x15ad9f64,  # → Bool
    "messages.setTyping": 0x58943ee2,  # → Bool
    "messages.startBot": 0xe6df7378,  # → Updates
    "messages.startHistoryImport": 0xb43df344,  # → Bool
    "messages.summarizeText": 0xabbbd346,  # → TextWithEntities
    "messages.toggleBotInAttachMenu": 0x69f59d69,  # → Bool
    "messages.toggleDialogFilterTags": 0xfd2dda49,  # → Bool
    "messages.toggleDialogPin": 0xa731e257,  # → Bool
    "messages.toggleNoForwards": 0xb2081a35,  # → Updates
    "messages.togglePaidReactionPrivacy": 0x435885b5,  # → Bool
    "messages.togglePeerTranslations": 0xe47cb579,  # → Bool
    "messages.toggleSavedDialogPin": 0xac81bbde,  # → Bool
    "messages.toggleStickerSets": 0xb5052fea,  # → Bool
    "messages.toggleSuggestedPostApproval": 0x8107455c,  # → Updates
    "messages.toggleTodoCompleted": 0xd3e03124,  # → Updates
    "messages.uninstallStickerSet": 0xf96e55de,  # → Bool
    "messages.updateDialogFilter": 0x1ad4a04a,  # → Bool
    "messages.updateDialogFiltersOrder": 0xc563c1e4,  # → Bool
    "messages.updatePinnedForumTopic": 0x175df251,  # → Updates
    "messages.updatePinnedMessage": 0xd2aaf7ec,  # → Updates
    "messages.updateSavedReactionTag": 0x60297dec,  # → Bool
    "messages.uploadEncryptedFile": 0x5057c497,  # → EncryptedFile
    "messages.uploadImportedMedia": 0x2a862092,  # → MessageMedia
    "messages.uploadMedia": 0x14967978,  # → MessageMedia
    "messages.viewSponsoredMessage": 0x269e3643,  # → Bool
    "payments.applyGiftCode": 0xf6e26854,  # → Updates
    "payments.assignAppStoreTransaction": 0x80ed747d,  # → Updates
    "payments.assignPlayMarketTransaction": 0xdffd50d3,  # → Updates
    "payments.botCancelStarsSubscription": 0x6dfa0622,  # → Bool
    "payments.canPurchaseStore": 0x4fdc5ea7,  # → Bool
    "payments.changeStarsSubscription": 0xc7770878,  # → Bool
    "payments.clearSavedInfo": 0xd83d70c1,  # → Bool
    "payments.convertStarGift": 0x74bf076b,  # → Bool
    "payments.craftStarGift": 0xb0f9684f,  # → Updates
    "payments.createStarGiftCollection": 0x1f4a0e87,  # → StarGiftCollection
    "payments.deleteStarGiftCollection": 0xad5648e8,  # → Bool
    "payments.fulfillStarsSubscription": 0xcc5bebb3,  # → Bool
    "payments.launchPrepaidGiveaway": 0x5ff58f20,  # → Updates
    "payments.refundStarsCharge": 0x25ae8f4a,  # → Updates
    "payments.reorderStarGiftCollections": 0xc32af4cc,  # → Bool
    "payments.resolveStarGiftOffer": 0xe9ce781c,  # → Updates
    "payments.saveStarGift": 0x2a2a697c,  # → Bool
    "payments.sendStarGiftOffer": 0x8fb86b41,  # → Updates
    "payments.toggleChatStarGiftNotifications": 0x60eaefa1,  # → Bool
    "payments.toggleStarGiftsPinnedToTop": 0x1513e7b0,  # → Bool
    "payments.transferStarGift": 0x7f18176a,  # → Updates
    "payments.updateStarGiftCollection": 0x4fddbee7,  # → StarGiftCollection
    "payments.updateStarGiftPrice": 0xedbe6ccb,  # → Updates
    "payments.upgradeStarGift": 0xaed6e4f5,  # → Updates
    "phone.createConferenceCall": 0x7d0444bb,  # → Updates
    "phone.createGroupCall": 0x48cdc6d8,  # → Updates
    "phone.declineConferenceCallInvite": 0x3c479971,  # → Updates
    "phone.deleteConferenceCallParticipants": 0x8ca60525,  # → Updates
    "phone.deleteGroupCallMessages": 0xf64f54f7,  # → Updates
    "phone.deleteGroupCallParticipantMessages": 0x1dbfeca0,  # → Updates
    "phone.discardCall": 0xb2cbc1c0,  # → Updates
    "phone.discardGroupCall": 0x7a777135,  # → Updates
    "phone.editGroupCallParticipant": 0xa5273abf,  # → Updates
    "phone.editGroupCallTitle": 0x1ca6ac0a,  # → Updates
    "phone.getCallConfig": 0x55451fa9,  # → DataJSON
    "phone.getGroupCallChainBlocks": 0xee9f88a6,  # → Updates
    "phone.inviteConferenceCallParticipant": 0xbcf22685,  # → Updates
    "phone.inviteToGroupCall": 0x7b393160,  # → Updates
    "phone.joinGroupCall": 0x8fb53057,  # → Updates
    "phone.joinGroupCallPresentation": 0xcbea6bc4,  # → Updates
    "phone.leaveGroupCall": 0x500377f9,  # → Updates
    "phone.leaveGroupCallPresentation": 0x1c50d144,  # → Updates
    "phone.receivedCall": 0x17d54f61,  # → Bool
    "phone.saveCallDebug": 0x277add7e,  # → Bool
    "phone.saveCallLog": 0x41248786,  # → Bool
    "phone.saveDefaultGroupCallJoinAs": 0x575e1f8c,  # → Bool
    "phone.saveDefaultSendAs": 0x4167add1,  # → Bool
    "phone.sendConferenceCallBroadcast": 0xc6701900,  # → Updates
    "phone.sendGroupCallEncryptedMessage": 0xe5afa56d,  # → Bool
    "phone.sendGroupCallMessage": 0xb1d11410,  # → Updates
    "phone.sendSignalingData": 0xff7a9383,  # → Bool
    "phone.setCallRating": 0x59ead627,  # → Updates
    "phone.startScheduledGroupCall": 0x5680e342,  # → Updates
    "phone.toggleGroupCallRecord": 0xf128c708,  # → Updates
    "phone.toggleGroupCallSettings": 0x974392f2,  # → Updates
    "phone.toggleGroupCallStartSubscription": 0x219c34e6,  # → Updates
    "smsjobs.finishJob": 0x4f1ebf24,  # → Bool
    "smsjobs.getSmsJob": 0x778d902f,  # → SmsJob
    "smsjobs.join": 0xa74ece2d,  # → Bool
    "smsjobs.leave": 0x9898ad73,  # → Bool
    "smsjobs.updateSettings": 0x93fa0bf,  # → Bool
    "stats.loadAsyncGraph": 0x621d5fa0,  # → StatsGraph
    "stickers.checkShortName": 0x284b3639,  # → Bool
    "stickers.deleteStickerSet": 0x87704394,  # → Bool
    "stories.activateStealthMode": 0x57bbd166,  # → Updates
    "stories.createAlbum": 0xa36396e5,  # → StoryAlbum
    "stories.deleteAlbum": 0x8d3456d0,  # → Bool
    "stories.editStory": 0x2c63a72b,  # → Updates
    "stories.exportStoryLink": 0x7b8def20,  # → ExportedStoryLink
    "stories.getAllReadPeerStories": 0x9b5ae7f9,  # → Updates
    "stories.incrementStoryViews": 0xb2028afb,  # → Bool
    "stories.reorderAlbums": 0x8535fbd9,  # → Bool
    "stories.report": 0x19d8eb45,  # → ReportResult
    "stories.sendReaction": 0x7fd736b2,  # → Updates
    "stories.sendStory": 0x8f9e6898,  # → Updates
    "stories.startLive": 0xd069ccde,  # → Updates
    "stories.toggleAllStoriesHidden": 0x7c2557c4,  # → Bool
    "stories.togglePeerStoriesHidden": 0xbd0415c4,  # → Bool
    "stories.togglePinnedToTop": 0xb297e9b,  # → Bool
    "stories.updateAlbum": 0x5e5259b6,  # → StoryAlbum
    "upload.saveBigFilePart": 0xde7b673d,  # → Bool
    "upload.saveFilePart": 0xb304a621,  # → Bool
    "users.setSecureValueErrors": 0x90c894b5,  # → Bool
    "users.suggestBirthday": 0xfc533372,  # → Updates
}

TL_SCHEMA = {
    "accountDaysTTL": [
        {"name": "days", "tl_type": "int"},
    ],
    "aiComposeTone": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "creator", "tl_type": "true", "cond": 0},
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "slug", "tl_type": "string"},
        {"name": "title", "tl_type": "string"},
        {"name": "emoji_id", "tl_type": "long", "cond": 1},
        {"name": "prompt", "tl_type": "string", "cond": 4},
        {"name": "installs_count", "tl_type": "int", "cond": 2},
        {"name": "author_id", "tl_type": "long", "cond": 3},
        {"name": "example_english", "tl_type": "AiComposeToneExample", "cond": 5},
    ],
    "aiComposeToneDefault": [
        {"name": "tone", "tl_type": "string"},
        {"name": "emoji_id", "tl_type": "long"},
        {"name": "title", "tl_type": "string"},
    ],
    "aiComposeToneExample": [
        {"name": "from", "tl_type": "TextWithEntities"},
        {"name": "to", "tl_type": "TextWithEntities"},
    ],
    "attachMenuBot": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "inactive", "tl_type": "true", "cond": 0},
        {"name": "has_settings", "tl_type": "true", "cond": 1},
        {"name": "request_write_access", "tl_type": "true", "cond": 2},
        {"name": "show_in_attach_menu", "tl_type": "true", "cond": 3},
        {"name": "show_in_side_menu", "tl_type": "true", "cond": 4},
        {"name": "side_menu_disclaimer_needed", "tl_type": "true", "cond": 5},
        {"name": "bot_id", "tl_type": "long"},
        {"name": "short_name", "tl_type": "string"},
        {"name": "peer_types", "tl_type": "Vector", "cond": 3},
        {"name": "icons", "tl_type": "Vector"},
    ],
    "attachMenuBotIcon": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "name", "tl_type": "string"},
        {"name": "icon", "tl_type": "Document"},
        {"name": "colors", "tl_type": "Vector", "cond": 0},
    ],
    "attachMenuBotIconColor": [
        {"name": "name", "tl_type": "string"},
        {"name": "color", "tl_type": "int"},
    ],
    "attachMenuBots": [
        {"name": "hash", "tl_type": "long"},
        {"name": "bots", "tl_type": "Vector"},
        {"name": "users", "tl_type": "Vector"},
    ],
    "attachMenuBotsBot": [
        {"name": "bot", "tl_type": "AttachMenuBot"},
        {"name": "users", "tl_type": "Vector"},
    ],
    "auctionBidLevel": [
        {"name": "pos", "tl_type": "int"},
        {"name": "amount", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
    ],
    "authorization": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "current", "tl_type": "true", "cond": 0},
        {"name": "official_app", "tl_type": "true", "cond": 1},
        {"name": "password_pending", "tl_type": "true", "cond": 2},
        {"name": "encrypted_requests_disabled", "tl_type": "true", "cond": 3},
        {"name": "call_requests_disabled", "tl_type": "true", "cond": 4},
        {"name": "unconfirmed", "tl_type": "true", "cond": 5},
        {"name": "hash", "tl_type": "long"},
        {"name": "device_model", "tl_type": "string"},
        {"name": "platform", "tl_type": "string"},
        {"name": "system_version", "tl_type": "string"},
        {"name": "api_id", "tl_type": "int"},
        {"name": "app_name", "tl_type": "string"},
        {"name": "app_version", "tl_type": "string"},
        {"name": "date_created", "tl_type": "int"},
        {"name": "date_active", "tl_type": "int"},
        {"name": "ip", "tl_type": "string"},
        {"name": "country", "tl_type": "string"},
        {"name": "region", "tl_type": "string"},
    ],
    "autoDownloadSettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "disabled", "tl_type": "true", "cond": 0},
        {"name": "video_preload_large", "tl_type": "true", "cond": 1},
        {"name": "audio_preload_next", "tl_type": "true", "cond": 2},
        {"name": "phonecalls_less_data", "tl_type": "true", "cond": 3},
        {"name": "stories_preload", "tl_type": "true", "cond": 4},
        {"name": "photo_size_max", "tl_type": "int"},
        {"name": "video_size_max", "tl_type": "long"},
        {"name": "file_size_max", "tl_type": "long"},
        {"name": "video_upload_maxbitrate", "tl_type": "int"},
        {"name": "small_queue_active_operations_max", "tl_type": "int"},
        {"name": "large_queue_active_operations_max", "tl_type": "int"},
    ],
    "autoSaveException": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "settings", "tl_type": "AutoSaveSettings"},
    ],
    "autoSaveSettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "photos", "tl_type": "true", "cond": 0},
        {"name": "videos", "tl_type": "true", "cond": 1},
        {"name": "video_max_size", "tl_type": "long", "cond": 2},
    ],
    "availableEffect": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "premium_required", "tl_type": "true", "cond": 2},
        {"name": "id", "tl_type": "long"},
        {"name": "emoticon", "tl_type": "string"},
        {"name": "static_icon_id", "tl_type": "long", "cond": 0},
        {"name": "effect_sticker_id", "tl_type": "long"},
        {"name": "effect_animation_id", "tl_type": "long", "cond": 1},
    ],
    "availableReaction": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "inactive", "tl_type": "true", "cond": 0},
        {"name": "premium", "tl_type": "true", "cond": 2},
        {"name": "reaction", "tl_type": "string"},
        {"name": "title", "tl_type": "string"},
        {"name": "static_icon", "tl_type": "Document"},
        {"name": "appear_animation", "tl_type": "Document"},
        {"name": "select_animation", "tl_type": "Document"},
        {"name": "activate_animation", "tl_type": "Document"},
        {"name": "effect_animation", "tl_type": "Document"},
        {"name": "around_animation", "tl_type": "Document", "cond": 1},
        {"name": "center_icon", "tl_type": "Document", "cond": 1},
    ],
    "bankCardOpenUrl": [
        {"name": "url", "tl_type": "string"},
        {"name": "name", "tl_type": "string"},
    ],
    "birthday": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "day", "tl_type": "int"},
        {"name": "month", "tl_type": "int"},
        {"name": "year", "tl_type": "int", "cond": 0},
    ],
    "boost": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "gift", "tl_type": "true", "cond": 1},
        {"name": "giveaway", "tl_type": "true", "cond": 2},
        {"name": "unclaimed", "tl_type": "true", "cond": 3},
        {"name": "id", "tl_type": "string"},
        {"name": "user_id", "tl_type": "long", "cond": 0},
        {"name": "giveaway_msg_id", "tl_type": "int", "cond": 2},
        {"name": "date", "tl_type": "int"},
        {"name": "expires", "tl_type": "int"},
        {"name": "used_gift_slug", "tl_type": "string", "cond": 4},
        {"name": "multiplier", "tl_type": "int", "cond": 5},
        {"name": "stars", "tl_type": "long", "cond": 6},
    ],
    "botApp": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "short_name", "tl_type": "string"},
        {"name": "title", "tl_type": "string"},
        {"name": "description", "tl_type": "string"},
        {"name": "photo", "tl_type": "Photo"},
        {"name": "document", "tl_type": "Document", "cond": 0},
        {"name": "hash", "tl_type": "long"},
    ],
    "botAppSettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "placeholder_path", "tl_type": "bytes", "cond": 0},
        {"name": "background_color", "tl_type": "int", "cond": 1},
        {"name": "background_dark_color", "tl_type": "int", "cond": 2},
        {"name": "header_color", "tl_type": "int", "cond": 3},
        {"name": "header_dark_color", "tl_type": "int", "cond": 4},
    ],
    "botBusinessConnection": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "disabled", "tl_type": "true", "cond": 1},
        {"name": "connection_id", "tl_type": "string"},
        {"name": "user_id", "tl_type": "long"},
        {"name": "dc_id", "tl_type": "int"},
        {"name": "date", "tl_type": "int"},
        {"name": "rights", "tl_type": "BusinessBotRights", "cond": 2},
    ],
    "botCommand": [
        {"name": "command", "tl_type": "string"},
        {"name": "description", "tl_type": "string"},
    ],
    "botCommandScopePeer": [
        {"name": "peer", "tl_type": "InputPeer"},
    ],
    "botCommandScopePeerAdmins": [
        {"name": "peer", "tl_type": "InputPeer"},
    ],
    "botCommandScopePeerUser": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "user_id", "tl_type": "InputUser"},
    ],
    "botInfo": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "has_preview_medias", "tl_type": "true", "cond": 6},
        {"name": "user_id", "tl_type": "long", "cond": 0},
        {"name": "description", "tl_type": "string", "cond": 1},
        {"name": "description_photo", "tl_type": "Photo", "cond": 4},
        {"name": "description_document", "tl_type": "Document", "cond": 5},
        {"name": "commands", "tl_type": "Vector", "cond": 2},
        {"name": "menu_button", "tl_type": "BotMenuButton", "cond": 3},
        {"name": "privacy_policy_url", "tl_type": "string", "cond": 7},
        {"name": "app_settings", "tl_type": "BotAppSettings", "cond": 8},
        {"name": "verifier_settings", "tl_type": "BotVerifierSettings", "cond": 9},
    ],
    "botInlineMessageMediaAuto": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "invert_media", "tl_type": "true", "cond": 3},
        {"name": "message", "tl_type": "string"},
        {"name": "entities", "tl_type": "Vector", "cond": 1},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
    ],
    "botInlineMessageText": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "no_webpage", "tl_type": "true", "cond": 0},
        {"name": "invert_media", "tl_type": "true", "cond": 3},
        {"name": "message", "tl_type": "string"},
        {"name": "entities", "tl_type": "Vector", "cond": 1},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
    ],
    "botInlineMessageMediaGeo": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "geo", "tl_type": "GeoPoint"},
        {"name": "heading", "tl_type": "int", "cond": 0},
        {"name": "period", "tl_type": "int", "cond": 1},
        {"name": "proximity_notification_radius", "tl_type": "int", "cond": 3},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
    ],
    "botInlineMessageMediaVenue": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "geo", "tl_type": "GeoPoint"},
        {"name": "title", "tl_type": "string"},
        {"name": "address", "tl_type": "string"},
        {"name": "provider", "tl_type": "string"},
        {"name": "venue_id", "tl_type": "string"},
        {"name": "venue_type", "tl_type": "string"},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
    ],
    "botInlineMessageMediaContact": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "phone_number", "tl_type": "string"},
        {"name": "first_name", "tl_type": "string"},
        {"name": "last_name", "tl_type": "string"},
        {"name": "vcard", "tl_type": "string"},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
    ],
    "botInlineMessageMediaInvoice": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "shipping_address_requested", "tl_type": "true", "cond": 1},
        {"name": "test", "tl_type": "true", "cond": 3},
        {"name": "title", "tl_type": "string"},
        {"name": "description", "tl_type": "string"},
        {"name": "photo", "tl_type": "WebDocument", "cond": 0},
        {"name": "currency", "tl_type": "string"},
        {"name": "total_amount", "tl_type": "long"},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
    ],
    "botInlineMessageMediaWebPage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "invert_media", "tl_type": "true", "cond": 3},
        {"name": "force_large_media", "tl_type": "true", "cond": 4},
        {"name": "force_small_media", "tl_type": "true", "cond": 5},
        {"name": "manual", "tl_type": "true", "cond": 7},
        {"name": "safe", "tl_type": "true", "cond": 8},
        {"name": "message", "tl_type": "string"},
        {"name": "entities", "tl_type": "Vector", "cond": 1},
        {"name": "url", "tl_type": "string"},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
    ],
    "botInlineMessageRichMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
        {"name": "rich_message", "tl_type": "RichMessage"},
    ],
    "botInlineResult": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "id", "tl_type": "string"},
        {"name": "type", "tl_type": "string"},
        {"name": "title", "tl_type": "string", "cond": 1},
        {"name": "description", "tl_type": "string", "cond": 2},
        {"name": "url", "tl_type": "string", "cond": 3},
        {"name": "thumb", "tl_type": "WebDocument", "cond": 4},
        {"name": "content", "tl_type": "WebDocument", "cond": 5},
        {"name": "send_message", "tl_type": "BotInlineMessage"},
    ],
    "botInlineMediaResult": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "id", "tl_type": "string"},
        {"name": "type", "tl_type": "string"},
        {"name": "photo", "tl_type": "Photo", "cond": 0},
        {"name": "document", "tl_type": "Document", "cond": 1},
        {"name": "title", "tl_type": "string", "cond": 2},
        {"name": "description", "tl_type": "string", "cond": 3},
        {"name": "send_message", "tl_type": "BotInlineMessage"},
    ],
    "botMenuButton": [
        {"name": "text", "tl_type": "string"},
        {"name": "url", "tl_type": "string"},
    ],
    "botPreviewMedia": [
        {"name": "date", "tl_type": "int"},
        {"name": "media", "tl_type": "MessageMedia"},
    ],
    "botVerification": [
        {"name": "bot_id", "tl_type": "long"},
        {"name": "icon", "tl_type": "long"},
        {"name": "description", "tl_type": "string"},
    ],
    "botVerifierSettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "can_modify_custom_description", "tl_type": "true", "cond": 1},
        {"name": "icon", "tl_type": "long"},
        {"name": "company", "tl_type": "string"},
        {"name": "custom_description", "tl_type": "string", "cond": 0},
    ],
    "businessAwayMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "offline_only", "tl_type": "true", "cond": 0},
        {"name": "shortcut_id", "tl_type": "int"},
        {"name": "schedule", "tl_type": "BusinessAwayMessageSchedule"},
        {"name": "recipients", "tl_type": "BusinessRecipients"},
    ],
    "businessAwayMessageScheduleCustom": [
        {"name": "start_date", "tl_type": "int"},
        {"name": "end_date", "tl_type": "int"},
    ],
    "businessBotRecipients": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "existing_chats", "tl_type": "true", "cond": 0},
        {"name": "new_chats", "tl_type": "true", "cond": 1},
        {"name": "contacts", "tl_type": "true", "cond": 2},
        {"name": "non_contacts", "tl_type": "true", "cond": 3},
        {"name": "exclude_selected", "tl_type": "true", "cond": 5},
        {"name": "users", "tl_type": "Vector", "cond": 4},
        {"name": "exclude_users", "tl_type": "Vector", "cond": 6},
    ],
    "businessBotRights": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "reply", "tl_type": "true", "cond": 0},
        {"name": "read_messages", "tl_type": "true", "cond": 1},
        {"name": "delete_sent_messages", "tl_type": "true", "cond": 2},
        {"name": "delete_received_messages", "tl_type": "true", "cond": 3},
        {"name": "edit_name", "tl_type": "true", "cond": 4},
        {"name": "edit_bio", "tl_type": "true", "cond": 5},
        {"name": "edit_profile_photo", "tl_type": "true", "cond": 6},
        {"name": "edit_username", "tl_type": "true", "cond": 7},
        {"name": "view_gifts", "tl_type": "true", "cond": 8},
        {"name": "sell_gifts", "tl_type": "true", "cond": 9},
        {"name": "change_gift_settings", "tl_type": "true", "cond": 10},
        {"name": "transfer_and_upgrade_gifts", "tl_type": "true", "cond": 11},
        {"name": "transfer_stars", "tl_type": "true", "cond": 12},
        {"name": "manage_stories", "tl_type": "true", "cond": 13},
    ],
    "businessChatLink": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "link", "tl_type": "string"},
        {"name": "message", "tl_type": "string"},
        {"name": "entities", "tl_type": "Vector", "cond": 0},
        {"name": "title", "tl_type": "string", "cond": 1},
        {"name": "views", "tl_type": "int"},
    ],
    "businessGreetingMessage": [
        {"name": "shortcut_id", "tl_type": "int"},
        {"name": "recipients", "tl_type": "BusinessRecipients"},
        {"name": "no_activity_days", "tl_type": "int"},
    ],
    "businessIntro": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "title", "tl_type": "string"},
        {"name": "description", "tl_type": "string"},
        {"name": "sticker", "tl_type": "Document", "cond": 0},
    ],
    "businessLocation": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "geo_point", "tl_type": "GeoPoint", "cond": 0},
        {"name": "address", "tl_type": "string"},
    ],
    "businessRecipients": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "existing_chats", "tl_type": "true", "cond": 0},
        {"name": "new_chats", "tl_type": "true", "cond": 1},
        {"name": "contacts", "tl_type": "true", "cond": 2},
        {"name": "non_contacts", "tl_type": "true", "cond": 3},
        {"name": "exclude_selected", "tl_type": "true", "cond": 5},
        {"name": "users", "tl_type": "Vector", "cond": 4},
    ],
    "businessWeeklyOpen": [
        {"name": "start_minute", "tl_type": "int"},
        {"name": "end_minute", "tl_type": "int"},
    ],
    "businessWorkHours": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "open_now", "tl_type": "true", "cond": 0},
        {"name": "timezone_id", "tl_type": "string"},
        {"name": "weekly_open", "tl_type": "Vector"},
    ],
    "cdnConfig": [
        {"name": "public_keys", "tl_type": "Vector"},
    ],
    "cdnPublicKey": [
        {"name": "dc_id", "tl_type": "int"},
        {"name": "public_key", "tl_type": "string"},
    ],
    "channelAdminLogEvent": [
        {"name": "id", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "user_id", "tl_type": "long"},
        {"name": "action", "tl_type": "ChannelAdminLogEventAction"},
    ],
    "channelAdminLogEventActionChangeTitle": [
        {"name": "prev_value", "tl_type": "string"},
        {"name": "new_value", "tl_type": "string"},
    ],
    "channelAdminLogEventActionChangeAbout": [
        {"name": "prev_value", "tl_type": "string"},
        {"name": "new_value", "tl_type": "string"},
    ],
    "channelAdminLogEventActionChangeUsername": [
        {"name": "prev_value", "tl_type": "string"},
        {"name": "new_value", "tl_type": "string"},
    ],
    "channelAdminLogEventActionChangePhoto": [
        {"name": "prev_photo", "tl_type": "Photo"},
        {"name": "new_photo", "tl_type": "Photo"},
    ],
    "channelAdminLogEventActionToggleInvites": [
        {"name": "new_value", "tl_type": "Bool"},
    ],
    "channelAdminLogEventActionToggleSignatures": [
        {"name": "new_value", "tl_type": "Bool"},
    ],
    "channelAdminLogEventActionUpdatePinned": [
        {"name": "message", "tl_type": "Message"},
    ],
    "channelAdminLogEventActionEditMessage": [
        {"name": "prev_message", "tl_type": "Message"},
        {"name": "new_message", "tl_type": "Message"},
    ],
    "channelAdminLogEventActionDeleteMessage": [
        {"name": "message", "tl_type": "Message"},
    ],
    "channelAdminLogEventActionParticipantInvite": [
        {"name": "participant", "tl_type": "ChannelParticipant"},
    ],
    "channelAdminLogEventActionParticipantToggleBan": [
        {"name": "prev_participant", "tl_type": "ChannelParticipant"},
        {"name": "new_participant", "tl_type": "ChannelParticipant"},
    ],
    "channelAdminLogEventActionParticipantToggleAdmin": [
        {"name": "prev_participant", "tl_type": "ChannelParticipant"},
        {"name": "new_participant", "tl_type": "ChannelParticipant"},
    ],
    "channelAdminLogEventActionChangeStickerSet": [
        {"name": "prev_stickerset", "tl_type": "InputStickerSet"},
        {"name": "new_stickerset", "tl_type": "InputStickerSet"},
    ],
    "channelAdminLogEventActionTogglePreHistoryHidden": [
        {"name": "new_value", "tl_type": "Bool"},
    ],
    "channelAdminLogEventActionDefaultBannedRights": [
        {"name": "prev_banned_rights", "tl_type": "ChatBannedRights"},
        {"name": "new_banned_rights", "tl_type": "ChatBannedRights"},
    ],
    "channelAdminLogEventActionStopPoll": [
        {"name": "message", "tl_type": "Message"},
    ],
    "channelAdminLogEventActionChangeLinkedChat": [
        {"name": "prev_value", "tl_type": "long"},
        {"name": "new_value", "tl_type": "long"},
    ],
    "channelAdminLogEventActionChangeLocation": [
        {"name": "prev_value", "tl_type": "ChannelLocation"},
        {"name": "new_value", "tl_type": "ChannelLocation"},
    ],
    "channelAdminLogEventActionToggleSlowMode": [
        {"name": "prev_value", "tl_type": "int"},
        {"name": "new_value", "tl_type": "int"},
    ],
    "channelAdminLogEventActionStartGroupCall": [
        {"name": "call", "tl_type": "InputGroupCall"},
    ],
    "channelAdminLogEventActionDiscardGroupCall": [
        {"name": "call", "tl_type": "InputGroupCall"},
    ],
    "channelAdminLogEventActionParticipantMute": [
        {"name": "participant", "tl_type": "GroupCallParticipant"},
    ],
    "channelAdminLogEventActionParticipantUnmute": [
        {"name": "participant", "tl_type": "GroupCallParticipant"},
    ],
    "channelAdminLogEventActionToggleGroupCallSetting": [
        {"name": "join_muted", "tl_type": "Bool"},
    ],
    "channelAdminLogEventActionParticipantJoinByInvite": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "via_chatlist", "tl_type": "true", "cond": 0},
        {"name": "invite", "tl_type": "ExportedChatInvite"},
    ],
    "channelAdminLogEventActionExportedInviteDelete": [
        {"name": "invite", "tl_type": "ExportedChatInvite"},
    ],
    "channelAdminLogEventActionExportedInviteRevoke": [
        {"name": "invite", "tl_type": "ExportedChatInvite"},
    ],
    "channelAdminLogEventActionExportedInviteEdit": [
        {"name": "prev_invite", "tl_type": "ExportedChatInvite"},
        {"name": "new_invite", "tl_type": "ExportedChatInvite"},
    ],
    "channelAdminLogEventActionParticipantVolume": [
        {"name": "participant", "tl_type": "GroupCallParticipant"},
    ],
    "channelAdminLogEventActionChangeHistoryTTL": [
        {"name": "prev_value", "tl_type": "int"},
        {"name": "new_value", "tl_type": "int"},
    ],
    "channelAdminLogEventActionParticipantJoinByRequest": [
        {"name": "invite", "tl_type": "ExportedChatInvite"},
        {"name": "approved_by", "tl_type": "long"},
    ],
    "channelAdminLogEventActionToggleNoForwards": [
        {"name": "new_value", "tl_type": "Bool"},
    ],
    "channelAdminLogEventActionSendMessage": [
        {"name": "message", "tl_type": "Message"},
    ],
    "channelAdminLogEventActionChangeAvailableReactions": [
        {"name": "prev_value", "tl_type": "ChatReactions"},
        {"name": "new_value", "tl_type": "ChatReactions"},
    ],
    "channelAdminLogEventActionChangeUsernames": [
        {"name": "prev_value", "tl_type": "Vector"},
        {"name": "new_value", "tl_type": "Vector"},
    ],
    "channelAdminLogEventActionToggleForum": [
        {"name": "new_value", "tl_type": "Bool"},
    ],
    "channelAdminLogEventActionCreateTopic": [
        {"name": "topic", "tl_type": "ForumTopic"},
    ],
    "channelAdminLogEventActionEditTopic": [
        {"name": "prev_topic", "tl_type": "ForumTopic"},
        {"name": "new_topic", "tl_type": "ForumTopic"},
    ],
    "channelAdminLogEventActionDeleteTopic": [
        {"name": "topic", "tl_type": "ForumTopic"},
    ],
    "channelAdminLogEventActionPinTopic": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "prev_topic", "tl_type": "ForumTopic", "cond": 0},
        {"name": "new_topic", "tl_type": "ForumTopic", "cond": 1},
    ],
    "channelAdminLogEventActionToggleAntiSpam": [
        {"name": "new_value", "tl_type": "Bool"},
    ],
    "channelAdminLogEventActionChangePeerColor": [
        {"name": "prev_value", "tl_type": "PeerColor"},
        {"name": "new_value", "tl_type": "PeerColor"},
    ],
    "channelAdminLogEventActionChangeProfilePeerColor": [
        {"name": "prev_value", "tl_type": "PeerColor"},
        {"name": "new_value", "tl_type": "PeerColor"},
    ],
    "channelAdminLogEventActionChangeWallpaper": [
        {"name": "prev_value", "tl_type": "WallPaper"},
        {"name": "new_value", "tl_type": "WallPaper"},
    ],
    "channelAdminLogEventActionChangeEmojiStatus": [
        {"name": "prev_value", "tl_type": "EmojiStatus"},
        {"name": "new_value", "tl_type": "EmojiStatus"},
    ],
    "channelAdminLogEventActionChangeEmojiStickerSet": [
        {"name": "prev_stickerset", "tl_type": "InputStickerSet"},
        {"name": "new_stickerset", "tl_type": "InputStickerSet"},
    ],
    "channelAdminLogEventActionToggleSignatureProfiles": [
        {"name": "new_value", "tl_type": "Bool"},
    ],
    "channelAdminLogEventActionParticipantSubExtend": [
        {"name": "prev_participant", "tl_type": "ChannelParticipant"},
        {"name": "new_participant", "tl_type": "ChannelParticipant"},
    ],
    "channelAdminLogEventActionToggleAutotranslation": [
        {"name": "new_value", "tl_type": "Bool"},
    ],
    "channelAdminLogEventActionParticipantEditRank": [
        {"name": "user_id", "tl_type": "long"},
        {"name": "prev_rank", "tl_type": "string"},
        {"name": "new_rank", "tl_type": "string"},
    ],
    "channelAdminLogEventsFilter": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "join", "tl_type": "true", "cond": 0},
        {"name": "leave", "tl_type": "true", "cond": 1},
        {"name": "invite", "tl_type": "true", "cond": 2},
        {"name": "ban", "tl_type": "true", "cond": 3},
        {"name": "unban", "tl_type": "true", "cond": 4},
        {"name": "kick", "tl_type": "true", "cond": 5},
        {"name": "unkick", "tl_type": "true", "cond": 6},
        {"name": "promote", "tl_type": "true", "cond": 7},
        {"name": "demote", "tl_type": "true", "cond": 8},
        {"name": "info", "tl_type": "true", "cond": 9},
        {"name": "settings", "tl_type": "true", "cond": 10},
        {"name": "pinned", "tl_type": "true", "cond": 11},
        {"name": "edit", "tl_type": "true", "cond": 12},
        {"name": "delete", "tl_type": "true", "cond": 13},
        {"name": "group_call", "tl_type": "true", "cond": 14},
        {"name": "invites", "tl_type": "true", "cond": 15},
        {"name": "send", "tl_type": "true", "cond": 16},
        {"name": "forums", "tl_type": "true", "cond": 17},
        {"name": "sub_extend", "tl_type": "true", "cond": 18},
        {"name": "edit_rank", "tl_type": "true", "cond": 19},
    ],
    "channelLocation": [
        {"name": "geo_point", "tl_type": "GeoPoint"},
        {"name": "address", "tl_type": "string"},
    ],
    "channelMessagesFilter": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "exclude_new_messages", "tl_type": "true", "cond": 1},
        {"name": "ranges", "tl_type": "Vector"},
    ],
    "channelParticipant": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "user_id", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "subscription_until_date", "tl_type": "int", "cond": 0},
        {"name": "rank", "tl_type": "string", "cond": 2},
    ],
    "channelParticipantSelf": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "via_request", "tl_type": "true", "cond": 0},
        {"name": "user_id", "tl_type": "long"},
        {"name": "inviter_id", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "subscription_until_date", "tl_type": "int", "cond": 1},
        {"name": "rank", "tl_type": "string", "cond": 2},
    ],
    "channelParticipantCreator": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "user_id", "tl_type": "long"},
        {"name": "admin_rights", "tl_type": "ChatAdminRights"},
        {"name": "rank", "tl_type": "string", "cond": 0},
    ],
    "channelParticipantAdmin": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "can_edit", "tl_type": "true", "cond": 0},
        {"name": "self", "tl_type": "true", "cond": 1},
        {"name": "user_id", "tl_type": "long"},
        {"name": "inviter_id", "tl_type": "long", "cond": 1},
        {"name": "promoted_by", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "admin_rights", "tl_type": "ChatAdminRights"},
        {"name": "rank", "tl_type": "string", "cond": 2},
    ],
    "channelParticipantBanned": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "left", "tl_type": "true", "cond": 0},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "kicked_by", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "banned_rights", "tl_type": "ChatBannedRights"},
        {"name": "rank", "tl_type": "string", "cond": 2},
    ],
    "channelParticipantLeft": [
        {"name": "peer", "tl_type": "Peer"},
    ],
    "channelParticipantsKicked": [
        {"name": "q", "tl_type": "string"},
    ],
    "channelParticipantsBanned": [
        {"name": "q", "tl_type": "string"},
    ],
    "channelParticipantsSearch": [
        {"name": "q", "tl_type": "string"},
    ],
    "channelParticipantsContacts": [
        {"name": "q", "tl_type": "string"},
    ],
    "channelParticipantsMentions": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "q", "tl_type": "string", "cond": 0},
        {"name": "top_msg_id", "tl_type": "int", "cond": 1},
    ],
    "chatEmpty": [
        {"name": "id", "tl_type": "long"},
    ],
    "chat": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "creator", "tl_type": "true", "cond": 0},
        {"name": "left", "tl_type": "true", "cond": 2},
        {"name": "deactivated", "tl_type": "true", "cond": 5},
        {"name": "call_active", "tl_type": "true", "cond": 23},
        {"name": "call_not_empty", "tl_type": "true", "cond": 24},
        {"name": "noforwards", "tl_type": "true", "cond": 25},
        {"name": "id", "tl_type": "long"},
        {"name": "title", "tl_type": "string"},
        {"name": "photo", "tl_type": "ChatPhoto"},
        {"name": "participants_count", "tl_type": "int"},
        {"name": "date", "tl_type": "int"},
        {"name": "version", "tl_type": "int"},
        {"name": "migrated_to", "tl_type": "InputChannel", "cond": 6},
        {"name": "admin_rights", "tl_type": "ChatAdminRights", "cond": 14},
        {"name": "default_banned_rights", "tl_type": "ChatBannedRights", "cond": 18},
    ],
    "chatForbidden": [
        {"name": "id", "tl_type": "long"},
        {"name": "title", "tl_type": "string"},
    ],
    "channel": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "creator", "tl_type": "true", "cond": 0},
        {"name": "left", "tl_type": "true", "cond": 2},
        {"name": "broadcast", "tl_type": "true", "cond": 5},
        {"name": "verified", "tl_type": "true", "cond": 7},
        {"name": "megagroup", "tl_type": "true", "cond": 8},
        {"name": "restricted", "tl_type": "true", "cond": 9},
        {"name": "signatures", "tl_type": "true", "cond": 11},
        {"name": "min", "tl_type": "true", "cond": 12},
        {"name": "scam", "tl_type": "true", "cond": 19},
        {"name": "has_link", "tl_type": "true", "cond": 20},
        {"name": "has_geo", "tl_type": "true", "cond": 21},
        {"name": "slowmode_enabled", "tl_type": "true", "cond": 22},
        {"name": "call_active", "tl_type": "true", "cond": 23},
        {"name": "call_not_empty", "tl_type": "true", "cond": 24},
        {"name": "fake", "tl_type": "true", "cond": 25},
        {"name": "gigagroup", "tl_type": "true", "cond": 26},
        {"name": "noforwards", "tl_type": "true", "cond": 27},
        {"name": "join_to_send", "tl_type": "true", "cond": 28},
        {"name": "join_request", "tl_type": "true", "cond": 29},
        {"name": "forum", "tl_type": "true", "cond": 30},
        {"name": "flags2", "tl_type": "flags", "is_flag": True},
        {"name": "stories_hidden", "tl_type": "flags2.1?true"},
        {"name": "stories_hidden_min", "tl_type": "flags2.2?true"},
        {"name": "stories_unavailable", "tl_type": "flags2.3?true"},
        {"name": "signature_profiles", "tl_type": "flags2.12?true"},
        {"name": "autotranslation", "tl_type": "flags2.15?true"},
        {"name": "broadcast_messages_allowed", "tl_type": "flags2.16?true"},
        {"name": "monoforum", "tl_type": "flags2.17?true"},
        {"name": "forum_tabs", "tl_type": "flags2.19?true"},
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long", "cond": 13},
        {"name": "title", "tl_type": "string"},
        {"name": "username", "tl_type": "string", "cond": 6},
        {"name": "photo", "tl_type": "ChatPhoto"},
        {"name": "date", "tl_type": "int"},
        {"name": "restriction_reason", "tl_type": "Vector", "cond": 9},
        {"name": "admin_rights", "tl_type": "ChatAdminRights", "cond": 14},
        {"name": "banned_rights", "tl_type": "ChatBannedRights", "cond": 15},
        {"name": "default_banned_rights", "tl_type": "ChatBannedRights", "cond": 18},
        {"name": "participants_count", "tl_type": "int", "cond": 17},
        {"name": "usernames", "tl_type": "flags2.0?Vector"},
        {"name": "stories_max_id", "tl_type": "flags2.4?RecentStory"},
        {"name": "color", "tl_type": "flags2.7?PeerColor"},
        {"name": "profile_color", "tl_type": "flags2.8?PeerColor"},
        {"name": "emoji_status", "tl_type": "flags2.9?EmojiStatus"},
        {"name": "level", "tl_type": "flags2.10?int"},
        {"name": "subscription_until_date", "tl_type": "flags2.11?int"},
        {"name": "bot_verification_icon", "tl_type": "flags2.13?long"},
        {"name": "send_paid_messages_stars", "tl_type": "flags2.14?long"},
        {"name": "linked_monoforum_id", "tl_type": "flags2.18?long"},
    ],
    "channelForbidden": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "broadcast", "tl_type": "true", "cond": 5},
        {"name": "megagroup", "tl_type": "true", "cond": 8},
        {"name": "monoforum", "tl_type": "true", "cond": 10},
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "title", "tl_type": "string"},
        {"name": "until_date", "tl_type": "int", "cond": 16},
    ],
    "chatAdminRights": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "change_info", "tl_type": "true", "cond": 0},
        {"name": "post_messages", "tl_type": "true", "cond": 1},
        {"name": "edit_messages", "tl_type": "true", "cond": 2},
        {"name": "delete_messages", "tl_type": "true", "cond": 3},
        {"name": "ban_users", "tl_type": "true", "cond": 4},
        {"name": "invite_users", "tl_type": "true", "cond": 5},
        {"name": "pin_messages", "tl_type": "true", "cond": 7},
        {"name": "add_admins", "tl_type": "true", "cond": 9},
        {"name": "anonymous", "tl_type": "true", "cond": 10},
        {"name": "manage_call", "tl_type": "true", "cond": 11},
        {"name": "other", "tl_type": "true", "cond": 12},
        {"name": "manage_topics", "tl_type": "true", "cond": 13},
        {"name": "post_stories", "tl_type": "true", "cond": 14},
        {"name": "edit_stories", "tl_type": "true", "cond": 15},
        {"name": "delete_stories", "tl_type": "true", "cond": 16},
        {"name": "manage_direct_messages", "tl_type": "true", "cond": 17},
        {"name": "manage_ranks", "tl_type": "true", "cond": 18},
    ],
    "chatAdminWithInvites": [
        {"name": "admin_id", "tl_type": "long"},
        {"name": "invites_count", "tl_type": "int"},
        {"name": "revoked_invites_count", "tl_type": "int"},
    ],
    "chatBannedRights": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "view_messages", "tl_type": "true", "cond": 0},
        {"name": "send_messages", "tl_type": "true", "cond": 1},
        {"name": "send_media", "tl_type": "true", "cond": 2},
        {"name": "send_stickers", "tl_type": "true", "cond": 3},
        {"name": "send_gifs", "tl_type": "true", "cond": 4},
        {"name": "send_games", "tl_type": "true", "cond": 5},
        {"name": "send_inline", "tl_type": "true", "cond": 6},
        {"name": "embed_links", "tl_type": "true", "cond": 7},
        {"name": "send_polls", "tl_type": "true", "cond": 8},
        {"name": "change_info", "tl_type": "true", "cond": 10},
        {"name": "invite_users", "tl_type": "true", "cond": 15},
        {"name": "pin_messages", "tl_type": "true", "cond": 17},
        {"name": "manage_topics", "tl_type": "true", "cond": 18},
        {"name": "send_photos", "tl_type": "true", "cond": 19},
        {"name": "send_videos", "tl_type": "true", "cond": 20},
        {"name": "send_roundvideos", "tl_type": "true", "cond": 21},
        {"name": "send_audios", "tl_type": "true", "cond": 22},
        {"name": "send_voices", "tl_type": "true", "cond": 23},
        {"name": "send_docs", "tl_type": "true", "cond": 24},
        {"name": "send_plain", "tl_type": "true", "cond": 25},
        {"name": "edit_rank", "tl_type": "true", "cond": 26},
        {"name": "send_reactions", "tl_type": "true", "cond": 27},
        {"name": "until_date", "tl_type": "int"},
    ],
    "chatFull": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "can_set_username", "tl_type": "true", "cond": 7},
        {"name": "has_scheduled", "tl_type": "true", "cond": 8},
        {"name": "translations_disabled", "tl_type": "true", "cond": 19},
        {"name": "id", "tl_type": "long"},
        {"name": "about", "tl_type": "string"},
        {"name": "participants", "tl_type": "ChatParticipants"},
        {"name": "chat_photo", "tl_type": "Photo", "cond": 2},
        {"name": "notify_settings", "tl_type": "PeerNotifySettings"},
        {"name": "exported_invite", "tl_type": "ExportedChatInvite", "cond": 13},
        {"name": "bot_info", "tl_type": "Vector", "cond": 3},
        {"name": "pinned_msg_id", "tl_type": "int", "cond": 6},
        {"name": "folder_id", "tl_type": "int", "cond": 11},
        {"name": "call", "tl_type": "InputGroupCall", "cond": 12},
        {"name": "ttl_period", "tl_type": "int", "cond": 14},
        {"name": "groupcall_default_join_as", "tl_type": "Peer", "cond": 15},
        {"name": "theme_emoticon", "tl_type": "string", "cond": 16},
        {"name": "requests_pending", "tl_type": "int", "cond": 17},
        {"name": "recent_requesters", "tl_type": "Vector", "cond": 17},
        {"name": "available_reactions", "tl_type": "ChatReactions", "cond": 18},
        {"name": "reactions_limit", "tl_type": "int", "cond": 20},
    ],
    "channelFull": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "can_view_participants", "tl_type": "true", "cond": 3},
        {"name": "can_set_username", "tl_type": "true", "cond": 6},
        {"name": "can_set_stickers", "tl_type": "true", "cond": 7},
        {"name": "hidden_prehistory", "tl_type": "true", "cond": 10},
        {"name": "can_set_location", "tl_type": "true", "cond": 16},
        {"name": "has_scheduled", "tl_type": "true", "cond": 19},
        {"name": "can_view_stats", "tl_type": "true", "cond": 20},
        {"name": "blocked", "tl_type": "true", "cond": 22},
        {"name": "flags2", "tl_type": "flags", "is_flag": True},
        {"name": "can_delete_channel", "tl_type": "flags2.0?true"},
        {"name": "antispam", "tl_type": "flags2.1?true"},
        {"name": "participants_hidden", "tl_type": "flags2.2?true"},
        {"name": "translations_disabled", "tl_type": "flags2.3?true"},
        {"name": "stories_pinned_available", "tl_type": "flags2.5?true"},
        {"name": "view_forum_as_messages", "tl_type": "flags2.6?true"},
        {"name": "restricted_sponsored", "tl_type": "flags2.11?true"},
        {"name": "can_view_revenue", "tl_type": "flags2.12?true"},
        {"name": "paid_media_allowed", "tl_type": "flags2.14?true"},
        {"name": "can_view_stars_revenue", "tl_type": "flags2.15?true"},
        {"name": "paid_reactions_available", "tl_type": "flags2.16?true"},
        {"name": "stargifts_available", "tl_type": "flags2.19?true"},
        {"name": "paid_messages_available", "tl_type": "flags2.20?true"},
        {"name": "id", "tl_type": "long"},
        {"name": "about", "tl_type": "string"},
        {"name": "participants_count", "tl_type": "int", "cond": 0},
        {"name": "admins_count", "tl_type": "int", "cond": 1},
        {"name": "kicked_count", "tl_type": "int", "cond": 2},
        {"name": "banned_count", "tl_type": "int", "cond": 2},
        {"name": "online_count", "tl_type": "int", "cond": 13},
        {"name": "read_inbox_max_id", "tl_type": "int"},
        {"name": "read_outbox_max_id", "tl_type": "int"},
        {"name": "unread_count", "tl_type": "int"},
        {"name": "chat_photo", "tl_type": "Photo"},
        {"name": "notify_settings", "tl_type": "PeerNotifySettings"},
        {"name": "exported_invite", "tl_type": "ExportedChatInvite", "cond": 23},
        {"name": "bot_info", "tl_type": "Vector"},
        {"name": "migrated_from_chat_id", "tl_type": "long", "cond": 4},
        {"name": "migrated_from_max_id", "tl_type": "int", "cond": 4},
        {"name": "pinned_msg_id", "tl_type": "int", "cond": 5},
        {"name": "stickerset", "tl_type": "StickerSet", "cond": 8},
        {"name": "available_min_id", "tl_type": "int", "cond": 9},
        {"name": "folder_id", "tl_type": "int", "cond": 11},
        {"name": "linked_chat_id", "tl_type": "long", "cond": 14},
        {"name": "location", "tl_type": "ChannelLocation", "cond": 15},
        {"name": "slowmode_seconds", "tl_type": "int", "cond": 17},
        {"name": "slowmode_next_send_date", "tl_type": "int", "cond": 18},
        {"name": "stats_dc", "tl_type": "int", "cond": 12},
        {"name": "pts", "tl_type": "int"},
        {"name": "call", "tl_type": "InputGroupCall", "cond": 21},
        {"name": "ttl_period", "tl_type": "int", "cond": 24},
        {"name": "pending_suggestions", "tl_type": "Vector", "cond": 25},
        {"name": "groupcall_default_join_as", "tl_type": "Peer", "cond": 26},
        {"name": "theme_emoticon", "tl_type": "string", "cond": 27},
        {"name": "requests_pending", "tl_type": "int", "cond": 28},
        {"name": "recent_requesters", "tl_type": "Vector", "cond": 28},
        {"name": "default_send_as", "tl_type": "Peer", "cond": 29},
        {"name": "available_reactions", "tl_type": "ChatReactions", "cond": 30},
        {"name": "reactions_limit", "tl_type": "flags2.13?int"},
        {"name": "stories", "tl_type": "flags2.4?PeerStories"},
        {"name": "wallpaper", "tl_type": "flags2.7?WallPaper"},
        {"name": "boosts_applied", "tl_type": "flags2.8?int"},
        {"name": "boosts_unrestrict", "tl_type": "flags2.9?int"},
        {"name": "emojiset", "tl_type": "flags2.10?StickerSet"},
        {"name": "bot_verification", "tl_type": "flags2.17?BotVerification"},
        {"name": "stargifts_count", "tl_type": "flags2.18?int"},
        {"name": "send_paid_messages_stars", "tl_type": "flags2.21?long"},
        {"name": "main_tab", "tl_type": "flags2.22?ProfileTab"},
        {"name": "guard_bot_id", "tl_type": "flags2.23?long"},
    ],
    "chatInviteAlready": [
        {"name": "chat", "tl_type": "Chat"},
    ],
    "chatInvite": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "channel", "tl_type": "true", "cond": 0},
        {"name": "broadcast", "tl_type": "true", "cond": 1},
        {"name": "public", "tl_type": "true", "cond": 2},
        {"name": "megagroup", "tl_type": "true", "cond": 3},
        {"name": "request_needed", "tl_type": "true", "cond": 6},
        {"name": "verified", "tl_type": "true", "cond": 7},
        {"name": "scam", "tl_type": "true", "cond": 8},
        {"name": "fake", "tl_type": "true", "cond": 9},
        {"name": "can_refulfill_subscription", "tl_type": "true", "cond": 11},
        {"name": "title", "tl_type": "string"},
        {"name": "about", "tl_type": "string", "cond": 5},
        {"name": "photo", "tl_type": "Photo"},
        {"name": "participants_count", "tl_type": "int"},
        {"name": "participants", "tl_type": "Vector", "cond": 4},
        {"name": "color", "tl_type": "int"},
        {"name": "subscription_pricing", "tl_type": "StarsSubscriptionPricing", "cond": 10},
        {"name": "subscription_form_id", "tl_type": "long", "cond": 12},
        {"name": "bot_verification", "tl_type": "BotVerification", "cond": 13},
    ],
    "chatInvitePeek": [
        {"name": "chat", "tl_type": "Chat"},
        {"name": "expires", "tl_type": "int"},
    ],
    "chatInviteImporter": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "requested", "tl_type": "true", "cond": 0},
        {"name": "via_chatlist", "tl_type": "true", "cond": 3},
        {"name": "user_id", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "about", "tl_type": "string", "cond": 2},
        {"name": "approved_by", "tl_type": "long", "cond": 1},
    ],
    "chatOnlines": [
        {"name": "onlines", "tl_type": "int"},
    ],
    "chatParticipant": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "user_id", "tl_type": "long"},
        {"name": "inviter_id", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "rank", "tl_type": "string", "cond": 0},
    ],
    "chatParticipantCreator": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "user_id", "tl_type": "long"},
        {"name": "rank", "tl_type": "string", "cond": 0},
    ],
    "chatParticipantAdmin": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "user_id", "tl_type": "long"},
        {"name": "inviter_id", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "rank", "tl_type": "string", "cond": 0},
    ],
    "chatParticipantsForbidden": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "chat_id", "tl_type": "long"},
        {"name": "self_participant", "tl_type": "ChatParticipant", "cond": 0},
    ],
    "chatParticipants": [
        {"name": "chat_id", "tl_type": "long"},
        {"name": "participants", "tl_type": "Vector"},
        {"name": "version", "tl_type": "int"},
    ],
    "chatPhoto": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "has_video", "tl_type": "true", "cond": 0},
        {"name": "photo_id", "tl_type": "long"},
        {"name": "stripped_thumb", "tl_type": "bytes", "cond": 1},
        {"name": "dc_id", "tl_type": "int"},
    ],
    "chatReactionsAll": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "allow_custom", "tl_type": "true", "cond": 0},
    ],
    "chatReactionsSome": [
        {"name": "reactions", "tl_type": "Vector"},
    ],
    "chatTheme": [
        {"name": "emoticon", "tl_type": "string"},
    ],
    "chatThemeUniqueGift": [
        {"name": "gift", "tl_type": "StarGift"},
        {"name": "theme_settings", "tl_type": "Vector"},
    ],
    "codeSettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "allow_flashcall", "tl_type": "true", "cond": 0},
        {"name": "current_number", "tl_type": "true", "cond": 1},
        {"name": "allow_app_hash", "tl_type": "true", "cond": 4},
        {"name": "allow_missed_call", "tl_type": "true", "cond": 5},
        {"name": "allow_firebase", "tl_type": "true", "cond": 7},
        {"name": "unknown_number", "tl_type": "true", "cond": 9},
        {"name": "logout_tokens", "tl_type": "Vector", "cond": 6},
        {"name": "token", "tl_type": "string", "cond": 8},
        {"name": "app_sandbox", "tl_type": "Bool", "cond": 8},
    ],
    "config": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "default_p2p_contacts", "tl_type": "true", "cond": 3},
        {"name": "preload_featured_stickers", "tl_type": "true", "cond": 4},
        {"name": "revoke_pm_inbox", "tl_type": "true", "cond": 6},
        {"name": "blocked_mode", "tl_type": "true", "cond": 8},
        {"name": "force_try_ipv6", "tl_type": "true", "cond": 14},
        {"name": "date", "tl_type": "int"},
        {"name": "expires", "tl_type": "int"},
        {"name": "test_mode", "tl_type": "Bool"},
        {"name": "this_dc", "tl_type": "int"},
        {"name": "dc_options", "tl_type": "Vector"},
        {"name": "dc_txt_domain_name", "tl_type": "string"},
        {"name": "chat_size_max", "tl_type": "int"},
        {"name": "megagroup_size_max", "tl_type": "int"},
        {"name": "forwarded_count_max", "tl_type": "int"},
        {"name": "online_update_period_ms", "tl_type": "int"},
        {"name": "offline_blur_timeout_ms", "tl_type": "int"},
        {"name": "offline_idle_timeout_ms", "tl_type": "int"},
        {"name": "online_cloud_timeout_ms", "tl_type": "int"},
        {"name": "notify_cloud_delay_ms", "tl_type": "int"},
        {"name": "notify_default_delay_ms", "tl_type": "int"},
        {"name": "push_chat_period_ms", "tl_type": "int"},
        {"name": "push_chat_limit", "tl_type": "int"},
        {"name": "edit_time_limit", "tl_type": "int"},
        {"name": "revoke_time_limit", "tl_type": "int"},
        {"name": "revoke_pm_time_limit", "tl_type": "int"},
        {"name": "rating_e_decay", "tl_type": "int"},
        {"name": "stickers_recent_limit", "tl_type": "int"},
        {"name": "channels_read_media_period", "tl_type": "int"},
        {"name": "tmp_sessions", "tl_type": "int", "cond": 0},
        {"name": "call_receive_timeout_ms", "tl_type": "int"},
        {"name": "call_ring_timeout_ms", "tl_type": "int"},
        {"name": "call_connect_timeout_ms", "tl_type": "int"},
        {"name": "call_packet_timeout_ms", "tl_type": "int"},
        {"name": "me_url_prefix", "tl_type": "string"},
        {"name": "autoupdate_url_prefix", "tl_type": "string", "cond": 7},
        {"name": "gif_search_username", "tl_type": "string", "cond": 9},
        {"name": "venue_search_username", "tl_type": "string", "cond": 10},
        {"name": "img_search_username", "tl_type": "string", "cond": 11},
        {"name": "static_maps_provider", "tl_type": "string", "cond": 12},
        {"name": "caption_length_max", "tl_type": "int"},
        {"name": "message_length_max", "tl_type": "int"},
        {"name": "webfile_dc_id", "tl_type": "int"},
        {"name": "suggested_lang_code", "tl_type": "string", "cond": 2},
        {"name": "lang_pack_version", "tl_type": "int", "cond": 2},
        {"name": "base_lang_pack_version", "tl_type": "int", "cond": 2},
        {"name": "reactions_default", "tl_type": "Reaction", "cond": 15},
        {"name": "autologin_token", "tl_type": "string", "cond": 16},
    ],
    "connectedBot": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "bot_id", "tl_type": "long"},
        {"name": "recipients", "tl_type": "BusinessBotRecipients"},
        {"name": "rights", "tl_type": "BusinessBotRights"},
        {"name": "device", "tl_type": "string", "cond": 0},
        {"name": "date", "tl_type": "int", "cond": 1},
        {"name": "location", "tl_type": "string", "cond": 2},
    ],
    "connectedBotStarRef": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "revoked", "tl_type": "true", "cond": 1},
        {"name": "url", "tl_type": "string"},
        {"name": "date", "tl_type": "int"},
        {"name": "bot_id", "tl_type": "long"},
        {"name": "commission_permille", "tl_type": "int"},
        {"name": "duration_months", "tl_type": "int", "cond": 0},
        {"name": "participants", "tl_type": "long"},
        {"name": "revenue", "tl_type": "long"},
    ],
    "contact": [
        {"name": "user_id", "tl_type": "long"},
        {"name": "mutual", "tl_type": "Bool"},
    ],
    "contactBirthday": [
        {"name": "contact_id", "tl_type": "long"},
        {"name": "birthday", "tl_type": "Birthday"},
    ],
    "contactStatus": [
        {"name": "user_id", "tl_type": "long"},
        {"name": "status", "tl_type": "UserStatus"},
    ],
    "dataJSON": [
        {"name": "data", "tl_type": "string"},
    ],
    "dcOption": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "ipv6", "tl_type": "true", "cond": 0},
        {"name": "media_only", "tl_type": "true", "cond": 1},
        {"name": "tcpo_only", "tl_type": "true", "cond": 2},
        {"name": "cdn", "tl_type": "true", "cond": 3},
        {"name": "static", "tl_type": "true", "cond": 4},
        {"name": "this_port_only", "tl_type": "true", "cond": 5},
        {"name": "id", "tl_type": "int"},
        {"name": "ip_address", "tl_type": "string"},
        {"name": "port", "tl_type": "int"},
        {"name": "secret", "tl_type": "bytes", "cond": 10},
    ],
    "defaultHistoryTTL": [
        {"name": "period", "tl_type": "int"},
    ],
    "dialog": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "pinned", "tl_type": "true", "cond": 2},
        {"name": "unread_mark", "tl_type": "true", "cond": 3},
        {"name": "view_forum_as_messages", "tl_type": "true", "cond": 6},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "top_message", "tl_type": "int"},
        {"name": "read_inbox_max_id", "tl_type": "int"},
        {"name": "read_outbox_max_id", "tl_type": "int"},
        {"name": "unread_count", "tl_type": "int"},
        {"name": "unread_mentions_count", "tl_type": "int"},
        {"name": "unread_reactions_count", "tl_type": "int"},
        {"name": "unread_poll_votes_count", "tl_type": "int"},
        {"name": "notify_settings", "tl_type": "PeerNotifySettings"},
        {"name": "pts", "tl_type": "int", "cond": 0},
        {"name": "draft", "tl_type": "DraftMessage", "cond": 1},
        {"name": "folder_id", "tl_type": "int", "cond": 4},
        {"name": "ttl_period", "tl_type": "int", "cond": 5},
    ],
    "dialogFolder": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "pinned", "tl_type": "true", "cond": 2},
        {"name": "folder", "tl_type": "Folder"},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "top_message", "tl_type": "int"},
        {"name": "unread_muted_peers_count", "tl_type": "int"},
        {"name": "unread_unmuted_peers_count", "tl_type": "int"},
        {"name": "unread_muted_messages_count", "tl_type": "int"},
        {"name": "unread_unmuted_messages_count", "tl_type": "int"},
    ],
    "dialogFilter": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "contacts", "tl_type": "true", "cond": 0},
        {"name": "non_contacts", "tl_type": "true", "cond": 1},
        {"name": "groups", "tl_type": "true", "cond": 2},
        {"name": "broadcasts", "tl_type": "true", "cond": 3},
        {"name": "bots", "tl_type": "true", "cond": 4},
        {"name": "exclude_muted", "tl_type": "true", "cond": 11},
        {"name": "exclude_read", "tl_type": "true", "cond": 12},
        {"name": "exclude_archived", "tl_type": "true", "cond": 13},
        {"name": "title_noanimate", "tl_type": "true", "cond": 28},
        {"name": "id", "tl_type": "int"},
        {"name": "title", "tl_type": "TextWithEntities"},
        {"name": "emoticon", "tl_type": "string", "cond": 25},
        {"name": "color", "tl_type": "int", "cond": 27},
        {"name": "pinned_peers", "tl_type": "Vector"},
        {"name": "include_peers", "tl_type": "Vector"},
        {"name": "exclude_peers", "tl_type": "Vector"},
    ],
    "dialogFilterChatlist": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "has_my_invites", "tl_type": "true", "cond": 26},
        {"name": "title_noanimate", "tl_type": "true", "cond": 28},
        {"name": "id", "tl_type": "int"},
        {"name": "title", "tl_type": "TextWithEntities"},
        {"name": "emoticon", "tl_type": "string", "cond": 25},
        {"name": "color", "tl_type": "int", "cond": 27},
        {"name": "pinned_peers", "tl_type": "Vector"},
        {"name": "include_peers", "tl_type": "Vector"},
    ],
    "dialogFilterSuggested": [
        {"name": "filter", "tl_type": "DialogFilter"},
        {"name": "description", "tl_type": "string"},
    ],
    "dialogPeer": [
        {"name": "peer", "tl_type": "Peer"},
    ],
    "dialogPeerFolder": [
        {"name": "folder_id", "tl_type": "int"},
    ],
    "disallowedGiftsSettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "disallow_unlimited_stargifts", "tl_type": "true", "cond": 0},
        {"name": "disallow_limited_stargifts", "tl_type": "true", "cond": 1},
        {"name": "disallow_unique_stargifts", "tl_type": "true", "cond": 2},
        {"name": "disallow_premium_gifts", "tl_type": "true", "cond": 3},
        {"name": "disallow_stargifts_from_channels", "tl_type": "true", "cond": 4},
    ],
    "documentEmpty": [
        {"name": "id", "tl_type": "long"},
    ],
    "document": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "file_reference", "tl_type": "bytes"},
        {"name": "date", "tl_type": "int"},
        {"name": "mime_type", "tl_type": "string"},
        {"name": "size", "tl_type": "long"},
        {"name": "thumbs", "tl_type": "Vector", "cond": 0},
        {"name": "video_thumbs", "tl_type": "Vector", "cond": 1},
        {"name": "dc_id", "tl_type": "int"},
        {"name": "attributes", "tl_type": "Vector"},
    ],
    "documentAttributeImageSize": [
        {"name": "w", "tl_type": "int"},
        {"name": "h", "tl_type": "int"},
    ],
    "documentAttributeSticker": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "mask", "tl_type": "true", "cond": 1},
        {"name": "alt", "tl_type": "string"},
        {"name": "stickerset", "tl_type": "InputStickerSet"},
        {"name": "mask_coords", "tl_type": "MaskCoords", "cond": 0},
    ],
    "documentAttributeVideo": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "round_message", "tl_type": "true", "cond": 0},
        {"name": "supports_streaming", "tl_type": "true", "cond": 1},
        {"name": "nosound", "tl_type": "true", "cond": 3},
        {"name": "duration", "tl_type": "double"},
        {"name": "w", "tl_type": "int"},
        {"name": "h", "tl_type": "int"},
        {"name": "preload_prefix_size", "tl_type": "int", "cond": 2},
        {"name": "video_start_ts", "tl_type": "double", "cond": 4},
        {"name": "video_codec", "tl_type": "string", "cond": 5},
    ],
    "documentAttributeAudio": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "voice", "tl_type": "true", "cond": 10},
        {"name": "duration", "tl_type": "int"},
        {"name": "title", "tl_type": "string", "cond": 0},
        {"name": "performer", "tl_type": "string", "cond": 1},
        {"name": "waveform", "tl_type": "bytes", "cond": 2},
    ],
    "documentAttributeFilename": [
        {"name": "file_name", "tl_type": "string"},
    ],
    "documentAttributeCustomEmoji": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "free", "tl_type": "true", "cond": 0},
        {"name": "text_color", "tl_type": "true", "cond": 1},
        {"name": "alt", "tl_type": "string"},
        {"name": "stickerset", "tl_type": "InputStickerSet"},
    ],
    "draftMessageEmpty": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "date", "tl_type": "int", "cond": 0},
    ],
    "draftMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "no_webpage", "tl_type": "true", "cond": 1},
        {"name": "invert_media", "tl_type": "true", "cond": 6},
        {"name": "reply_to", "tl_type": "InputReplyTo", "cond": 4},
        {"name": "message", "tl_type": "string"},
        {"name": "entities", "tl_type": "Vector", "cond": 3},
        {"name": "media", "tl_type": "InputMedia", "cond": 5},
        {"name": "date", "tl_type": "int"},
        {"name": "effect", "tl_type": "long", "cond": 7},
        {"name": "suggested_post", "tl_type": "SuggestedPost", "cond": 8},
        {"name": "rich_message", "tl_type": "RichMessage", "cond": 9},
    ],
    "emailVerificationCode": [
        {"name": "code", "tl_type": "string"},
    ],
    "emailVerificationGoogle": [
        {"name": "token", "tl_type": "string"},
    ],
    "emailVerificationApple": [
        {"name": "token", "tl_type": "string"},
    ],
    "emailVerifyPurposeLoginSetup": [
        {"name": "phone_number", "tl_type": "string"},
        {"name": "phone_code_hash", "tl_type": "string"},
    ],
    "emojiGroup": [
        {"name": "title", "tl_type": "string"},
        {"name": "icon_emoji_id", "tl_type": "long"},
        {"name": "emoticons", "tl_type": "Vector"},
    ],
    "emojiGroupGreeting": [
        {"name": "title", "tl_type": "string"},
        {"name": "icon_emoji_id", "tl_type": "long"},
        {"name": "emoticons", "tl_type": "Vector"},
    ],
    "emojiGroupPremium": [
        {"name": "title", "tl_type": "string"},
        {"name": "icon_emoji_id", "tl_type": "long"},
    ],
    "emojiKeyword": [
        {"name": "keyword", "tl_type": "string"},
        {"name": "emoticons", "tl_type": "Vector"},
    ],
    "emojiKeywordDeleted": [
        {"name": "keyword", "tl_type": "string"},
        {"name": "emoticons", "tl_type": "Vector"},
    ],
    "emojiKeywordsDifference": [
        {"name": "lang_code", "tl_type": "string"},
        {"name": "from_version", "tl_type": "int"},
        {"name": "version", "tl_type": "int"},
        {"name": "keywords", "tl_type": "Vector"},
    ],
    "emojiLanguage": [
        {"name": "lang_code", "tl_type": "string"},
    ],
    "emojiList": [
        {"name": "hash", "tl_type": "long"},
        {"name": "document_id", "tl_type": "Vector"},
    ],
    "emojiStatus": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "document_id", "tl_type": "long"},
        {"name": "until", "tl_type": "int", "cond": 0},
    ],
    "emojiStatusCollectible": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "collectible_id", "tl_type": "long"},
        {"name": "document_id", "tl_type": "long"},
        {"name": "title", "tl_type": "string"},
        {"name": "slug", "tl_type": "string"},
        {"name": "pattern_document_id", "tl_type": "long"},
        {"name": "center_color", "tl_type": "int"},
        {"name": "edge_color", "tl_type": "int"},
        {"name": "pattern_color", "tl_type": "int"},
        {"name": "text_color", "tl_type": "int"},
        {"name": "until", "tl_type": "int", "cond": 0},
    ],
    "inputEmojiStatusCollectible": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "collectible_id", "tl_type": "long"},
        {"name": "until", "tl_type": "int", "cond": 0},
    ],
    "emojiURL": [
        {"name": "url", "tl_type": "string"},
    ],
    "encryptedChatEmpty": [
        {"name": "id", "tl_type": "int"},
    ],
    "encryptedChatWaiting": [
        {"name": "id", "tl_type": "int"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "admin_id", "tl_type": "long"},
        {"name": "participant_id", "tl_type": "long"},
    ],
    "encryptedChatRequested": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "folder_id", "tl_type": "int", "cond": 0},
        {"name": "id", "tl_type": "int"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "admin_id", "tl_type": "long"},
        {"name": "participant_id", "tl_type": "long"},
        {"name": "g_a", "tl_type": "bytes"},
    ],
    "encryptedChat": [
        {"name": "id", "tl_type": "int"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "admin_id", "tl_type": "long"},
        {"name": "participant_id", "tl_type": "long"},
        {"name": "g_a_or_b", "tl_type": "bytes"},
        {"name": "key_fingerprint", "tl_type": "long"},
    ],
    "encryptedChatDiscarded": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "history_deleted", "tl_type": "true", "cond": 0},
        {"name": "id", "tl_type": "int"},
    ],
    "encryptedFile": [
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "size", "tl_type": "long"},
        {"name": "dc_id", "tl_type": "int"},
        {"name": "key_fingerprint", "tl_type": "int"},
    ],
    "encryptedMessage": [
        {"name": "random_id", "tl_type": "long"},
        {"name": "chat_id", "tl_type": "int"},
        {"name": "date", "tl_type": "int"},
        {"name": "bytes", "tl_type": "bytes"},
        {"name": "file", "tl_type": "EncryptedFile"},
    ],
    "encryptedMessageService": [
        {"name": "random_id", "tl_type": "long"},
        {"name": "chat_id", "tl_type": "int"},
        {"name": "date", "tl_type": "int"},
        {"name": "bytes", "tl_type": "bytes"},
    ],
    "error": [
        {"name": "code", "tl_type": "int"},
        {"name": "text", "tl_type": "string"},
    ],
    "chatInviteExported": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "revoked", "tl_type": "true", "cond": 0},
        {"name": "permanent", "tl_type": "true", "cond": 5},
        {"name": "request_needed", "tl_type": "true", "cond": 6},
        {"name": "link", "tl_type": "string"},
        {"name": "admin_id", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "start_date", "tl_type": "int", "cond": 4},
        {"name": "expire_date", "tl_type": "int", "cond": 1},
        {"name": "usage_limit", "tl_type": "int", "cond": 2},
        {"name": "usage", "tl_type": "int", "cond": 3},
        {"name": "requested", "tl_type": "int", "cond": 7},
        {"name": "subscription_expired", "tl_type": "int", "cond": 10},
        {"name": "title", "tl_type": "string", "cond": 8},
        {"name": "subscription_pricing", "tl_type": "StarsSubscriptionPricing", "cond": 9},
    ],
    "exportedChatlistInvite": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "title", "tl_type": "string"},
        {"name": "url", "tl_type": "string"},
        {"name": "peers", "tl_type": "Vector"},
    ],
    "exportedContactToken": [
        {"name": "url", "tl_type": "string"},
        {"name": "expires", "tl_type": "int"},
    ],
    "exportedMessageLink": [
        {"name": "link", "tl_type": "string"},
        {"name": "html", "tl_type": "string"},
    ],
    "exportedStoryLink": [
        {"name": "link", "tl_type": "string"},
    ],
    "factCheck": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "need_check", "tl_type": "true", "cond": 0},
        {"name": "country", "tl_type": "string", "cond": 1},
        {"name": "text", "tl_type": "TextWithEntities", "cond": 1},
        {"name": "hash", "tl_type": "long"},
    ],
    "fileHash": [
        {"name": "offset", "tl_type": "long"},
        {"name": "limit", "tl_type": "int"},
        {"name": "hash", "tl_type": "bytes"},
    ],
    "folder": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "autofill_new_broadcasts", "tl_type": "true", "cond": 0},
        {"name": "autofill_public_groups", "tl_type": "true", "cond": 1},
        {"name": "autofill_new_correspondents", "tl_type": "true", "cond": 2},
        {"name": "id", "tl_type": "int"},
        {"name": "title", "tl_type": "string"},
        {"name": "photo", "tl_type": "ChatPhoto", "cond": 3},
    ],
    "folderPeer": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "folder_id", "tl_type": "int"},
    ],
    "forumTopicDeleted": [
        {"name": "id", "tl_type": "int"},
    ],
    "forumTopic": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "my", "tl_type": "true", "cond": 1},
        {"name": "closed", "tl_type": "true", "cond": 2},
        {"name": "pinned", "tl_type": "true", "cond": 3},
        {"name": "short", "tl_type": "true", "cond": 5},
        {"name": "hidden", "tl_type": "true", "cond": 6},
        {"name": "title_missing", "tl_type": "true", "cond": 7},
        {"name": "id", "tl_type": "int"},
        {"name": "date", "tl_type": "int"},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "title", "tl_type": "string"},
        {"name": "icon_color", "tl_type": "int"},
        {"name": "icon_emoji_id", "tl_type": "long", "cond": 0},
        {"name": "top_message", "tl_type": "int"},
        {"name": "read_inbox_max_id", "tl_type": "int"},
        {"name": "read_outbox_max_id", "tl_type": "int"},
        {"name": "unread_count", "tl_type": "int"},
        {"name": "unread_mentions_count", "tl_type": "int"},
        {"name": "unread_reactions_count", "tl_type": "int"},
        {"name": "unread_poll_votes_count", "tl_type": "int"},
        {"name": "from_id", "tl_type": "Peer"},
        {"name": "notify_settings", "tl_type": "PeerNotifySettings"},
        {"name": "draft", "tl_type": "DraftMessage", "cond": 4},
    ],
    "foundStory": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "story", "tl_type": "StoryItem"},
    ],
    "game": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "short_name", "tl_type": "string"},
        {"name": "title", "tl_type": "string"},
        {"name": "description", "tl_type": "string"},
        {"name": "photo", "tl_type": "Photo"},
        {"name": "document", "tl_type": "Document", "cond": 0},
    ],
    "geoPoint": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "long", "tl_type": "double"},
        {"name": "lat", "tl_type": "double"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "accuracy_radius", "tl_type": "int", "cond": 0},
    ],
    "geoPointAddress": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "country_iso2", "tl_type": "string"},
        {"name": "state", "tl_type": "string", "cond": 0},
        {"name": "city", "tl_type": "string", "cond": 1},
        {"name": "street", "tl_type": "string", "cond": 2},
    ],
    "globalPrivacySettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "archive_and_mute_new_noncontact_peers", "tl_type": "true", "cond": 0},
        {"name": "keep_archived_unmuted", "tl_type": "true", "cond": 1},
        {"name": "keep_archived_folders", "tl_type": "true", "cond": 2},
        {"name": "hide_read_marks", "tl_type": "true", "cond": 3},
        {"name": "new_noncontact_peers_require_premium", "tl_type": "true", "cond": 4},
        {"name": "display_gifts_button", "tl_type": "true", "cond": 7},
        {"name": "noncontact_peers_paid_stars", "tl_type": "long", "cond": 5},
        {"name": "disallowed_gifts", "tl_type": "DisallowedGiftsSettings", "cond": 6},
    ],
    "groupCallDiscarded": [
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "duration", "tl_type": "int"},
    ],
    "groupCall": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "join_muted", "tl_type": "true", "cond": 1},
        {"name": "can_change_join_muted", "tl_type": "true", "cond": 2},
        {"name": "join_date_asc", "tl_type": "true", "cond": 6},
        {"name": "schedule_start_subscribed", "tl_type": "true", "cond": 8},
        {"name": "can_start_video", "tl_type": "true", "cond": 9},
        {"name": "record_video_active", "tl_type": "true", "cond": 11},
        {"name": "rtmp_stream", "tl_type": "true", "cond": 12},
        {"name": "listeners_hidden", "tl_type": "true", "cond": 13},
        {"name": "conference", "tl_type": "true", "cond": 14},
        {"name": "creator", "tl_type": "true", "cond": 15},
        {"name": "messages_enabled", "tl_type": "true", "cond": 17},
        {"name": "can_change_messages_enabled", "tl_type": "true", "cond": 18},
        {"name": "min", "tl_type": "true", "cond": 19},
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "participants_count", "tl_type": "int"},
        {"name": "title", "tl_type": "string", "cond": 3},
        {"name": "stream_dc_id", "tl_type": "int", "cond": 4},
        {"name": "record_start_date", "tl_type": "int", "cond": 5},
        {"name": "schedule_date", "tl_type": "int", "cond": 7},
        {"name": "unmuted_video_count", "tl_type": "int", "cond": 10},
        {"name": "unmuted_video_limit", "tl_type": "int"},
        {"name": "version", "tl_type": "int"},
        {"name": "invite_link", "tl_type": "string", "cond": 16},
        {"name": "send_paid_messages_stars", "tl_type": "long", "cond": 20},
        {"name": "default_send_as", "tl_type": "Peer", "cond": 21},
    ],
    "groupCallDonor": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "top", "tl_type": "true", "cond": 0},
        {"name": "my", "tl_type": "true", "cond": 1},
        {"name": "peer_id", "tl_type": "Peer", "cond": 3},
        {"name": "stars", "tl_type": "long"},
    ],
    "groupCallMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "from_admin", "tl_type": "true", "cond": 1},
        {"name": "id", "tl_type": "int"},
        {"name": "from_id", "tl_type": "Peer"},
        {"name": "date", "tl_type": "int"},
        {"name": "message", "tl_type": "TextWithEntities"},
        {"name": "paid_message_stars", "tl_type": "long", "cond": 0},
    ],
    "groupCallParticipant": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "muted", "tl_type": "true", "cond": 0},
        {"name": "left", "tl_type": "true", "cond": 1},
        {"name": "can_self_unmute", "tl_type": "true", "cond": 2},
        {"name": "just_joined", "tl_type": "true", "cond": 4},
        {"name": "versioned", "tl_type": "true", "cond": 5},
        {"name": "min", "tl_type": "true", "cond": 8},
        {"name": "muted_by_you", "tl_type": "true", "cond": 9},
        {"name": "volume_by_admin", "tl_type": "true", "cond": 10},
        {"name": "self", "tl_type": "true", "cond": 12},
        {"name": "video_joined", "tl_type": "true", "cond": 15},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "date", "tl_type": "int"},
        {"name": "active_date", "tl_type": "int", "cond": 3},
        {"name": "source", "tl_type": "int"},
        {"name": "volume", "tl_type": "int", "cond": 7},
        {"name": "about", "tl_type": "string", "cond": 11},
        {"name": "raise_hand_rating", "tl_type": "long", "cond": 13},
        {"name": "video", "tl_type": "GroupCallParticipantVideo", "cond": 6},
        {"name": "presentation", "tl_type": "GroupCallParticipantVideo", "cond": 14},
        {"name": "paid_stars_total", "tl_type": "long", "cond": 16},
    ],
    "groupCallParticipantVideo": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "paused", "tl_type": "true", "cond": 0},
        {"name": "endpoint", "tl_type": "string"},
        {"name": "source_groups", "tl_type": "Vector"},
        {"name": "audio_source", "tl_type": "int", "cond": 1},
    ],
    "groupCallParticipantVideoSourceGroup": [
        {"name": "semantics", "tl_type": "string"},
        {"name": "sources", "tl_type": "Vector"},
    ],
    "groupCallStreamChannel": [
        {"name": "channel", "tl_type": "int"},
        {"name": "scale", "tl_type": "int"},
        {"name": "last_timestamp_ms", "tl_type": "long"},
    ],
    "highScore": [
        {"name": "pos", "tl_type": "int"},
        {"name": "user_id", "tl_type": "long"},
        {"name": "score", "tl_type": "int"},
    ],
    "importedContact": [
        {"name": "user_id", "tl_type": "long"},
        {"name": "client_id", "tl_type": "long"},
    ],
    "inlineBotSwitchPM": [
        {"name": "text", "tl_type": "string"},
        {"name": "start_param", "tl_type": "string"},
    ],
    "inlineBotWebView": [
        {"name": "text", "tl_type": "string"},
        {"name": "url", "tl_type": "string"},
    ],
    "inputAiComposeToneDefault": [
        {"name": "tone", "tl_type": "string"},
    ],
    "inputAiComposeToneID": [
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
    ],
    "inputAiComposeToneSlug": [
        {"name": "slug", "tl_type": "string"},
    ],
    "inputAppEvent": [
        {"name": "time", "tl_type": "double"},
        {"name": "type", "tl_type": "string"},
        {"name": "peer", "tl_type": "long"},
        {"name": "data", "tl_type": "JSONValue"},
    ],
    "inputBotAppID": [
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
    ],
    "inputBotAppShortName": [
        {"name": "bot_id", "tl_type": "InputUser"},
        {"name": "short_name", "tl_type": "string"},
    ],
    "inputBotInlineMessageMediaAuto": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "invert_media", "tl_type": "true", "cond": 3},
        {"name": "message", "tl_type": "string"},
        {"name": "entities", "tl_type": "Vector", "cond": 1},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
    ],
    "inputBotInlineMessageText": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "no_webpage", "tl_type": "true", "cond": 0},
        {"name": "invert_media", "tl_type": "true", "cond": 3},
        {"name": "message", "tl_type": "string"},
        {"name": "entities", "tl_type": "Vector", "cond": 1},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
    ],
    "inputBotInlineMessageMediaGeo": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "geo_point", "tl_type": "InputGeoPoint"},
        {"name": "heading", "tl_type": "int", "cond": 0},
        {"name": "period", "tl_type": "int", "cond": 1},
        {"name": "proximity_notification_radius", "tl_type": "int", "cond": 3},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
    ],
    "inputBotInlineMessageMediaVenue": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "geo_point", "tl_type": "InputGeoPoint"},
        {"name": "title", "tl_type": "string"},
        {"name": "address", "tl_type": "string"},
        {"name": "provider", "tl_type": "string"},
        {"name": "venue_id", "tl_type": "string"},
        {"name": "venue_type", "tl_type": "string"},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
    ],
    "inputBotInlineMessageMediaContact": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "phone_number", "tl_type": "string"},
        {"name": "first_name", "tl_type": "string"},
        {"name": "last_name", "tl_type": "string"},
        {"name": "vcard", "tl_type": "string"},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
    ],
    "inputBotInlineMessageGame": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
    ],
    "inputBotInlineMessageMediaInvoice": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "title", "tl_type": "string"},
        {"name": "description", "tl_type": "string"},
        {"name": "photo", "tl_type": "InputWebDocument", "cond": 0},
        {"name": "invoice", "tl_type": "Invoice"},
        {"name": "payload", "tl_type": "bytes"},
        {"name": "provider", "tl_type": "string"},
        {"name": "provider_data", "tl_type": "DataJSON"},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
    ],
    "inputBotInlineMessageMediaWebPage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "invert_media", "tl_type": "true", "cond": 3},
        {"name": "force_large_media", "tl_type": "true", "cond": 4},
        {"name": "force_small_media", "tl_type": "true", "cond": 5},
        {"name": "optional", "tl_type": "true", "cond": 6},
        {"name": "message", "tl_type": "string"},
        {"name": "entities", "tl_type": "Vector", "cond": 1},
        {"name": "url", "tl_type": "string"},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
    ],
    "inputBotInlineMessageRichMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
        {"name": "rich_message", "tl_type": "InputRichMessage"},
    ],
    "inputBotInlineMessageID": [
        {"name": "dc_id", "tl_type": "int"},
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
    ],
    "inputBotInlineMessageID64": [
        {"name": "dc_id", "tl_type": "int"},
        {"name": "owner_id", "tl_type": "long"},
        {"name": "id", "tl_type": "int"},
        {"name": "access_hash", "tl_type": "long"},
    ],
    "inputBotInlineResult": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "id", "tl_type": "string"},
        {"name": "type", "tl_type": "string"},
        {"name": "title", "tl_type": "string", "cond": 1},
        {"name": "description", "tl_type": "string", "cond": 2},
        {"name": "url", "tl_type": "string", "cond": 3},
        {"name": "thumb", "tl_type": "InputWebDocument", "cond": 4},
        {"name": "content", "tl_type": "InputWebDocument", "cond": 5},
        {"name": "send_message", "tl_type": "InputBotInlineMessage"},
    ],
    "inputBotInlineResultPhoto": [
        {"name": "id", "tl_type": "string"},
        {"name": "type", "tl_type": "string"},
        {"name": "photo", "tl_type": "InputPhoto"},
        {"name": "send_message", "tl_type": "InputBotInlineMessage"},
    ],
    "inputBotInlineResultDocument": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "id", "tl_type": "string"},
        {"name": "type", "tl_type": "string"},
        {"name": "title", "tl_type": "string", "cond": 1},
        {"name": "description", "tl_type": "string", "cond": 2},
        {"name": "document", "tl_type": "InputDocument"},
        {"name": "send_message", "tl_type": "InputBotInlineMessage"},
    ],
    "inputBotInlineResultGame": [
        {"name": "id", "tl_type": "string"},
        {"name": "short_name", "tl_type": "string"},
        {"name": "send_message", "tl_type": "InputBotInlineMessage"},
    ],
    "inputBusinessAwayMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "offline_only", "tl_type": "true", "cond": 0},
        {"name": "shortcut_id", "tl_type": "int"},
        {"name": "schedule", "tl_type": "BusinessAwayMessageSchedule"},
        {"name": "recipients", "tl_type": "InputBusinessRecipients"},
    ],
    "inputBusinessBotRecipients": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "existing_chats", "tl_type": "true", "cond": 0},
        {"name": "new_chats", "tl_type": "true", "cond": 1},
        {"name": "contacts", "tl_type": "true", "cond": 2},
        {"name": "non_contacts", "tl_type": "true", "cond": 3},
        {"name": "exclude_selected", "tl_type": "true", "cond": 5},
        {"name": "users", "tl_type": "Vector", "cond": 4},
        {"name": "exclude_users", "tl_type": "Vector", "cond": 6},
    ],
    "inputBusinessChatLink": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "message", "tl_type": "string"},
        {"name": "entities", "tl_type": "Vector", "cond": 0},
        {"name": "title", "tl_type": "string", "cond": 1},
    ],
    "inputBusinessGreetingMessage": [
        {"name": "shortcut_id", "tl_type": "int"},
        {"name": "recipients", "tl_type": "InputBusinessRecipients"},
        {"name": "no_activity_days", "tl_type": "int"},
    ],
    "inputBusinessIntro": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "title", "tl_type": "string"},
        {"name": "description", "tl_type": "string"},
        {"name": "sticker", "tl_type": "InputDocument", "cond": 0},
    ],
    "inputBusinessRecipients": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "existing_chats", "tl_type": "true", "cond": 0},
        {"name": "new_chats", "tl_type": "true", "cond": 1},
        {"name": "contacts", "tl_type": "true", "cond": 2},
        {"name": "non_contacts", "tl_type": "true", "cond": 3},
        {"name": "exclude_selected", "tl_type": "true", "cond": 5},
        {"name": "users", "tl_type": "Vector", "cond": 4},
    ],
    "inputChannel": [
        {"name": "channel_id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
    ],
    "inputChannelFromMessage": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "channel_id", "tl_type": "long"},
    ],
    "inputChatUploadedPhoto": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "file", "tl_type": "InputFile", "cond": 0},
        {"name": "video", "tl_type": "InputFile", "cond": 1},
        {"name": "video_start_ts", "tl_type": "double", "cond": 2},
        {"name": "video_emoji_markup", "tl_type": "VideoSize", "cond": 3},
    ],
    "inputChatPhoto": [
        {"name": "id", "tl_type": "InputPhoto"},
    ],
    "inputChatTheme": [
        {"name": "emoticon", "tl_type": "string"},
    ],
    "inputChatThemeUniqueGift": [
        {"name": "slug", "tl_type": "string"},
    ],
    "inputChatlistDialogFilter": [
        {"name": "filter_id", "tl_type": "int"},
    ],
    "inputCheckPasswordSRP": [
        {"name": "srp_id", "tl_type": "long"},
        {"name": "A", "tl_type": "bytes"},
        {"name": "M1", "tl_type": "bytes"},
    ],
    "inputClientProxy": [
        {"name": "address", "tl_type": "string"},
        {"name": "port", "tl_type": "int"},
    ],
    "inputCollectibleUsername": [
        {"name": "username", "tl_type": "string"},
    ],
    "inputCollectiblePhone": [
        {"name": "phone", "tl_type": "string"},
    ],
    "inputPhoneContact": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "client_id", "tl_type": "long"},
        {"name": "phone", "tl_type": "string"},
        {"name": "first_name", "tl_type": "string"},
        {"name": "last_name", "tl_type": "string"},
        {"name": "note", "tl_type": "TextWithEntities", "cond": 0},
    ],
    "inputDialogPeer": [
        {"name": "peer", "tl_type": "InputPeer"},
    ],
    "inputDialogPeerFolder": [
        {"name": "folder_id", "tl_type": "int"},
    ],
    "inputDocument": [
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "file_reference", "tl_type": "bytes"},
    ],
    "inputEncryptedChat": [
        {"name": "chat_id", "tl_type": "int"},
        {"name": "access_hash", "tl_type": "long"},
    ],
    "inputEncryptedFileUploaded": [
        {"name": "id", "tl_type": "long"},
        {"name": "parts", "tl_type": "int"},
        {"name": "md5_checksum", "tl_type": "string"},
        {"name": "key_fingerprint", "tl_type": "int"},
    ],
    "inputEncryptedFile": [
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
    ],
    "inputEncryptedFileBigUploaded": [
        {"name": "id", "tl_type": "long"},
        {"name": "parts", "tl_type": "int"},
        {"name": "key_fingerprint", "tl_type": "int"},
    ],
    "inputFile": [
        {"name": "id", "tl_type": "long"},
        {"name": "parts", "tl_type": "int"},
        {"name": "name", "tl_type": "string"},
        {"name": "md5_checksum", "tl_type": "string"},
    ],
    "inputFileBig": [
        {"name": "id", "tl_type": "long"},
        {"name": "parts", "tl_type": "int"},
        {"name": "name", "tl_type": "string"},
    ],
    "inputFileStoryDocument": [
        {"name": "id", "tl_type": "InputDocument"},
    ],
    "inputFileLocation": [
        {"name": "volume_id", "tl_type": "long"},
        {"name": "local_id", "tl_type": "int"},
        {"name": "secret", "tl_type": "long"},
        {"name": "file_reference", "tl_type": "bytes"},
    ],
    "inputEncryptedFileLocation": [
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
    ],
    "inputDocumentFileLocation": [
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "file_reference", "tl_type": "bytes"},
        {"name": "thumb_size", "tl_type": "string"},
    ],
    "inputSecureFileLocation": [
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
    ],
    "inputPhotoFileLocation": [
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "file_reference", "tl_type": "bytes"},
        {"name": "thumb_size", "tl_type": "string"},
    ],
    "inputPhotoLegacyFileLocation": [
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "file_reference", "tl_type": "bytes"},
        {"name": "volume_id", "tl_type": "long"},
        {"name": "local_id", "tl_type": "int"},
        {"name": "secret", "tl_type": "long"},
    ],
    "inputPeerPhotoFileLocation": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "big", "tl_type": "true", "cond": 0},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "photo_id", "tl_type": "long"},
    ],
    "inputStickerSetThumb": [
        {"name": "stickerset", "tl_type": "InputStickerSet"},
        {"name": "thumb_version", "tl_type": "int"},
    ],
    "inputGroupCallStream": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "time_ms", "tl_type": "long"},
        {"name": "scale", "tl_type": "int"},
        {"name": "video_channel", "tl_type": "int", "cond": 0},
        {"name": "video_quality", "tl_type": "int", "cond": 0},
    ],
    "inputFolderPeer": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "folder_id", "tl_type": "int"},
    ],
    "inputGameID": [
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
    ],
    "inputGameShortName": [
        {"name": "bot_id", "tl_type": "InputUser"},
        {"name": "short_name", "tl_type": "string"},
    ],
    "inputGeoPoint": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "lat", "tl_type": "double"},
        {"name": "long", "tl_type": "double"},
        {"name": "accuracy_radius", "tl_type": "int", "cond": 0},
    ],
    "inputGroupCall": [
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
    ],
    "inputGroupCallSlug": [
        {"name": "slug", "tl_type": "string"},
    ],
    "inputGroupCallInviteMessage": [
        {"name": "msg_id", "tl_type": "int"},
    ],
    "inputInvoiceMessage": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
    ],
    "inputInvoiceSlug": [
        {"name": "slug", "tl_type": "string"},
    ],
    "inputInvoicePremiumGiftCode": [
        {"name": "purpose", "tl_type": "InputStorePaymentPurpose"},
        {"name": "option", "tl_type": "PremiumGiftCodeOption"},
    ],
    "inputInvoiceStars": [
        {"name": "purpose", "tl_type": "InputStorePaymentPurpose"},
    ],
    "inputInvoiceChatInviteSubscription": [
        {"name": "hash", "tl_type": "string"},
    ],
    "inputInvoiceStarGift": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "hide_name", "tl_type": "true", "cond": 0},
        {"name": "include_upgrade", "tl_type": "true", "cond": 2},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "gift_id", "tl_type": "long"},
        {"name": "message", "tl_type": "TextWithEntities", "cond": 1},
    ],
    "inputInvoiceStarGiftUpgrade": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "keep_original_details", "tl_type": "true", "cond": 0},
        {"name": "stargift", "tl_type": "InputSavedStarGift"},
    ],
    "inputInvoiceStarGiftTransfer": [
        {"name": "stargift", "tl_type": "InputSavedStarGift"},
        {"name": "to_id", "tl_type": "InputPeer"},
    ],
    "inputInvoicePremiumGiftStars": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "user_id", "tl_type": "InputUser"},
        {"name": "months", "tl_type": "int"},
        {"name": "message", "tl_type": "TextWithEntities", "cond": 0},
    ],
    "inputInvoiceBusinessBotTransferStars": [
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "stars", "tl_type": "long"},
    ],
    "inputInvoiceStarGiftResale": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "ton", "tl_type": "true", "cond": 0},
        {"name": "slug", "tl_type": "string"},
        {"name": "to_id", "tl_type": "InputPeer"},
    ],
    "inputInvoiceStarGiftPrepaidUpgrade": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "hash", "tl_type": "string"},
    ],
    "inputInvoicePremiumAuthCode": [
        {"name": "purpose", "tl_type": "InputStorePaymentPurpose"},
    ],
    "inputInvoiceStarGiftDropOriginalDetails": [
        {"name": "stargift", "tl_type": "InputSavedStarGift"},
    ],
    "inputInvoiceStarGiftAuctionBid": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "hide_name", "tl_type": "true", "cond": 0},
        {"name": "update_bid", "tl_type": "true", "cond": 2},
        {"name": "peer", "tl_type": "InputPeer", "cond": 3},
        {"name": "gift_id", "tl_type": "long"},
        {"name": "bid_amount", "tl_type": "long"},
        {"name": "message", "tl_type": "TextWithEntities", "cond": 1},
    ],
    "inputMediaUploadedPhoto": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "spoiler", "tl_type": "true", "cond": 2},
        {"name": "live_photo", "tl_type": "true", "cond": 3},
        {"name": "file", "tl_type": "InputFile"},
        {"name": "stickers", "tl_type": "Vector", "cond": 0},
        {"name": "ttl_seconds", "tl_type": "int", "cond": 1},
        {"name": "video", "tl_type": "InputDocument", "cond": 3},
    ],
    "inputMediaPhoto": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "spoiler", "tl_type": "true", "cond": 1},
        {"name": "live_photo", "tl_type": "true", "cond": 2},
        {"name": "id", "tl_type": "InputPhoto"},
        {"name": "ttl_seconds", "tl_type": "int", "cond": 0},
        {"name": "video", "tl_type": "InputDocument", "cond": 2},
    ],
    "inputMediaGeoPoint": [
        {"name": "geo_point", "tl_type": "InputGeoPoint"},
    ],
    "inputMediaContact": [
        {"name": "phone_number", "tl_type": "string"},
        {"name": "first_name", "tl_type": "string"},
        {"name": "last_name", "tl_type": "string"},
        {"name": "vcard", "tl_type": "string"},
    ],
    "inputMediaUploadedDocument": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "nosound_video", "tl_type": "true", "cond": 3},
        {"name": "force_file", "tl_type": "true", "cond": 4},
        {"name": "spoiler", "tl_type": "true", "cond": 5},
        {"name": "file", "tl_type": "InputFile"},
        {"name": "thumb", "tl_type": "InputFile", "cond": 2},
        {"name": "mime_type", "tl_type": "string"},
        {"name": "attributes", "tl_type": "Vector"},
        {"name": "stickers", "tl_type": "Vector", "cond": 0},
        {"name": "video_cover", "tl_type": "InputPhoto", "cond": 6},
        {"name": "video_timestamp", "tl_type": "int", "cond": 7},
        {"name": "ttl_seconds", "tl_type": "int", "cond": 1},
    ],
    "inputMediaDocument": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "spoiler", "tl_type": "true", "cond": 2},
        {"name": "id", "tl_type": "InputDocument"},
        {"name": "video_cover", "tl_type": "InputPhoto", "cond": 3},
        {"name": "video_timestamp", "tl_type": "int", "cond": 4},
        {"name": "ttl_seconds", "tl_type": "int", "cond": 0},
        {"name": "query", "tl_type": "string", "cond": 1},
    ],
    "inputMediaVenue": [
        {"name": "geo_point", "tl_type": "InputGeoPoint"},
        {"name": "title", "tl_type": "string"},
        {"name": "address", "tl_type": "string"},
        {"name": "provider", "tl_type": "string"},
        {"name": "venue_id", "tl_type": "string"},
        {"name": "venue_type", "tl_type": "string"},
    ],
    "inputMediaPhotoExternal": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "spoiler", "tl_type": "true", "cond": 1},
        {"name": "url", "tl_type": "string"},
        {"name": "ttl_seconds", "tl_type": "int", "cond": 0},
    ],
    "inputMediaDocumentExternal": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "spoiler", "tl_type": "true", "cond": 1},
        {"name": "url", "tl_type": "string"},
        {"name": "ttl_seconds", "tl_type": "int", "cond": 0},
        {"name": "video_cover", "tl_type": "InputPhoto", "cond": 2},
        {"name": "video_timestamp", "tl_type": "int", "cond": 3},
    ],
    "inputMediaGame": [
        {"name": "id", "tl_type": "InputGame"},
    ],
    "inputMediaInvoice": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "title", "tl_type": "string"},
        {"name": "description", "tl_type": "string"},
        {"name": "photo", "tl_type": "InputWebDocument", "cond": 0},
        {"name": "invoice", "tl_type": "Invoice"},
        {"name": "payload", "tl_type": "bytes"},
        {"name": "provider", "tl_type": "string", "cond": 3},
        {"name": "provider_data", "tl_type": "DataJSON"},
        {"name": "start_param", "tl_type": "string", "cond": 1},
        {"name": "extended_media", "tl_type": "InputMedia", "cond": 2},
    ],
    "inputMediaGeoLive": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "stopped", "tl_type": "true", "cond": 0},
        {"name": "geo_point", "tl_type": "InputGeoPoint"},
        {"name": "heading", "tl_type": "int", "cond": 2},
        {"name": "period", "tl_type": "int", "cond": 1},
        {"name": "proximity_notification_radius", "tl_type": "int", "cond": 3},
    ],
    "inputMediaPoll": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "poll", "tl_type": "Poll"},
        {"name": "correct_answers", "tl_type": "Vector", "cond": 0},
        {"name": "attached_media", "tl_type": "InputMedia", "cond": 3},
        {"name": "solution", "tl_type": "string", "cond": 1},
        {"name": "solution_entities", "tl_type": "Vector", "cond": 1},
        {"name": "solution_media", "tl_type": "InputMedia", "cond": 2},
    ],
    "inputMediaDice": [
        {"name": "emoticon", "tl_type": "string"},
    ],
    "inputMediaStory": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "id", "tl_type": "int"},
    ],
    "inputMediaWebPage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "force_large_media", "tl_type": "true", "cond": 0},
        {"name": "force_small_media", "tl_type": "true", "cond": 1},
        {"name": "optional", "tl_type": "true", "cond": 2},
        {"name": "url", "tl_type": "string"},
    ],
    "inputMediaPaidMedia": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "stars_amount", "tl_type": "long"},
        {"name": "extended_media", "tl_type": "Vector"},
        {"name": "payload", "tl_type": "string", "cond": 0},
    ],
    "inputMediaTodo": [
        {"name": "todo", "tl_type": "TodoList"},
    ],
    "inputMediaStakeDice": [
        {"name": "game_hash", "tl_type": "string"},
        {"name": "ton_amount", "tl_type": "long"},
        {"name": "client_seed", "tl_type": "bytes"},
    ],
    "inputMessageID": [
        {"name": "id", "tl_type": "int"},
    ],
    "inputMessageReplyTo": [
        {"name": "id", "tl_type": "int"},
    ],
    "inputMessageCallbackQuery": [
        {"name": "id", "tl_type": "int"},
        {"name": "query_id", "tl_type": "long"},
    ],
    "inputMessageReadMetric": [
        {"name": "msg_id", "tl_type": "int"},
        {"name": "view_id", "tl_type": "long"},
        {"name": "time_in_view_ms", "tl_type": "int"},
        {"name": "active_time_in_view_ms", "tl_type": "int"},
        {"name": "height_to_viewport_ratio_permille", "tl_type": "int"},
        {"name": "seen_range_ratio_permille", "tl_type": "int"},
    ],
    "inputNotifyPeer": [
        {"name": "peer", "tl_type": "InputPeer"},
    ],
    "inputNotifyForumTopic": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "top_msg_id", "tl_type": "int"},
    ],
    "inputPasskeyCredentialPublicKey": [
        {"name": "id", "tl_type": "string"},
        {"name": "raw_id", "tl_type": "string"},
        {"name": "response", "tl_type": "InputPasskeyResponse"},
    ],
    "inputPasskeyCredentialFirebasePNV": [
        {"name": "pnv_token", "tl_type": "string"},
    ],
    "inputPasskeyResponseRegister": [
        {"name": "client_data", "tl_type": "DataJSON"},
        {"name": "attestation_data", "tl_type": "bytes"},
    ],
    "inputPasskeyResponseLogin": [
        {"name": "client_data", "tl_type": "DataJSON"},
        {"name": "authenticator_data", "tl_type": "bytes"},
        {"name": "signature", "tl_type": "bytes"},
        {"name": "user_handle", "tl_type": "string"},
    ],
    "inputPaymentCredentialsSaved": [
        {"name": "id", "tl_type": "string"},
        {"name": "tmp_password", "tl_type": "bytes"},
    ],
    "inputPaymentCredentials": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "save", "tl_type": "true", "cond": 0},
        {"name": "data", "tl_type": "DataJSON"},
    ],
    "inputPaymentCredentialsApplePay": [
        {"name": "payment_data", "tl_type": "DataJSON"},
    ],
    "inputPaymentCredentialsGooglePay": [
        {"name": "payment_token", "tl_type": "DataJSON"},
    ],
    "inputPeerChat": [
        {"name": "chat_id", "tl_type": "long"},
    ],
    "inputPeerUser": [
        {"name": "user_id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
    ],
    "inputPeerChannel": [
        {"name": "channel_id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
    ],
    "inputPeerUserFromMessage": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "user_id", "tl_type": "long"},
    ],
    "inputPeerChannelFromMessage": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "channel_id", "tl_type": "long"},
    ],
    "inputPeerNotifySettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "show_previews", "tl_type": "Bool", "cond": 0},
        {"name": "silent", "tl_type": "Bool", "cond": 1},
        {"name": "mute_until", "tl_type": "int", "cond": 2},
        {"name": "sound", "tl_type": "NotificationSound", "cond": 3},
        {"name": "stories_muted", "tl_type": "Bool", "cond": 6},
        {"name": "stories_hide_sender", "tl_type": "Bool", "cond": 7},
        {"name": "stories_sound", "tl_type": "NotificationSound", "cond": 8},
    ],
    "inputPhoneCall": [
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
    ],
    "inputPhoto": [
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "file_reference", "tl_type": "bytes"},
    ],
    "inputPrivacyValueAllowUsers": [
        {"name": "users", "tl_type": "Vector"},
    ],
    "inputPrivacyValueDisallowUsers": [
        {"name": "users", "tl_type": "Vector"},
    ],
    "inputPrivacyValueAllowChatParticipants": [
        {"name": "chats", "tl_type": "Vector"},
    ],
    "inputPrivacyValueDisallowChatParticipants": [
        {"name": "chats", "tl_type": "Vector"},
    ],
    "inputQuickReplyShortcut": [
        {"name": "shortcut", "tl_type": "string"},
    ],
    "inputQuickReplyShortcutId": [
        {"name": "shortcut_id", "tl_type": "int"},
    ],
    "inputReplyToMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "reply_to_msg_id", "tl_type": "int"},
        {"name": "top_msg_id", "tl_type": "int", "cond": 0},
        {"name": "reply_to_peer_id", "tl_type": "InputPeer", "cond": 1},
        {"name": "quote_text", "tl_type": "string", "cond": 2},
        {"name": "quote_entities", "tl_type": "Vector", "cond": 3},
        {"name": "quote_offset", "tl_type": "int", "cond": 4},
        {"name": "monoforum_peer_id", "tl_type": "InputPeer", "cond": 5},
        {"name": "todo_item_id", "tl_type": "int", "cond": 6},
        {"name": "poll_option", "tl_type": "bytes", "cond": 7},
    ],
    "inputReplyToStory": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "story_id", "tl_type": "int"},
    ],
    "inputReplyToMonoForum": [
        {"name": "monoforum_peer_id", "tl_type": "InputPeer"},
    ],
    "inputRichFilePhoto": [
        {"name": "id", "tl_type": "string"},
        {"name": "photo", "tl_type": "InputPhoto"},
    ],
    "inputRichFileDocument": [
        {"name": "id", "tl_type": "string"},
        {"name": "document", "tl_type": "InputDocument"},
    ],
    "inputRichMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "rtl", "tl_type": "true", "cond": 0},
        {"name": "noautolink", "tl_type": "true", "cond": 1},
        {"name": "blocks", "tl_type": "Vector"},
        {"name": "photos", "tl_type": "Vector", "cond": 2},
        {"name": "documents", "tl_type": "Vector", "cond": 3},
        {"name": "users", "tl_type": "Vector", "cond": 4},
    ],
    "inputRichMessageHTML": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "rtl", "tl_type": "true", "cond": 0},
        {"name": "noautolink", "tl_type": "true", "cond": 1},
        {"name": "html", "tl_type": "string"},
        {"name": "files", "tl_type": "Vector", "cond": 2},
    ],
    "inputRichMessageMarkdown": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "rtl", "tl_type": "true", "cond": 0},
        {"name": "noautolink", "tl_type": "true", "cond": 1},
        {"name": "markdown", "tl_type": "string"},
        {"name": "files", "tl_type": "Vector", "cond": 2},
    ],
    "inputSavedStarGiftUser": [
        {"name": "msg_id", "tl_type": "int"},
    ],
    "inputSavedStarGiftChat": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "saved_id", "tl_type": "long"},
    ],
    "inputSavedStarGiftSlug": [
        {"name": "slug", "tl_type": "string"},
    ],
    "inputSecureFileUploaded": [
        {"name": "id", "tl_type": "long"},
        {"name": "parts", "tl_type": "int"},
        {"name": "md5_checksum", "tl_type": "string"},
        {"name": "file_hash", "tl_type": "bytes"},
        {"name": "secret", "tl_type": "bytes"},
    ],
    "inputSecureFile": [
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
    ],
    "inputSecureValue": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "type", "tl_type": "SecureValueType"},
        {"name": "data", "tl_type": "SecureData", "cond": 0},
        {"name": "front_side", "tl_type": "InputSecureFile", "cond": 1},
        {"name": "reverse_side", "tl_type": "InputSecureFile", "cond": 2},
        {"name": "selfie", "tl_type": "InputSecureFile", "cond": 3},
        {"name": "translation", "tl_type": "Vector", "cond": 6},
        {"name": "files", "tl_type": "Vector", "cond": 4},
        {"name": "plain_data", "tl_type": "SecurePlainData", "cond": 5},
    ],
    "inputSingleMedia": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "media", "tl_type": "InputMedia"},
        {"name": "random_id", "tl_type": "long"},
        {"name": "message", "tl_type": "string"},
        {"name": "entities", "tl_type": "Vector", "cond": 0},
    ],
    "inputStarGiftAuction": [
        {"name": "gift_id", "tl_type": "long"},
    ],
    "inputStarGiftAuctionSlug": [
        {"name": "slug", "tl_type": "string"},
    ],
    "inputStarsTransaction": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "refund", "tl_type": "true", "cond": 0},
        {"name": "id", "tl_type": "string"},
    ],
    "inputStickerSetID": [
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
    ],
    "inputStickerSetShortName": [
        {"name": "short_name", "tl_type": "string"},
    ],
    "inputStickerSetDice": [
        {"name": "emoticon", "tl_type": "string"},
    ],
    "inputStickerSetItem": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "document", "tl_type": "InputDocument"},
        {"name": "emoji", "tl_type": "string"},
        {"name": "mask_coords", "tl_type": "MaskCoords", "cond": 0},
        {"name": "keywords", "tl_type": "string", "cond": 1},
    ],
    "inputStickeredMediaPhoto": [
        {"name": "id", "tl_type": "InputPhoto"},
    ],
    "inputStickeredMediaDocument": [
        {"name": "id", "tl_type": "InputDocument"},
    ],
    "inputStorePaymentPremiumSubscription": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "restore", "tl_type": "true", "cond": 0},
        {"name": "upgrade", "tl_type": "true", "cond": 1},
    ],
    "inputStorePaymentGiftPremium": [
        {"name": "user_id", "tl_type": "InputUser"},
        {"name": "currency", "tl_type": "string"},
        {"name": "amount", "tl_type": "long"},
    ],
    "inputStorePaymentPremiumGiftCode": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "users", "tl_type": "Vector"},
        {"name": "boost_peer", "tl_type": "InputPeer", "cond": 0},
        {"name": "currency", "tl_type": "string"},
        {"name": "amount", "tl_type": "long"},
        {"name": "message", "tl_type": "TextWithEntities", "cond": 1},
    ],
    "inputStorePaymentPremiumGiveaway": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "only_new_subscribers", "tl_type": "true", "cond": 0},
        {"name": "winners_are_visible", "tl_type": "true", "cond": 3},
        {"name": "boost_peer", "tl_type": "InputPeer"},
        {"name": "additional_peers", "tl_type": "Vector", "cond": 1},
        {"name": "countries_iso2", "tl_type": "Vector", "cond": 2},
        {"name": "prize_description", "tl_type": "string", "cond": 4},
        {"name": "random_id", "tl_type": "long"},
        {"name": "until_date", "tl_type": "int"},
        {"name": "currency", "tl_type": "string"},
        {"name": "amount", "tl_type": "long"},
    ],
    "inputStorePaymentStarsTopup": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "stars", "tl_type": "long"},
        {"name": "currency", "tl_type": "string"},
        {"name": "amount", "tl_type": "long"},
        {"name": "spend_purpose_peer", "tl_type": "InputPeer", "cond": 0},
    ],
    "inputStorePaymentStarsGift": [
        {"name": "user_id", "tl_type": "InputUser"},
        {"name": "stars", "tl_type": "long"},
        {"name": "currency", "tl_type": "string"},
        {"name": "amount", "tl_type": "long"},
    ],
    "inputStorePaymentStarsGiveaway": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "only_new_subscribers", "tl_type": "true", "cond": 0},
        {"name": "winners_are_visible", "tl_type": "true", "cond": 3},
        {"name": "stars", "tl_type": "long"},
        {"name": "boost_peer", "tl_type": "InputPeer"},
        {"name": "additional_peers", "tl_type": "Vector", "cond": 1},
        {"name": "countries_iso2", "tl_type": "Vector", "cond": 2},
        {"name": "prize_description", "tl_type": "string", "cond": 4},
        {"name": "random_id", "tl_type": "long"},
        {"name": "until_date", "tl_type": "int"},
        {"name": "currency", "tl_type": "string"},
        {"name": "amount", "tl_type": "long"},
        {"name": "users", "tl_type": "int"},
    ],
    "inputStorePaymentAuthCode": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "restore", "tl_type": "true", "cond": 0},
        {"name": "phone_number", "tl_type": "string"},
        {"name": "phone_code_hash", "tl_type": "string"},
        {"name": "premium_days", "tl_type": "int"},
        {"name": "currency", "tl_type": "string"},
        {"name": "amount", "tl_type": "long"},
    ],
    "inputTheme": [
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
    ],
    "inputThemeSlug": [
        {"name": "slug", "tl_type": "string"},
    ],
    "inputThemeSettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "message_colors_animated", "tl_type": "true", "cond": 2},
        {"name": "base_theme", "tl_type": "BaseTheme"},
        {"name": "accent_color", "tl_type": "int"},
        {"name": "outbox_accent_color", "tl_type": "int", "cond": 3},
        {"name": "message_colors", "tl_type": "Vector", "cond": 0},
        {"name": "wallpaper", "tl_type": "InputWallPaper", "cond": 1},
        {"name": "wallpaper_settings", "tl_type": "WallPaperSettings", "cond": 1},
    ],
    "inputUser": [
        {"name": "user_id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
    ],
    "inputUserFromMessage": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "user_id", "tl_type": "long"},
    ],
    "inputWallPaper": [
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
    ],
    "inputWallPaperSlug": [
        {"name": "slug", "tl_type": "string"},
    ],
    "inputWallPaperNoFile": [
        {"name": "id", "tl_type": "long"},
    ],
    "inputWebDocument": [
        {"name": "url", "tl_type": "string"},
        {"name": "size", "tl_type": "int"},
        {"name": "mime_type", "tl_type": "string"},
        {"name": "attributes", "tl_type": "Vector"},
    ],
    "inputWebFileLocation": [
        {"name": "url", "tl_type": "string"},
        {"name": "access_hash", "tl_type": "long"},
    ],
    "inputWebFileGeoPointLocation": [
        {"name": "geo_point", "tl_type": "InputGeoPoint"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "w", "tl_type": "int"},
        {"name": "h", "tl_type": "int"},
        {"name": "zoom", "tl_type": "int"},
        {"name": "scale", "tl_type": "int"},
    ],
    "inputWebFileAudioAlbumThumbLocation": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "small", "tl_type": "true", "cond": 2},
        {"name": "document", "tl_type": "InputDocument", "cond": 0},
        {"name": "title", "tl_type": "string", "cond": 1},
        {"name": "performer", "tl_type": "string", "cond": 1},
    ],
    "invoice": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "test", "tl_type": "true", "cond": 0},
        {"name": "name_requested", "tl_type": "true", "cond": 1},
        {"name": "phone_requested", "tl_type": "true", "cond": 2},
        {"name": "email_requested", "tl_type": "true", "cond": 3},
        {"name": "shipping_address_requested", "tl_type": "true", "cond": 4},
        {"name": "flexible", "tl_type": "true", "cond": 5},
        {"name": "phone_to_provider", "tl_type": "true", "cond": 6},
        {"name": "email_to_provider", "tl_type": "true", "cond": 7},
        {"name": "recurring", "tl_type": "true", "cond": 9},
        {"name": "currency", "tl_type": "string"},
        {"name": "prices", "tl_type": "Vector"},
        {"name": "max_tip_amount", "tl_type": "long", "cond": 8},
        {"name": "suggested_tip_amounts", "tl_type": "Vector", "cond": 8},
        {"name": "terms_url", "tl_type": "string", "cond": 10},
        {"name": "subscription_period", "tl_type": "int", "cond": 11},
    ],
    "jsonObjectValue": [
        {"name": "key", "tl_type": "string"},
        {"name": "value", "tl_type": "JSONValue"},
    ],
    "jsonBool": [
        {"name": "value", "tl_type": "Bool"},
    ],
    "jsonNumber": [
        {"name": "value", "tl_type": "double"},
    ],
    "jsonString": [
        {"name": "value", "tl_type": "string"},
    ],
    "jsonArray": [
        {"name": "value", "tl_type": "Vector"},
    ],
    "jsonObject": [
        {"name": "value", "tl_type": "Vector"},
    ],
    "joinChatBotResultWebView": [
        {"name": "url", "tl_type": "string"},
    ],
    "keyboardButton": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "style", "tl_type": "KeyboardButtonStyle", "cond": 10},
        {"name": "text", "tl_type": "string"},
    ],
    "keyboardButtonUrl": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "style", "tl_type": "KeyboardButtonStyle", "cond": 10},
        {"name": "text", "tl_type": "string"},
        {"name": "url", "tl_type": "string"},
    ],
    "keyboardButtonCallback": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "requires_password", "tl_type": "true", "cond": 0},
        {"name": "style", "tl_type": "KeyboardButtonStyle", "cond": 10},
        {"name": "text", "tl_type": "string"},
        {"name": "data", "tl_type": "bytes"},
    ],
    "keyboardButtonRequestPhone": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "style", "tl_type": "KeyboardButtonStyle", "cond": 10},
        {"name": "text", "tl_type": "string"},
    ],
    "keyboardButtonRequestGeoLocation": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "style", "tl_type": "KeyboardButtonStyle", "cond": 10},
        {"name": "text", "tl_type": "string"},
    ],
    "keyboardButtonSwitchInline": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "same_peer", "tl_type": "true", "cond": 0},
        {"name": "style", "tl_type": "KeyboardButtonStyle", "cond": 10},
        {"name": "text", "tl_type": "string"},
        {"name": "query", "tl_type": "string"},
        {"name": "peer_types", "tl_type": "Vector", "cond": 1},
    ],
    "keyboardButtonGame": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "style", "tl_type": "KeyboardButtonStyle", "cond": 10},
        {"name": "text", "tl_type": "string"},
    ],
    "keyboardButtonBuy": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "style", "tl_type": "KeyboardButtonStyle", "cond": 10},
        {"name": "text", "tl_type": "string"},
    ],
    "keyboardButtonUrlAuth": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "style", "tl_type": "KeyboardButtonStyle", "cond": 10},
        {"name": "text", "tl_type": "string"},
        {"name": "fwd_text", "tl_type": "string", "cond": 0},
        {"name": "url", "tl_type": "string"},
        {"name": "button_id", "tl_type": "int"},
    ],
    "inputKeyboardButtonUrlAuth": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "request_write_access", "tl_type": "true", "cond": 0},
        {"name": "style", "tl_type": "KeyboardButtonStyle", "cond": 10},
        {"name": "text", "tl_type": "string"},
        {"name": "fwd_text", "tl_type": "string", "cond": 1},
        {"name": "url", "tl_type": "string"},
        {"name": "bot", "tl_type": "InputUser"},
    ],
    "keyboardButtonRequestPoll": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "style", "tl_type": "KeyboardButtonStyle", "cond": 10},
        {"name": "quiz", "tl_type": "Bool", "cond": 0},
        {"name": "text", "tl_type": "string"},
    ],
    "inputKeyboardButtonUserProfile": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "style", "tl_type": "KeyboardButtonStyle", "cond": 10},
        {"name": "text", "tl_type": "string"},
        {"name": "user_id", "tl_type": "InputUser"},
    ],
    "keyboardButtonUserProfile": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "style", "tl_type": "KeyboardButtonStyle", "cond": 10},
        {"name": "text", "tl_type": "string"},
        {"name": "user_id", "tl_type": "long"},
    ],
    "keyboardButtonWebView": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "style", "tl_type": "KeyboardButtonStyle", "cond": 10},
        {"name": "text", "tl_type": "string"},
        {"name": "url", "tl_type": "string"},
    ],
    "keyboardButtonSimpleWebView": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "style", "tl_type": "KeyboardButtonStyle", "cond": 10},
        {"name": "text", "tl_type": "string"},
        {"name": "url", "tl_type": "string"},
    ],
    "keyboardButtonRequestPeer": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "style", "tl_type": "KeyboardButtonStyle", "cond": 10},
        {"name": "text", "tl_type": "string"},
        {"name": "button_id", "tl_type": "int"},
        {"name": "peer_type", "tl_type": "RequestPeerType"},
        {"name": "max_quantity", "tl_type": "int"},
    ],
    "inputKeyboardButtonRequestPeer": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "name_requested", "tl_type": "true", "cond": 0},
        {"name": "username_requested", "tl_type": "true", "cond": 1},
        {"name": "photo_requested", "tl_type": "true", "cond": 2},
        {"name": "style", "tl_type": "KeyboardButtonStyle", "cond": 10},
        {"name": "text", "tl_type": "string"},
        {"name": "button_id", "tl_type": "int"},
        {"name": "peer_type", "tl_type": "RequestPeerType"},
        {"name": "max_quantity", "tl_type": "int"},
    ],
    "keyboardButtonCopy": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "style", "tl_type": "KeyboardButtonStyle", "cond": 10},
        {"name": "text", "tl_type": "string"},
        {"name": "copy_text", "tl_type": "string"},
    ],
    "keyboardButtonRow": [
        {"name": "buttons", "tl_type": "Vector"},
    ],
    "keyboardButtonStyle": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "bg_primary", "tl_type": "true", "cond": 0},
        {"name": "bg_danger", "tl_type": "true", "cond": 1},
        {"name": "bg_success", "tl_type": "true", "cond": 2},
        {"name": "icon", "tl_type": "long", "cond": 3},
    ],
    "labeledPrice": [
        {"name": "label", "tl_type": "string"},
        {"name": "amount", "tl_type": "long"},
    ],
    "langPackDifference": [
        {"name": "lang_code", "tl_type": "string"},
        {"name": "from_version", "tl_type": "int"},
        {"name": "version", "tl_type": "int"},
        {"name": "strings", "tl_type": "Vector"},
    ],
    "langPackLanguage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "official", "tl_type": "true", "cond": 0},
        {"name": "rtl", "tl_type": "true", "cond": 2},
        {"name": "beta", "tl_type": "true", "cond": 3},
        {"name": "name", "tl_type": "string"},
        {"name": "native_name", "tl_type": "string"},
        {"name": "lang_code", "tl_type": "string"},
        {"name": "base_lang_code", "tl_type": "string", "cond": 1},
        {"name": "plural_code", "tl_type": "string"},
        {"name": "strings_count", "tl_type": "int"},
        {"name": "translated_count", "tl_type": "int"},
        {"name": "translations_url", "tl_type": "string"},
    ],
    "langPackString": [
        {"name": "key", "tl_type": "string"},
        {"name": "value", "tl_type": "string"},
    ],
    "langPackStringPluralized": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "key", "tl_type": "string"},
        {"name": "zero_value", "tl_type": "string", "cond": 0},
        {"name": "one_value", "tl_type": "string", "cond": 1},
        {"name": "two_value", "tl_type": "string", "cond": 2},
        {"name": "few_value", "tl_type": "string", "cond": 3},
        {"name": "many_value", "tl_type": "string", "cond": 4},
        {"name": "other_value", "tl_type": "string"},
    ],
    "langPackStringDeleted": [
        {"name": "key", "tl_type": "string"},
    ],
    "maskCoords": [
        {"name": "n", "tl_type": "int"},
        {"name": "x", "tl_type": "double"},
        {"name": "y", "tl_type": "double"},
        {"name": "zoom", "tl_type": "double"},
    ],
    "mediaAreaVenue": [
        {"name": "coordinates", "tl_type": "MediaAreaCoordinates"},
        {"name": "geo", "tl_type": "GeoPoint"},
        {"name": "title", "tl_type": "string"},
        {"name": "address", "tl_type": "string"},
        {"name": "provider", "tl_type": "string"},
        {"name": "venue_id", "tl_type": "string"},
        {"name": "venue_type", "tl_type": "string"},
    ],
    "inputMediaAreaVenue": [
        {"name": "coordinates", "tl_type": "MediaAreaCoordinates"},
        {"name": "query_id", "tl_type": "long"},
        {"name": "result_id", "tl_type": "string"},
    ],
    "mediaAreaGeoPoint": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "coordinates", "tl_type": "MediaAreaCoordinates"},
        {"name": "geo", "tl_type": "GeoPoint"},
        {"name": "address", "tl_type": "GeoPointAddress", "cond": 0},
    ],
    "mediaAreaSuggestedReaction": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "dark", "tl_type": "true", "cond": 0},
        {"name": "flipped", "tl_type": "true", "cond": 1},
        {"name": "coordinates", "tl_type": "MediaAreaCoordinates"},
        {"name": "reaction", "tl_type": "Reaction"},
    ],
    "mediaAreaChannelPost": [
        {"name": "coordinates", "tl_type": "MediaAreaCoordinates"},
        {"name": "channel_id", "tl_type": "long"},
        {"name": "msg_id", "tl_type": "int"},
    ],
    "inputMediaAreaChannelPost": [
        {"name": "coordinates", "tl_type": "MediaAreaCoordinates"},
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "msg_id", "tl_type": "int"},
    ],
    "mediaAreaUrl": [
        {"name": "coordinates", "tl_type": "MediaAreaCoordinates"},
        {"name": "url", "tl_type": "string"},
    ],
    "mediaAreaWeather": [
        {"name": "coordinates", "tl_type": "MediaAreaCoordinates"},
        {"name": "emoji", "tl_type": "string"},
        {"name": "temperature_c", "tl_type": "double"},
        {"name": "color", "tl_type": "int"},
    ],
    "mediaAreaStarGift": [
        {"name": "coordinates", "tl_type": "MediaAreaCoordinates"},
        {"name": "slug", "tl_type": "string"},
    ],
    "mediaAreaCoordinates": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "x", "tl_type": "double"},
        {"name": "y", "tl_type": "double"},
        {"name": "w", "tl_type": "double"},
        {"name": "h", "tl_type": "double"},
        {"name": "rotation", "tl_type": "double"},
        {"name": "radius", "tl_type": "double", "cond": 0},
    ],
    "messageEmpty": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "id", "tl_type": "int"},
        {"name": "peer_id", "tl_type": "Peer", "cond": 0},
    ],
    "message": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "out", "tl_type": "true", "cond": 1},
        {"name": "mentioned", "tl_type": "true", "cond": 4},
        {"name": "media_unread", "tl_type": "true", "cond": 5},
        {"name": "silent", "tl_type": "true", "cond": 13},
        {"name": "post", "tl_type": "true", "cond": 14},
        {"name": "from_scheduled", "tl_type": "true", "cond": 18},
        {"name": "legacy", "tl_type": "true", "cond": 19},
        {"name": "edit_hide", "tl_type": "true", "cond": 21},
        {"name": "pinned", "tl_type": "true", "cond": 24},
        {"name": "noforwards", "tl_type": "true", "cond": 26},
        {"name": "invert_media", "tl_type": "true", "cond": 27},
        {"name": "flags2", "tl_type": "flags", "is_flag": True},
        {"name": "offline", "tl_type": "flags2.1?true"},
        {"name": "video_processing_pending", "tl_type": "flags2.4?true"},
        {"name": "paid_suggested_post_stars", "tl_type": "flags2.8?true"},
        {"name": "paid_suggested_post_ton", "tl_type": "flags2.9?true"},
        {"name": "id", "tl_type": "int"},
        {"name": "from_id", "tl_type": "Peer", "cond": 8},
        {"name": "from_boosts_applied", "tl_type": "int", "cond": 29},
        {"name": "from_rank", "tl_type": "flags2.12?string"},
        {"name": "peer_id", "tl_type": "Peer"},
        {"name": "saved_peer_id", "tl_type": "Peer", "cond": 28},
        {"name": "fwd_from", "tl_type": "MessageFwdHeader", "cond": 2},
        {"name": "via_bot_id", "tl_type": "long", "cond": 11},
        {"name": "via_business_bot_id", "tl_type": "flags2.0?long"},
        {"name": "guestchat_via_from", "tl_type": "flags2.19?Peer"},
        {"name": "reply_to", "tl_type": "MessageReplyHeader", "cond": 3},
        {"name": "date", "tl_type": "int"},
        {"name": "message", "tl_type": "string"},
        {"name": "media", "tl_type": "MessageMedia", "cond": 9},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 6},
        {"name": "entities", "tl_type": "Vector", "cond": 7},
        {"name": "views", "tl_type": "int", "cond": 10},
        {"name": "forwards", "tl_type": "int", "cond": 10},
        {"name": "replies", "tl_type": "MessageReplies", "cond": 23},
        {"name": "edit_date", "tl_type": "int", "cond": 15},
        {"name": "post_author", "tl_type": "string", "cond": 16},
        {"name": "grouped_id", "tl_type": "long", "cond": 17},
        {"name": "reactions", "tl_type": "MessageReactions", "cond": 20},
        {"name": "restriction_reason", "tl_type": "Vector", "cond": 22},
        {"name": "ttl_period", "tl_type": "int", "cond": 25},
        {"name": "quick_reply_shortcut_id", "tl_type": "int", "cond": 30},
        {"name": "effect", "tl_type": "flags2.2?long"},
        {"name": "factcheck", "tl_type": "flags2.3?FactCheck"},
        {"name": "report_delivery_until_date", "tl_type": "flags2.5?int"},
        {"name": "paid_message_stars", "tl_type": "flags2.6?long"},
        {"name": "suggested_post", "tl_type": "flags2.7?SuggestedPost"},
        {"name": "schedule_repeat_period", "tl_type": "flags2.10?int"},
        {"name": "summary_from_language", "tl_type": "flags2.11?string"},
        {"name": "rich_message", "tl_type": "flags2.13?RichMessage"},
    ],
    "messageService": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "out", "tl_type": "true", "cond": 1},
        {"name": "mentioned", "tl_type": "true", "cond": 4},
        {"name": "media_unread", "tl_type": "true", "cond": 5},
        {"name": "reactions_are_possible", "tl_type": "true", "cond": 9},
        {"name": "silent", "tl_type": "true", "cond": 13},
        {"name": "post", "tl_type": "true", "cond": 14},
        {"name": "legacy", "tl_type": "true", "cond": 19},
        {"name": "id", "tl_type": "int"},
        {"name": "from_id", "tl_type": "Peer", "cond": 8},
        {"name": "peer_id", "tl_type": "Peer"},
        {"name": "saved_peer_id", "tl_type": "Peer", "cond": 28},
        {"name": "reply_to", "tl_type": "MessageReplyHeader", "cond": 3},
        {"name": "date", "tl_type": "int"},
        {"name": "action", "tl_type": "MessageAction"},
        {"name": "reactions", "tl_type": "MessageReactions", "cond": 20},
        {"name": "ttl_period", "tl_type": "int", "cond": 25},
    ],
    "messageActionChatCreate": [
        {"name": "title", "tl_type": "string"},
        {"name": "users", "tl_type": "Vector"},
    ],
    "messageActionChatEditTitle": [
        {"name": "title", "tl_type": "string"},
    ],
    "messageActionChatEditPhoto": [
        {"name": "photo", "tl_type": "Photo"},
    ],
    "messageActionChatAddUser": [
        {"name": "users", "tl_type": "Vector"},
    ],
    "messageActionChatDeleteUser": [
        {"name": "user_id", "tl_type": "long"},
    ],
    "messageActionChatJoinedByLink": [
        {"name": "inviter_id", "tl_type": "long"},
    ],
    "messageActionChannelCreate": [
        {"name": "title", "tl_type": "string"},
    ],
    "messageActionChatMigrateTo": [
        {"name": "channel_id", "tl_type": "long"},
    ],
    "messageActionChannelMigrateFrom": [
        {"name": "title", "tl_type": "string"},
        {"name": "chat_id", "tl_type": "long"},
    ],
    "messageActionGameScore": [
        {"name": "game_id", "tl_type": "long"},
        {"name": "score", "tl_type": "int"},
    ],
    "messageActionPaymentSentMe": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "recurring_init", "tl_type": "true", "cond": 2},
        {"name": "recurring_used", "tl_type": "true", "cond": 3},
        {"name": "currency", "tl_type": "string"},
        {"name": "total_amount", "tl_type": "long"},
        {"name": "payload", "tl_type": "bytes"},
        {"name": "info", "tl_type": "PaymentRequestedInfo", "cond": 0},
        {"name": "shipping_option_id", "tl_type": "string", "cond": 1},
        {"name": "charge", "tl_type": "PaymentCharge"},
        {"name": "subscription_until_date", "tl_type": "int", "cond": 4},
    ],
    "messageActionPaymentSent": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "recurring_init", "tl_type": "true", "cond": 2},
        {"name": "recurring_used", "tl_type": "true", "cond": 3},
        {"name": "currency", "tl_type": "string"},
        {"name": "total_amount", "tl_type": "long"},
        {"name": "invoice_slug", "tl_type": "string", "cond": 0},
        {"name": "subscription_until_date", "tl_type": "int", "cond": 4},
    ],
    "messageActionPhoneCall": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "video", "tl_type": "true", "cond": 2},
        {"name": "call_id", "tl_type": "long"},
        {"name": "reason", "tl_type": "PhoneCallDiscardReason", "cond": 0},
        {"name": "duration", "tl_type": "int", "cond": 1},
    ],
    "messageActionCustomAction": [
        {"name": "message", "tl_type": "string"},
    ],
    "messageActionBotAllowed": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "attach_menu", "tl_type": "true", "cond": 1},
        {"name": "from_request", "tl_type": "true", "cond": 3},
        {"name": "domain", "tl_type": "string", "cond": 0},
        {"name": "app", "tl_type": "BotApp", "cond": 2},
    ],
    "messageActionSecureValuesSentMe": [
        {"name": "values", "tl_type": "Vector"},
        {"name": "credentials", "tl_type": "SecureCredentialsEncrypted"},
    ],
    "messageActionSecureValuesSent": [
        {"name": "types", "tl_type": "Vector"},
    ],
    "messageActionGeoProximityReached": [
        {"name": "from_id", "tl_type": "Peer"},
        {"name": "to_id", "tl_type": "Peer"},
        {"name": "distance", "tl_type": "int"},
    ],
    "messageActionGroupCall": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "duration", "tl_type": "int", "cond": 0},
    ],
    "messageActionInviteToGroupCall": [
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "users", "tl_type": "Vector"},
    ],
    "messageActionSetMessagesTTL": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "period", "tl_type": "int"},
        {"name": "auto_setting_from", "tl_type": "long", "cond": 0},
    ],
    "messageActionGroupCallScheduled": [
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "schedule_date", "tl_type": "int"},
    ],
    "messageActionSetChatTheme": [
        {"name": "theme", "tl_type": "ChatTheme"},
    ],
    "messageActionWebViewDataSentMe": [
        {"name": "text", "tl_type": "string"},
        {"name": "data", "tl_type": "string"},
    ],
    "messageActionWebViewDataSent": [
        {"name": "text", "tl_type": "string"},
    ],
    "messageActionGiftPremium": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "currency", "tl_type": "string"},
        {"name": "amount", "tl_type": "long"},
        {"name": "days", "tl_type": "int"},
        {"name": "crypto_currency", "tl_type": "string", "cond": 0},
        {"name": "crypto_amount", "tl_type": "long", "cond": 0},
        {"name": "message", "tl_type": "TextWithEntities", "cond": 1},
    ],
    "messageActionTopicCreate": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "title_missing", "tl_type": "true", "cond": 1},
        {"name": "title", "tl_type": "string"},
        {"name": "icon_color", "tl_type": "int"},
        {"name": "icon_emoji_id", "tl_type": "long", "cond": 0},
    ],
    "messageActionTopicEdit": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "title", "tl_type": "string", "cond": 0},
        {"name": "icon_emoji_id", "tl_type": "long", "cond": 1},
        {"name": "closed", "tl_type": "Bool", "cond": 2},
        {"name": "hidden", "tl_type": "Bool", "cond": 3},
    ],
    "messageActionSuggestProfilePhoto": [
        {"name": "photo", "tl_type": "Photo"},
    ],
    "messageActionRequestedPeer": [
        {"name": "button_id", "tl_type": "int"},
        {"name": "peers", "tl_type": "Vector"},
    ],
    "messageActionSetChatWallPaper": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "same", "tl_type": "true", "cond": 0},
        {"name": "for_both", "tl_type": "true", "cond": 1},
        {"name": "wallpaper", "tl_type": "WallPaper"},
    ],
    "messageActionGiftCode": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "via_giveaway", "tl_type": "true", "cond": 0},
        {"name": "unclaimed", "tl_type": "true", "cond": 5},
        {"name": "boost_peer", "tl_type": "Peer", "cond": 1},
        {"name": "days", "tl_type": "int"},
        {"name": "slug", "tl_type": "string"},
        {"name": "currency", "tl_type": "string", "cond": 2},
        {"name": "amount", "tl_type": "long", "cond": 2},
        {"name": "crypto_currency", "tl_type": "string", "cond": 3},
        {"name": "crypto_amount", "tl_type": "long", "cond": 3},
        {"name": "message", "tl_type": "TextWithEntities", "cond": 4},
    ],
    "messageActionGiveawayLaunch": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "stars", "tl_type": "long", "cond": 0},
    ],
    "messageActionGiveawayResults": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "stars", "tl_type": "true", "cond": 0},
        {"name": "winners_count", "tl_type": "int"},
        {"name": "unclaimed_count", "tl_type": "int"},
    ],
    "messageActionBoostApply": [
        {"name": "boosts", "tl_type": "int"},
    ],
    "messageActionRequestedPeerSentMe": [
        {"name": "button_id", "tl_type": "int"},
        {"name": "peers", "tl_type": "Vector"},
    ],
    "messageActionPaymentRefunded": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "currency", "tl_type": "string"},
        {"name": "total_amount", "tl_type": "long"},
        {"name": "payload", "tl_type": "bytes", "cond": 0},
        {"name": "charge", "tl_type": "PaymentCharge"},
    ],
    "messageActionGiftStars": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "currency", "tl_type": "string"},
        {"name": "amount", "tl_type": "long"},
        {"name": "stars", "tl_type": "long"},
        {"name": "crypto_currency", "tl_type": "string", "cond": 0},
        {"name": "crypto_amount", "tl_type": "long", "cond": 0},
        {"name": "transaction_id", "tl_type": "string", "cond": 1},
    ],
    "messageActionPrizeStars": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "unclaimed", "tl_type": "true", "cond": 0},
        {"name": "stars", "tl_type": "long"},
        {"name": "transaction_id", "tl_type": "string"},
        {"name": "boost_peer", "tl_type": "Peer"},
        {"name": "giveaway_msg_id", "tl_type": "int"},
    ],
    "messageActionStarGift": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "name_hidden", "tl_type": "true", "cond": 0},
        {"name": "saved", "tl_type": "true", "cond": 2},
        {"name": "converted", "tl_type": "true", "cond": 3},
        {"name": "upgraded", "tl_type": "true", "cond": 5},
        {"name": "refunded", "tl_type": "true", "cond": 9},
        {"name": "can_upgrade", "tl_type": "true", "cond": 10},
        {"name": "prepaid_upgrade", "tl_type": "true", "cond": 13},
        {"name": "upgrade_separate", "tl_type": "true", "cond": 16},
        {"name": "auction_acquired", "tl_type": "true", "cond": 17},
        {"name": "gift", "tl_type": "StarGift"},
        {"name": "message", "tl_type": "TextWithEntities", "cond": 1},
        {"name": "convert_stars", "tl_type": "long", "cond": 4},
        {"name": "upgrade_msg_id", "tl_type": "int", "cond": 5},
        {"name": "upgrade_stars", "tl_type": "long", "cond": 8},
        {"name": "from_id", "tl_type": "Peer", "cond": 11},
        {"name": "peer", "tl_type": "Peer", "cond": 12},
        {"name": "saved_id", "tl_type": "long", "cond": 12},
        {"name": "prepaid_upgrade_hash", "tl_type": "string", "cond": 14},
        {"name": "gift_msg_id", "tl_type": "int", "cond": 15},
        {"name": "to_id", "tl_type": "Peer", "cond": 18},
        {"name": "gift_num", "tl_type": "int", "cond": 19},
    ],
    "messageActionStarGiftUnique": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "upgrade", "tl_type": "true", "cond": 0},
        {"name": "transferred", "tl_type": "true", "cond": 1},
        {"name": "saved", "tl_type": "true", "cond": 2},
        {"name": "refunded", "tl_type": "true", "cond": 5},
        {"name": "prepaid_upgrade", "tl_type": "true", "cond": 11},
        {"name": "assigned", "tl_type": "true", "cond": 13},
        {"name": "from_offer", "tl_type": "true", "cond": 14},
        {"name": "craft", "tl_type": "true", "cond": 16},
        {"name": "gift", "tl_type": "StarGift"},
        {"name": "can_export_at", "tl_type": "int", "cond": 3},
        {"name": "transfer_stars", "tl_type": "long", "cond": 4},
        {"name": "from_id", "tl_type": "Peer", "cond": 6},
        {"name": "peer", "tl_type": "Peer", "cond": 7},
        {"name": "saved_id", "tl_type": "long", "cond": 7},
        {"name": "resale_amount", "tl_type": "StarsAmount", "cond": 8},
        {"name": "can_transfer_at", "tl_type": "int", "cond": 9},
        {"name": "can_resell_at", "tl_type": "int", "cond": 10},
        {"name": "drop_original_details_stars", "tl_type": "long", "cond": 12},
        {"name": "can_craft_at", "tl_type": "int", "cond": 15},
    ],
    "messageActionPaidMessagesRefunded": [
        {"name": "count", "tl_type": "int"},
        {"name": "stars", "tl_type": "long"},
    ],
    "messageActionPaidMessagesPrice": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "broadcast_messages_allowed", "tl_type": "true", "cond": 0},
        {"name": "stars", "tl_type": "long"},
    ],
    "messageActionConferenceCall": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "missed", "tl_type": "true", "cond": 0},
        {"name": "active", "tl_type": "true", "cond": 1},
        {"name": "video", "tl_type": "true", "cond": 4},
        {"name": "call_id", "tl_type": "long"},
        {"name": "duration", "tl_type": "int", "cond": 2},
        {"name": "other_participants", "tl_type": "Vector", "cond": 3},
    ],
    "messageActionTodoCompletions": [
        {"name": "completed", "tl_type": "Vector"},
        {"name": "incompleted", "tl_type": "Vector"},
    ],
    "messageActionTodoAppendTasks": [
        {"name": "list", "tl_type": "Vector"},
    ],
    "messageActionSuggestedPostApproval": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "rejected", "tl_type": "true", "cond": 0},
        {"name": "balance_too_low", "tl_type": "true", "cond": 1},
        {"name": "reject_comment", "tl_type": "string", "cond": 2},
        {"name": "schedule_date", "tl_type": "int", "cond": 3},
        {"name": "price", "tl_type": "StarsAmount", "cond": 4},
    ],
    "messageActionSuggestedPostSuccess": [
        {"name": "price", "tl_type": "StarsAmount"},
    ],
    "messageActionSuggestedPostRefund": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "payer_initiated", "tl_type": "true", "cond": 0},
    ],
    "messageActionGiftTon": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "currency", "tl_type": "string"},
        {"name": "amount", "tl_type": "long"},
        {"name": "crypto_currency", "tl_type": "string"},
        {"name": "crypto_amount", "tl_type": "long"},
        {"name": "transaction_id", "tl_type": "string", "cond": 0},
    ],
    "messageActionSuggestBirthday": [
        {"name": "birthday", "tl_type": "Birthday"},
    ],
    "messageActionStarGiftPurchaseOffer": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "accepted", "tl_type": "true", "cond": 0},
        {"name": "declined", "tl_type": "true", "cond": 1},
        {"name": "gift", "tl_type": "StarGift"},
        {"name": "price", "tl_type": "StarsAmount"},
        {"name": "expires_at", "tl_type": "int"},
    ],
    "messageActionStarGiftPurchaseOfferDeclined": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "expired", "tl_type": "true", "cond": 0},
        {"name": "gift", "tl_type": "StarGift"},
        {"name": "price", "tl_type": "StarsAmount"},
    ],
    "messageActionNewCreatorPending": [
        {"name": "new_creator_id", "tl_type": "long"},
    ],
    "messageActionChangeCreator": [
        {"name": "new_creator_id", "tl_type": "long"},
    ],
    "messageActionNoForwardsToggle": [
        {"name": "prev_value", "tl_type": "Bool"},
        {"name": "new_value", "tl_type": "Bool"},
    ],
    "messageActionNoForwardsRequest": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "expired", "tl_type": "true", "cond": 0},
        {"name": "prev_value", "tl_type": "Bool"},
        {"name": "new_value", "tl_type": "Bool"},
    ],
    "messageActionPollAppendAnswer": [
        {"name": "answer", "tl_type": "PollAnswer"},
    ],
    "messageActionPollDeleteAnswer": [
        {"name": "answer", "tl_type": "PollAnswer"},
    ],
    "messageActionManagedBotCreated": [
        {"name": "bot_id", "tl_type": "long"},
    ],
    "messageEntityUnknown": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
    ],
    "messageEntityMention": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
    ],
    "messageEntityHashtag": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
    ],
    "messageEntityBotCommand": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
    ],
    "messageEntityUrl": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
    ],
    "messageEntityEmail": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
    ],
    "messageEntityBold": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
    ],
    "messageEntityItalic": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
    ],
    "messageEntityCode": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
    ],
    "messageEntityPre": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
        {"name": "language", "tl_type": "string"},
    ],
    "messageEntityTextUrl": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
        {"name": "url", "tl_type": "string"},
    ],
    "messageEntityMentionName": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
        {"name": "user_id", "tl_type": "long"},
    ],
    "inputMessageEntityMentionName": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
        {"name": "user_id", "tl_type": "InputUser"},
    ],
    "messageEntityPhone": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
    ],
    "messageEntityCashtag": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
    ],
    "messageEntityUnderline": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
    ],
    "messageEntityStrike": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
    ],
    "messageEntityBankCard": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
    ],
    "messageEntitySpoiler": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
    ],
    "messageEntityCustomEmoji": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
        {"name": "document_id", "tl_type": "long"},
    ],
    "messageEntityBlockquote": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "collapsed", "tl_type": "true", "cond": 0},
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
    ],
    "messageEntityFormattedDate": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "relative", "tl_type": "true", "cond": 0},
        {"name": "short_time", "tl_type": "true", "cond": 1},
        {"name": "long_time", "tl_type": "true", "cond": 2},
        {"name": "short_date", "tl_type": "true", "cond": 3},
        {"name": "long_date", "tl_type": "true", "cond": 4},
        {"name": "day_of_week", "tl_type": "true", "cond": 5},
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
        {"name": "date", "tl_type": "int"},
    ],
    "messageEntityDiffInsert": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
    ],
    "messageEntityDiffReplace": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
        {"name": "old_text", "tl_type": "string"},
    ],
    "messageEntityDiffDelete": [
        {"name": "offset", "tl_type": "int"},
        {"name": "length", "tl_type": "int"},
    ],
    "messageExtendedMediaPreview": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "w", "tl_type": "int", "cond": 0},
        {"name": "h", "tl_type": "int", "cond": 0},
        {"name": "thumb", "tl_type": "PhotoSize", "cond": 1},
        {"name": "video_duration", "tl_type": "int", "cond": 2},
    ],
    "messageExtendedMedia": [
        {"name": "media", "tl_type": "MessageMedia"},
    ],
    "messageFwdHeader": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "imported", "tl_type": "true", "cond": 7},
        {"name": "saved_out", "tl_type": "true", "cond": 11},
        {"name": "from_id", "tl_type": "Peer", "cond": 0},
        {"name": "from_name", "tl_type": "string", "cond": 5},
        {"name": "date", "tl_type": "int"},
        {"name": "channel_post", "tl_type": "int", "cond": 2},
        {"name": "post_author", "tl_type": "string", "cond": 3},
        {"name": "saved_from_peer", "tl_type": "Peer", "cond": 4},
        {"name": "saved_from_msg_id", "tl_type": "int", "cond": 4},
        {"name": "saved_from_id", "tl_type": "Peer", "cond": 8},
        {"name": "saved_from_name", "tl_type": "string", "cond": 9},
        {"name": "saved_date", "tl_type": "int", "cond": 10},
        {"name": "psa_type", "tl_type": "string", "cond": 6},
    ],
    "messageMediaPhoto": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "spoiler", "tl_type": "true", "cond": 3},
        {"name": "live_photo", "tl_type": "true", "cond": 4},
        {"name": "photo", "tl_type": "Photo", "cond": 0},
        {"name": "ttl_seconds", "tl_type": "int", "cond": 2},
        {"name": "video", "tl_type": "Document", "cond": 4},
    ],
    "messageMediaGeo": [
        {"name": "geo", "tl_type": "GeoPoint"},
    ],
    "messageMediaContact": [
        {"name": "phone_number", "tl_type": "string"},
        {"name": "first_name", "tl_type": "string"},
        {"name": "last_name", "tl_type": "string"},
        {"name": "vcard", "tl_type": "string"},
        {"name": "user_id", "tl_type": "long"},
    ],
    "messageMediaDocument": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "nopremium", "tl_type": "true", "cond": 3},
        {"name": "spoiler", "tl_type": "true", "cond": 4},
        {"name": "video", "tl_type": "true", "cond": 6},
        {"name": "round", "tl_type": "true", "cond": 7},
        {"name": "voice", "tl_type": "true", "cond": 8},
        {"name": "document", "tl_type": "Document", "cond": 0},
        {"name": "alt_documents", "tl_type": "Vector", "cond": 5},
        {"name": "video_cover", "tl_type": "Photo", "cond": 9},
        {"name": "video_timestamp", "tl_type": "int", "cond": 10},
        {"name": "ttl_seconds", "tl_type": "int", "cond": 2},
    ],
    "messageMediaWebPage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "force_large_media", "tl_type": "true", "cond": 0},
        {"name": "force_small_media", "tl_type": "true", "cond": 1},
        {"name": "manual", "tl_type": "true", "cond": 3},
        {"name": "safe", "tl_type": "true", "cond": 4},
        {"name": "webpage", "tl_type": "WebPage"},
    ],
    "messageMediaVenue": [
        {"name": "geo", "tl_type": "GeoPoint"},
        {"name": "title", "tl_type": "string"},
        {"name": "address", "tl_type": "string"},
        {"name": "provider", "tl_type": "string"},
        {"name": "venue_id", "tl_type": "string"},
        {"name": "venue_type", "tl_type": "string"},
    ],
    "messageMediaGame": [
        {"name": "game", "tl_type": "Game"},
    ],
    "messageMediaInvoice": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "shipping_address_requested", "tl_type": "true", "cond": 1},
        {"name": "test", "tl_type": "true", "cond": 3},
        {"name": "title", "tl_type": "string"},
        {"name": "description", "tl_type": "string"},
        {"name": "photo", "tl_type": "WebDocument", "cond": 0},
        {"name": "receipt_msg_id", "tl_type": "int", "cond": 2},
        {"name": "currency", "tl_type": "string"},
        {"name": "total_amount", "tl_type": "long"},
        {"name": "start_param", "tl_type": "string"},
        {"name": "extended_media", "tl_type": "MessageExtendedMedia", "cond": 4},
    ],
    "messageMediaGeoLive": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "geo", "tl_type": "GeoPoint"},
        {"name": "heading", "tl_type": "int", "cond": 0},
        {"name": "period", "tl_type": "int"},
        {"name": "proximity_notification_radius", "tl_type": "int", "cond": 1},
    ],
    "messageMediaPoll": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "poll", "tl_type": "Poll"},
        {"name": "results", "tl_type": "PollResults"},
        {"name": "attached_media", "tl_type": "MessageMedia", "cond": 0},
    ],
    "messageMediaDice": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "value", "tl_type": "int"},
        {"name": "emoticon", "tl_type": "string"},
        {"name": "game_outcome", "tl_type": "messages.EmojiGameOutcome", "cond": 0},
    ],
    "messageMediaStory": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "via_mention", "tl_type": "true", "cond": 1},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "id", "tl_type": "int"},
        {"name": "story", "tl_type": "StoryItem", "cond": 0},
    ],
    "messageMediaGiveaway": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "only_new_subscribers", "tl_type": "true", "cond": 0},
        {"name": "winners_are_visible", "tl_type": "true", "cond": 2},
        {"name": "channels", "tl_type": "Vector"},
        {"name": "countries_iso2", "tl_type": "Vector", "cond": 1},
        {"name": "prize_description", "tl_type": "string", "cond": 3},
        {"name": "quantity", "tl_type": "int"},
        {"name": "months", "tl_type": "int", "cond": 4},
        {"name": "stars", "tl_type": "long", "cond": 5},
        {"name": "until_date", "tl_type": "int"},
    ],
    "messageMediaGiveawayResults": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "only_new_subscribers", "tl_type": "true", "cond": 0},
        {"name": "refunded", "tl_type": "true", "cond": 2},
        {"name": "channel_id", "tl_type": "long"},
        {"name": "additional_peers_count", "tl_type": "int", "cond": 3},
        {"name": "launch_msg_id", "tl_type": "int"},
        {"name": "winners_count", "tl_type": "int"},
        {"name": "unclaimed_count", "tl_type": "int"},
        {"name": "winners", "tl_type": "Vector"},
        {"name": "months", "tl_type": "int", "cond": 4},
        {"name": "stars", "tl_type": "long", "cond": 5},
        {"name": "prize_description", "tl_type": "string", "cond": 1},
        {"name": "until_date", "tl_type": "int"},
    ],
    "messageMediaPaidMedia": [
        {"name": "stars_amount", "tl_type": "long"},
        {"name": "extended_media", "tl_type": "Vector"},
    ],
    "messageMediaToDo": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "todo", "tl_type": "TodoList"},
        {"name": "completions", "tl_type": "Vector", "cond": 0},
    ],
    "messageMediaVideoStream": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "rtmp_stream", "tl_type": "true", "cond": 0},
        {"name": "call", "tl_type": "InputGroupCall"},
    ],
    "messagePeerReaction": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "big", "tl_type": "true", "cond": 0},
        {"name": "unread", "tl_type": "true", "cond": 1},
        {"name": "my", "tl_type": "true", "cond": 2},
        {"name": "peer_id", "tl_type": "Peer"},
        {"name": "date", "tl_type": "int"},
        {"name": "reaction", "tl_type": "Reaction"},
    ],
    "messagePeerVote": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "option", "tl_type": "bytes"},
        {"name": "date", "tl_type": "int"},
    ],
    "messagePeerVoteInputOption": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "date", "tl_type": "int"},
    ],
    "messagePeerVoteMultiple": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "options", "tl_type": "Vector"},
        {"name": "date", "tl_type": "int"},
    ],
    "messageRange": [
        {"name": "min_id", "tl_type": "int"},
        {"name": "max_id", "tl_type": "int"},
    ],
    "messageReactions": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "min", "tl_type": "true", "cond": 0},
        {"name": "can_see_list", "tl_type": "true", "cond": 2},
        {"name": "reactions_as_tags", "tl_type": "true", "cond": 3},
        {"name": "results", "tl_type": "Vector"},
        {"name": "recent_reactions", "tl_type": "Vector", "cond": 1},
        {"name": "top_reactors", "tl_type": "Vector", "cond": 4},
    ],
    "messageReactor": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "top", "tl_type": "true", "cond": 0},
        {"name": "my", "tl_type": "true", "cond": 1},
        {"name": "anonymous", "tl_type": "true", "cond": 2},
        {"name": "peer_id", "tl_type": "Peer", "cond": 3},
        {"name": "count", "tl_type": "int"},
    ],
    "messageReplies": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "comments", "tl_type": "true", "cond": 0},
        {"name": "replies", "tl_type": "int"},
        {"name": "replies_pts", "tl_type": "int"},
        {"name": "recent_repliers", "tl_type": "Vector", "cond": 1},
        {"name": "channel_id", "tl_type": "long", "cond": 0},
        {"name": "max_id", "tl_type": "int", "cond": 2},
        {"name": "read_max_id", "tl_type": "int", "cond": 3},
    ],
    "messageReplyHeader": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "reply_to_scheduled", "tl_type": "true", "cond": 2},
        {"name": "forum_topic", "tl_type": "true", "cond": 3},
        {"name": "quote", "tl_type": "true", "cond": 9},
        {"name": "reply_to_ephemeral", "tl_type": "true", "cond": 13},
        {"name": "reply_to_msg_id", "tl_type": "int", "cond": 4},
        {"name": "reply_to_peer_id", "tl_type": "Peer", "cond": 0},
        {"name": "reply_from", "tl_type": "MessageFwdHeader", "cond": 5},
        {"name": "reply_media", "tl_type": "MessageMedia", "cond": 8},
        {"name": "reply_to_top_id", "tl_type": "int", "cond": 1},
        {"name": "quote_text", "tl_type": "string", "cond": 6},
        {"name": "quote_entities", "tl_type": "Vector", "cond": 7},
        {"name": "quote_offset", "tl_type": "int", "cond": 10},
        {"name": "todo_item_id", "tl_type": "int", "cond": 11},
        {"name": "poll_option", "tl_type": "bytes", "cond": 12},
    ],
    "messageReplyStoryHeader": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "story_id", "tl_type": "int"},
    ],
    "messageReportOption": [
        {"name": "text", "tl_type": "string"},
        {"name": "option", "tl_type": "bytes"},
    ],
    "messageViews": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "views", "tl_type": "int", "cond": 0},
        {"name": "forwards", "tl_type": "int", "cond": 1},
        {"name": "replies", "tl_type": "MessageReplies", "cond": 2},
    ],
    "inputMessagesFilterPhoneCalls": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "missed", "tl_type": "true", "cond": 0},
    ],
    "missingInvitee": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "premium_would_allow_invite", "tl_type": "true", "cond": 0},
        {"name": "premium_required_for_pm", "tl_type": "true", "cond": 1},
        {"name": "user_id", "tl_type": "long"},
    ],
    "myBoost": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "slot", "tl_type": "int"},
        {"name": "peer", "tl_type": "Peer", "cond": 0},
        {"name": "date", "tl_type": "int"},
        {"name": "expires", "tl_type": "int"},
        {"name": "cooldown_until_date", "tl_type": "int", "cond": 1},
    ],
    "nearestDc": [
        {"name": "country", "tl_type": "string"},
        {"name": "this_dc", "tl_type": "int"},
        {"name": "nearest_dc", "tl_type": "int"},
    ],
    "notificationSoundLocal": [
        {"name": "title", "tl_type": "string"},
        {"name": "data", "tl_type": "string"},
    ],
    "notificationSoundRingtone": [
        {"name": "id", "tl_type": "long"},
    ],
    "notifyPeer": [
        {"name": "peer", "tl_type": "Peer"},
    ],
    "notifyForumTopic": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "top_msg_id", "tl_type": "int"},
    ],
    "outboxReadDate": [
        {"name": "date", "tl_type": "int"},
    ],
    "page": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "part", "tl_type": "true", "cond": 0},
        {"name": "rtl", "tl_type": "true", "cond": 1},
        {"name": "v2", "tl_type": "true", "cond": 2},
        {"name": "url", "tl_type": "string"},
        {"name": "blocks", "tl_type": "Vector"},
        {"name": "photos", "tl_type": "Vector"},
        {"name": "documents", "tl_type": "Vector"},
        {"name": "views", "tl_type": "int", "cond": 3},
    ],
    "pageBlockTitle": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "pageBlockSubtitle": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "pageBlockAuthorDate": [
        {"name": "author", "tl_type": "RichText"},
        {"name": "published_date", "tl_type": "int"},
    ],
    "pageBlockHeader": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "pageBlockSubheader": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "pageBlockParagraph": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "pageBlockPreformatted": [
        {"name": "text", "tl_type": "RichText"},
        {"name": "language", "tl_type": "string"},
    ],
    "pageBlockFooter": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "pageBlockAnchor": [
        {"name": "name", "tl_type": "string"},
    ],
    "pageBlockList": [
        {"name": "items", "tl_type": "Vector"},
    ],
    "pageBlockBlockquote": [
        {"name": "text", "tl_type": "RichText"},
        {"name": "caption", "tl_type": "RichText"},
    ],
    "pageBlockPullquote": [
        {"name": "text", "tl_type": "RichText"},
        {"name": "caption", "tl_type": "RichText"},
    ],
    "pageBlockPhoto": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "spoiler", "tl_type": "true", "cond": 1},
        {"name": "photo_id", "tl_type": "long"},
        {"name": "caption", "tl_type": "PageCaption"},
        {"name": "url", "tl_type": "string", "cond": 0},
        {"name": "webpage_id", "tl_type": "long", "cond": 0},
    ],
    "pageBlockVideo": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "autoplay", "tl_type": "true", "cond": 0},
        {"name": "loop", "tl_type": "true", "cond": 1},
        {"name": "spoiler", "tl_type": "true", "cond": 2},
        {"name": "video_id", "tl_type": "long"},
        {"name": "caption", "tl_type": "PageCaption"},
    ],
    "pageBlockCover": [
        {"name": "cover", "tl_type": "PageBlock"},
    ],
    "pageBlockEmbed": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "full_width", "tl_type": "true", "cond": 0},
        {"name": "allow_scrolling", "tl_type": "true", "cond": 3},
        {"name": "url", "tl_type": "string", "cond": 1},
        {"name": "html", "tl_type": "string", "cond": 2},
        {"name": "poster_photo_id", "tl_type": "long", "cond": 4},
        {"name": "w", "tl_type": "int", "cond": 5},
        {"name": "h", "tl_type": "int", "cond": 5},
        {"name": "caption", "tl_type": "PageCaption"},
    ],
    "pageBlockEmbedPost": [
        {"name": "url", "tl_type": "string"},
        {"name": "webpage_id", "tl_type": "long"},
        {"name": "author_photo_id", "tl_type": "long"},
        {"name": "author", "tl_type": "string"},
        {"name": "date", "tl_type": "int"},
        {"name": "blocks", "tl_type": "Vector"},
        {"name": "caption", "tl_type": "PageCaption"},
    ],
    "pageBlockCollage": [
        {"name": "items", "tl_type": "Vector"},
        {"name": "caption", "tl_type": "PageCaption"},
    ],
    "pageBlockSlideshow": [
        {"name": "items", "tl_type": "Vector"},
        {"name": "caption", "tl_type": "PageCaption"},
    ],
    "pageBlockChannel": [
        {"name": "channel", "tl_type": "Chat"},
    ],
    "pageBlockAudio": [
        {"name": "audio_id", "tl_type": "long"},
        {"name": "caption", "tl_type": "PageCaption"},
    ],
    "pageBlockKicker": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "pageBlockTable": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "bordered", "tl_type": "true", "cond": 0},
        {"name": "striped", "tl_type": "true", "cond": 1},
        {"name": "title", "tl_type": "RichText"},
        {"name": "rows", "tl_type": "Vector"},
    ],
    "pageBlockOrderedList": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "reversed", "tl_type": "true", "cond": 2},
        {"name": "items", "tl_type": "Vector"},
        {"name": "start", "tl_type": "int", "cond": 0},
        {"name": "type", "tl_type": "string", "cond": 1},
    ],
    "pageBlockDetails": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "open", "tl_type": "true", "cond": 0},
        {"name": "blocks", "tl_type": "Vector"},
        {"name": "title", "tl_type": "RichText"},
    ],
    "pageBlockRelatedArticles": [
        {"name": "title", "tl_type": "RichText"},
        {"name": "articles", "tl_type": "Vector"},
    ],
    "pageBlockMap": [
        {"name": "geo", "tl_type": "GeoPoint"},
        {"name": "zoom", "tl_type": "int"},
        {"name": "w", "tl_type": "int"},
        {"name": "h", "tl_type": "int"},
        {"name": "caption", "tl_type": "PageCaption"},
    ],
    "pageBlockHeading1": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "pageBlockHeading2": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "pageBlockHeading3": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "pageBlockHeading4": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "pageBlockHeading5": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "pageBlockHeading6": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "pageBlockMath": [
        {"name": "source", "tl_type": "string"},
    ],
    "pageBlockThinking": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "inputPageBlockMap": [
        {"name": "geo", "tl_type": "InputGeoPoint"},
        {"name": "zoom", "tl_type": "int"},
        {"name": "w", "tl_type": "int"},
        {"name": "h", "tl_type": "int"},
        {"name": "caption", "tl_type": "PageCaption"},
    ],
    "pageBlockBlockquoteBlocks": [
        {"name": "blocks", "tl_type": "Vector"},
        {"name": "caption", "tl_type": "RichText"},
    ],
    "pageCaption": [
        {"name": "text", "tl_type": "RichText"},
        {"name": "credit", "tl_type": "RichText"},
    ],
    "pageListItemText": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "checkbox", "tl_type": "true", "cond": 0},
        {"name": "checked", "tl_type": "true", "cond": 1},
        {"name": "text", "tl_type": "RichText"},
    ],
    "pageListItemBlocks": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "checkbox", "tl_type": "true", "cond": 0},
        {"name": "checked", "tl_type": "true", "cond": 1},
        {"name": "blocks", "tl_type": "Vector"},
    ],
    "pageListOrderedItemText": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "checkbox", "tl_type": "true", "cond": 0},
        {"name": "checked", "tl_type": "true", "cond": 1},
        {"name": "num", "tl_type": "string", "cond": 2},
        {"name": "text", "tl_type": "RichText"},
        {"name": "value", "tl_type": "int", "cond": 3},
        {"name": "type", "tl_type": "string", "cond": 4},
    ],
    "pageListOrderedItemBlocks": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "checkbox", "tl_type": "true", "cond": 0},
        {"name": "checked", "tl_type": "true", "cond": 1},
        {"name": "num", "tl_type": "string", "cond": 2},
        {"name": "blocks", "tl_type": "Vector"},
        {"name": "value", "tl_type": "int", "cond": 3},
        {"name": "type", "tl_type": "string", "cond": 4},
    ],
    "pageRelatedArticle": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "url", "tl_type": "string"},
        {"name": "webpage_id", "tl_type": "long"},
        {"name": "title", "tl_type": "string", "cond": 0},
        {"name": "description", "tl_type": "string", "cond": 1},
        {"name": "photo_id", "tl_type": "long", "cond": 2},
        {"name": "author", "tl_type": "string", "cond": 3},
        {"name": "published_date", "tl_type": "int", "cond": 4},
    ],
    "pageTableCell": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "header", "tl_type": "true", "cond": 0},
        {"name": "align_center", "tl_type": "true", "cond": 3},
        {"name": "align_right", "tl_type": "true", "cond": 4},
        {"name": "valign_middle", "tl_type": "true", "cond": 5},
        {"name": "valign_bottom", "tl_type": "true", "cond": 6},
        {"name": "text", "tl_type": "RichText", "cond": 7},
        {"name": "colspan", "tl_type": "int", "cond": 1},
        {"name": "rowspan", "tl_type": "int", "cond": 2},
    ],
    "pageTableRow": [
        {"name": "cells", "tl_type": "Vector"},
    ],
    "paidReactionPrivacyPeer": [
        {"name": "peer", "tl_type": "InputPeer"},
    ],
    "passkey": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "id", "tl_type": "string"},
        {"name": "name", "tl_type": "string"},
        {"name": "date", "tl_type": "int"},
        {"name": "software_emoji_id", "tl_type": "long", "cond": 0},
        {"name": "last_usage_date", "tl_type": "int", "cond": 1},
    ],
    "passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow": [
        {"name": "salt1", "tl_type": "bytes"},
        {"name": "salt2", "tl_type": "bytes"},
        {"name": "g", "tl_type": "int"},
        {"name": "p", "tl_type": "bytes"},
    ],
    "paymentCharge": [
        {"name": "id", "tl_type": "string"},
        {"name": "provider_charge_id", "tl_type": "string"},
    ],
    "paymentFormMethod": [
        {"name": "url", "tl_type": "string"},
        {"name": "title", "tl_type": "string"},
    ],
    "paymentRequestedInfo": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "name", "tl_type": "string", "cond": 0},
        {"name": "phone", "tl_type": "string", "cond": 1},
        {"name": "email", "tl_type": "string", "cond": 2},
        {"name": "shipping_address", "tl_type": "PostAddress", "cond": 3},
    ],
    "paymentSavedCredentialsCard": [
        {"name": "id", "tl_type": "string"},
        {"name": "title", "tl_type": "string"},
    ],
    "peerUser": [
        {"name": "user_id", "tl_type": "long"},
    ],
    "peerChat": [
        {"name": "chat_id", "tl_type": "long"},
    ],
    "peerChannel": [
        {"name": "channel_id", "tl_type": "long"},
    ],
    "peerBlocked": [
        {"name": "peer_id", "tl_type": "Peer"},
        {"name": "date", "tl_type": "int"},
    ],
    "peerColor": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "color", "tl_type": "int", "cond": 0},
        {"name": "background_emoji_id", "tl_type": "long", "cond": 1},
    ],
    "peerColorCollectible": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "collectible_id", "tl_type": "long"},
        {"name": "gift_emoji_id", "tl_type": "long"},
        {"name": "background_emoji_id", "tl_type": "long"},
        {"name": "accent_color", "tl_type": "int"},
        {"name": "colors", "tl_type": "Vector"},
        {"name": "dark_accent_color", "tl_type": "int", "cond": 0},
        {"name": "dark_colors", "tl_type": "Vector", "cond": 1},
    ],
    "inputPeerColorCollectible": [
        {"name": "collectible_id", "tl_type": "long"},
    ],
    "peerLocated": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "expires", "tl_type": "int"},
        {"name": "distance", "tl_type": "int"},
    ],
    "peerSelfLocated": [
        {"name": "expires", "tl_type": "int"},
    ],
    "peerNotifySettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "show_previews", "tl_type": "Bool", "cond": 0},
        {"name": "silent", "tl_type": "Bool", "cond": 1},
        {"name": "mute_until", "tl_type": "int", "cond": 2},
        {"name": "ios_sound", "tl_type": "NotificationSound", "cond": 3},
        {"name": "android_sound", "tl_type": "NotificationSound", "cond": 4},
        {"name": "other_sound", "tl_type": "NotificationSound", "cond": 5},
        {"name": "stories_muted", "tl_type": "Bool", "cond": 6},
        {"name": "stories_hide_sender", "tl_type": "Bool", "cond": 7},
        {"name": "stories_ios_sound", "tl_type": "NotificationSound", "cond": 8},
        {"name": "stories_android_sound", "tl_type": "NotificationSound", "cond": 9},
        {"name": "stories_other_sound", "tl_type": "NotificationSound", "cond": 10},
    ],
    "peerSettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "report_spam", "tl_type": "true", "cond": 0},
        {"name": "add_contact", "tl_type": "true", "cond": 1},
        {"name": "block_contact", "tl_type": "true", "cond": 2},
        {"name": "share_contact", "tl_type": "true", "cond": 3},
        {"name": "need_contacts_exception", "tl_type": "true", "cond": 4},
        {"name": "report_geo", "tl_type": "true", "cond": 5},
        {"name": "autoarchived", "tl_type": "true", "cond": 7},
        {"name": "invite_members", "tl_type": "true", "cond": 8},
        {"name": "request_chat_broadcast", "tl_type": "true", "cond": 10},
        {"name": "business_bot_paused", "tl_type": "true", "cond": 11},
        {"name": "business_bot_can_reply", "tl_type": "true", "cond": 12},
        {"name": "geo_distance", "tl_type": "int", "cond": 6},
        {"name": "request_chat_title", "tl_type": "string", "cond": 9},
        {"name": "request_chat_date", "tl_type": "int", "cond": 9},
        {"name": "business_bot_id", "tl_type": "long", "cond": 13},
        {"name": "business_bot_manage_url", "tl_type": "string", "cond": 13},
        {"name": "charge_paid_message_stars", "tl_type": "long", "cond": 14},
        {"name": "registration_month", "tl_type": "string", "cond": 15},
        {"name": "phone_country", "tl_type": "string", "cond": 16},
        {"name": "name_change_date", "tl_type": "int", "cond": 17},
        {"name": "photo_change_date", "tl_type": "int", "cond": 18},
    ],
    "peerStories": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "max_read_id", "tl_type": "int", "cond": 0},
        {"name": "stories", "tl_type": "Vector"},
    ],
    "pendingSuggestion": [
        {"name": "suggestion", "tl_type": "string"},
        {"name": "title", "tl_type": "TextWithEntities"},
        {"name": "description", "tl_type": "TextWithEntities"},
        {"name": "url", "tl_type": "string"},
    ],
    "phoneCallEmpty": [
        {"name": "id", "tl_type": "long"},
    ],
    "phoneCallWaiting": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "video", "tl_type": "true", "cond": 6},
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "admin_id", "tl_type": "long"},
        {"name": "participant_id", "tl_type": "long"},
        {"name": "protocol", "tl_type": "PhoneCallProtocol"},
        {"name": "receive_date", "tl_type": "int", "cond": 0},
    ],
    "phoneCallRequested": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "video", "tl_type": "true", "cond": 6},
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "admin_id", "tl_type": "long"},
        {"name": "participant_id", "tl_type": "long"},
        {"name": "g_a_hash", "tl_type": "bytes"},
        {"name": "protocol", "tl_type": "PhoneCallProtocol"},
    ],
    "phoneCallAccepted": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "video", "tl_type": "true", "cond": 6},
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "admin_id", "tl_type": "long"},
        {"name": "participant_id", "tl_type": "long"},
        {"name": "g_b", "tl_type": "bytes"},
        {"name": "protocol", "tl_type": "PhoneCallProtocol"},
    ],
    "phoneCall": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "p2p_allowed", "tl_type": "true", "cond": 5},
        {"name": "video", "tl_type": "true", "cond": 6},
        {"name": "conference_supported", "tl_type": "true", "cond": 8},
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "admin_id", "tl_type": "long"},
        {"name": "participant_id", "tl_type": "long"},
        {"name": "g_a_or_b", "tl_type": "bytes"},
        {"name": "key_fingerprint", "tl_type": "long"},
        {"name": "protocol", "tl_type": "PhoneCallProtocol"},
        {"name": "connections", "tl_type": "Vector"},
        {"name": "start_date", "tl_type": "int"},
        {"name": "custom_parameters", "tl_type": "DataJSON", "cond": 7},
    ],
    "phoneCallDiscarded": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "need_rating", "tl_type": "true", "cond": 2},
        {"name": "need_debug", "tl_type": "true", "cond": 3},
        {"name": "video", "tl_type": "true", "cond": 6},
        {"name": "id", "tl_type": "long"},
        {"name": "reason", "tl_type": "PhoneCallDiscardReason", "cond": 0},
        {"name": "duration", "tl_type": "int", "cond": 1},
    ],
    "phoneCallDiscardReasonMigrateConferenceCall": [
        {"name": "slug", "tl_type": "string"},
    ],
    "phoneCallProtocol": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "udp_p2p", "tl_type": "true", "cond": 0},
        {"name": "udp_reflector", "tl_type": "true", "cond": 1},
        {"name": "min_layer", "tl_type": "int"},
        {"name": "max_layer", "tl_type": "int"},
        {"name": "library_versions", "tl_type": "Vector"},
    ],
    "phoneConnection": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "tcp", "tl_type": "true", "cond": 0},
        {"name": "id", "tl_type": "long"},
        {"name": "ip", "tl_type": "string"},
        {"name": "ipv6", "tl_type": "string"},
        {"name": "port", "tl_type": "int"},
        {"name": "peer_tag", "tl_type": "bytes"},
    ],
    "phoneConnectionWebrtc": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "turn", "tl_type": "true", "cond": 0},
        {"name": "stun", "tl_type": "true", "cond": 1},
        {"name": "id", "tl_type": "long"},
        {"name": "ip", "tl_type": "string"},
        {"name": "ipv6", "tl_type": "string"},
        {"name": "port", "tl_type": "int"},
        {"name": "username", "tl_type": "string"},
        {"name": "password", "tl_type": "string"},
    ],
    "photoEmpty": [
        {"name": "id", "tl_type": "long"},
    ],
    "photo": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "has_stickers", "tl_type": "true", "cond": 0},
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "file_reference", "tl_type": "bytes"},
        {"name": "date", "tl_type": "int"},
        {"name": "sizes", "tl_type": "Vector"},
        {"name": "video_sizes", "tl_type": "Vector", "cond": 1},
        {"name": "dc_id", "tl_type": "int"},
    ],
    "photoSizeEmpty": [
        {"name": "type", "tl_type": "string"},
    ],
    "photoSize": [
        {"name": "type", "tl_type": "string"},
        {"name": "w", "tl_type": "int"},
        {"name": "h", "tl_type": "int"},
        {"name": "size", "tl_type": "int"},
    ],
    "photoCachedSize": [
        {"name": "type", "tl_type": "string"},
        {"name": "w", "tl_type": "int"},
        {"name": "h", "tl_type": "int"},
        {"name": "bytes", "tl_type": "bytes"},
    ],
    "photoStrippedSize": [
        {"name": "type", "tl_type": "string"},
        {"name": "bytes", "tl_type": "bytes"},
    ],
    "photoSizeProgressive": [
        {"name": "type", "tl_type": "string"},
        {"name": "w", "tl_type": "int"},
        {"name": "h", "tl_type": "int"},
        {"name": "sizes", "tl_type": "Vector"},
    ],
    "photoPathSize": [
        {"name": "type", "tl_type": "string"},
        {"name": "bytes", "tl_type": "bytes"},
    ],
    "poll": [
        {"name": "id", "tl_type": "long"},
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "closed", "tl_type": "true", "cond": 0},
        {"name": "public_voters", "tl_type": "true", "cond": 1},
        {"name": "multiple_choice", "tl_type": "true", "cond": 2},
        {"name": "quiz", "tl_type": "true", "cond": 3},
        {"name": "open_answers", "tl_type": "true", "cond": 6},
        {"name": "revoting_disabled", "tl_type": "true", "cond": 7},
        {"name": "shuffle_answers", "tl_type": "true", "cond": 8},
        {"name": "hide_results_until_close", "tl_type": "true", "cond": 9},
        {"name": "creator", "tl_type": "true", "cond": 10},
        {"name": "subscribers_only", "tl_type": "true", "cond": 11},
        {"name": "question", "tl_type": "TextWithEntities"},
        {"name": "answers", "tl_type": "Vector"},
        {"name": "close_period", "tl_type": "int", "cond": 4},
        {"name": "close_date", "tl_type": "int", "cond": 5},
        {"name": "countries_iso2", "tl_type": "Vector", "cond": 12},
        {"name": "hash", "tl_type": "long"},
    ],
    "pollAnswer": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "text", "tl_type": "TextWithEntities"},
        {"name": "option", "tl_type": "bytes"},
        {"name": "media", "tl_type": "MessageMedia", "cond": 0},
        {"name": "added_by", "tl_type": "Peer", "cond": 1},
        {"name": "date", "tl_type": "int", "cond": 1},
    ],
    "inputPollAnswer": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "text", "tl_type": "TextWithEntities"},
        {"name": "media", "tl_type": "InputMedia", "cond": 0},
    ],
    "pollAnswerVoters": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "chosen", "tl_type": "true", "cond": 0},
        {"name": "correct", "tl_type": "true", "cond": 1},
        {"name": "option", "tl_type": "bytes"},
        {"name": "voters", "tl_type": "int", "cond": 2},
        {"name": "recent_voters", "tl_type": "Vector", "cond": 2},
    ],
    "pollResults": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "min", "tl_type": "true", "cond": 0},
        {"name": "has_unread_votes", "tl_type": "true", "cond": 6},
        {"name": "can_view_stats", "tl_type": "true", "cond": 7},
        {"name": "results", "tl_type": "Vector", "cond": 1},
        {"name": "total_voters", "tl_type": "int", "cond": 2},
        {"name": "recent_voters", "tl_type": "Vector", "cond": 3},
        {"name": "solution", "tl_type": "string", "cond": 4},
        {"name": "solution_entities", "tl_type": "Vector", "cond": 4},
        {"name": "solution_media", "tl_type": "MessageMedia", "cond": 5},
    ],
    "popularContact": [
        {"name": "client_id", "tl_type": "long"},
        {"name": "importers", "tl_type": "int"},
    ],
    "postAddress": [
        {"name": "street_line1", "tl_type": "string"},
        {"name": "street_line2", "tl_type": "string"},
        {"name": "city", "tl_type": "string"},
        {"name": "state", "tl_type": "string"},
        {"name": "country_iso2", "tl_type": "string"},
        {"name": "post_code", "tl_type": "string"},
    ],
    "postInteractionCountersMessage": [
        {"name": "msg_id", "tl_type": "int"},
        {"name": "views", "tl_type": "int"},
        {"name": "forwards", "tl_type": "int"},
        {"name": "reactions", "tl_type": "int"},
    ],
    "postInteractionCountersStory": [
        {"name": "story_id", "tl_type": "int"},
        {"name": "views", "tl_type": "int"},
        {"name": "forwards", "tl_type": "int"},
        {"name": "reactions", "tl_type": "int"},
    ],
    "premiumGiftCodeOption": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "users", "tl_type": "int"},
        {"name": "months", "tl_type": "int"},
        {"name": "store_product", "tl_type": "string", "cond": 0},
        {"name": "store_quantity", "tl_type": "int", "cond": 1},
        {"name": "currency", "tl_type": "string"},
        {"name": "amount", "tl_type": "long"},
    ],
    "premiumSubscriptionOption": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "current", "tl_type": "true", "cond": 1},
        {"name": "can_purchase_upgrade", "tl_type": "true", "cond": 2},
        {"name": "transaction", "tl_type": "string", "cond": 3},
        {"name": "months", "tl_type": "int"},
        {"name": "currency", "tl_type": "string"},
        {"name": "amount", "tl_type": "long"},
        {"name": "bot_url", "tl_type": "string"},
        {"name": "store_product", "tl_type": "string", "cond": 0},
    ],
    "prepaidGiveaway": [
        {"name": "id", "tl_type": "long"},
        {"name": "months", "tl_type": "int"},
        {"name": "quantity", "tl_type": "int"},
        {"name": "date", "tl_type": "int"},
    ],
    "prepaidStarsGiveaway": [
        {"name": "id", "tl_type": "long"},
        {"name": "stars", "tl_type": "long"},
        {"name": "quantity", "tl_type": "int"},
        {"name": "boosts", "tl_type": "int"},
        {"name": "date", "tl_type": "int"},
    ],
    "privacyValueAllowUsers": [
        {"name": "users", "tl_type": "Vector"},
    ],
    "privacyValueDisallowUsers": [
        {"name": "users", "tl_type": "Vector"},
    ],
    "privacyValueAllowChatParticipants": [
        {"name": "chats", "tl_type": "Vector"},
    ],
    "privacyValueDisallowChatParticipants": [
        {"name": "chats", "tl_type": "Vector"},
    ],
    "publicForwardMessage": [
        {"name": "message", "tl_type": "Message"},
    ],
    "publicForwardStory": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "story", "tl_type": "StoryItem"},
    ],
    "quickReply": [
        {"name": "shortcut_id", "tl_type": "int"},
        {"name": "shortcut", "tl_type": "string"},
        {"name": "top_message", "tl_type": "int"},
        {"name": "count", "tl_type": "int"},
    ],
    "reactionEmoji": [
        {"name": "emoticon", "tl_type": "string"},
    ],
    "reactionCustomEmoji": [
        {"name": "document_id", "tl_type": "long"},
    ],
    "reactionCount": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "chosen_order", "tl_type": "int", "cond": 0},
        {"name": "reaction", "tl_type": "Reaction"},
        {"name": "count", "tl_type": "int"},
    ],
    "reactionsNotifySettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "messages_notify_from", "tl_type": "ReactionNotificationsFrom", "cond": 0},
        {"name": "stories_notify_from", "tl_type": "ReactionNotificationsFrom", "cond": 1},
        {"name": "poll_votes_notify_from", "tl_type": "ReactionNotificationsFrom", "cond": 2},
        {"name": "sound", "tl_type": "NotificationSound"},
        {"name": "show_previews", "tl_type": "Bool"},
    ],
    "readParticipantDate": [
        {"name": "user_id", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
    ],
    "receivedNotifyMessage": [
        {"name": "id", "tl_type": "int"},
        {"name": "flags", "tl_type": "int"},
    ],
    "recentMeUrlUnknown": [
        {"name": "url", "tl_type": "string"},
    ],
    "recentMeUrlUser": [
        {"name": "url", "tl_type": "string"},
        {"name": "user_id", "tl_type": "long"},
    ],
    "recentMeUrlChat": [
        {"name": "url", "tl_type": "string"},
        {"name": "chat_id", "tl_type": "long"},
    ],
    "recentMeUrlChatInvite": [
        {"name": "url", "tl_type": "string"},
        {"name": "chat_invite", "tl_type": "ChatInvite"},
    ],
    "recentMeUrlStickerSet": [
        {"name": "url", "tl_type": "string"},
        {"name": "set", "tl_type": "StickerSetCovered"},
    ],
    "recentStory": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "live", "tl_type": "true", "cond": 0},
        {"name": "max_id", "tl_type": "int", "cond": 1},
    ],
    "replyKeyboardHide": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "selective", "tl_type": "true", "cond": 2},
    ],
    "replyKeyboardForceReply": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "single_use", "tl_type": "true", "cond": 1},
        {"name": "selective", "tl_type": "true", "cond": 2},
        {"name": "placeholder", "tl_type": "string", "cond": 3},
    ],
    "replyKeyboardMarkup": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "resize", "tl_type": "true", "cond": 0},
        {"name": "single_use", "tl_type": "true", "cond": 1},
        {"name": "selective", "tl_type": "true", "cond": 2},
        {"name": "persistent", "tl_type": "true", "cond": 4},
        {"name": "rows", "tl_type": "Vector"},
        {"name": "placeholder", "tl_type": "string", "cond": 3},
    ],
    "replyInlineMarkup": [
        {"name": "rows", "tl_type": "Vector"},
    ],
    "reportResultChooseOption": [
        {"name": "title", "tl_type": "string"},
        {"name": "options", "tl_type": "Vector"},
    ],
    "reportResultAddComment": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "optional", "tl_type": "true", "cond": 0},
        {"name": "option", "tl_type": "bytes"},
    ],
    "requestPeerTypeUser": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "bot", "tl_type": "Bool", "cond": 0},
        {"name": "premium", "tl_type": "Bool", "cond": 1},
    ],
    "requestPeerTypeChat": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "creator", "tl_type": "true", "cond": 0},
        {"name": "bot_participant", "tl_type": "true", "cond": 5},
        {"name": "has_username", "tl_type": "Bool", "cond": 3},
        {"name": "forum", "tl_type": "Bool", "cond": 4},
        {"name": "user_admin_rights", "tl_type": "ChatAdminRights", "cond": 1},
        {"name": "bot_admin_rights", "tl_type": "ChatAdminRights", "cond": 2},
    ],
    "requestPeerTypeBroadcast": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "creator", "tl_type": "true", "cond": 0},
        {"name": "has_username", "tl_type": "Bool", "cond": 3},
        {"name": "user_admin_rights", "tl_type": "ChatAdminRights", "cond": 1},
        {"name": "bot_admin_rights", "tl_type": "ChatAdminRights", "cond": 2},
    ],
    "requestPeerTypeCreateBot": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "bot_managed", "tl_type": "true", "cond": 0},
        {"name": "suggested_name", "tl_type": "string", "cond": 1},
        {"name": "suggested_username", "tl_type": "string", "cond": 2},
    ],
    "requestedPeerUser": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "user_id", "tl_type": "long"},
        {"name": "first_name", "tl_type": "string", "cond": 0},
        {"name": "last_name", "tl_type": "string", "cond": 0},
        {"name": "username", "tl_type": "string", "cond": 1},
        {"name": "photo", "tl_type": "Photo", "cond": 2},
    ],
    "requestedPeerChat": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "chat_id", "tl_type": "long"},
        {"name": "title", "tl_type": "string", "cond": 0},
        {"name": "photo", "tl_type": "Photo", "cond": 2},
    ],
    "requestedPeerChannel": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "channel_id", "tl_type": "long"},
        {"name": "title", "tl_type": "string", "cond": 0},
        {"name": "username", "tl_type": "string", "cond": 1},
        {"name": "photo", "tl_type": "Photo", "cond": 2},
    ],
    "requirementToContactPaidMessages": [
        {"name": "stars_amount", "tl_type": "long"},
    ],
    "restrictionReason": [
        {"name": "platform", "tl_type": "string"},
        {"name": "reason", "tl_type": "string"},
        {"name": "text", "tl_type": "string"},
    ],
    "richMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "rtl", "tl_type": "true", "cond": 0},
        {"name": "part", "tl_type": "true", "cond": 1},
        {"name": "blocks", "tl_type": "Vector"},
        {"name": "photos", "tl_type": "Vector"},
        {"name": "documents", "tl_type": "Vector"},
    ],
    "textPlain": [
        {"name": "text", "tl_type": "string"},
    ],
    "textBold": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "textItalic": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "textUnderline": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "textStrike": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "textFixed": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "textUrl": [
        {"name": "text", "tl_type": "RichText"},
        {"name": "url", "tl_type": "string"},
        {"name": "webpage_id", "tl_type": "long"},
    ],
    "textEmail": [
        {"name": "text", "tl_type": "RichText"},
        {"name": "email", "tl_type": "string"},
    ],
    "textConcat": [
        {"name": "texts", "tl_type": "Vector"},
    ],
    "textSubscript": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "textSuperscript": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "textMarked": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "textPhone": [
        {"name": "text", "tl_type": "RichText"},
        {"name": "phone", "tl_type": "string"},
    ],
    "textImage": [
        {"name": "document_id", "tl_type": "long"},
        {"name": "w", "tl_type": "int"},
        {"name": "h", "tl_type": "int"},
    ],
    "textAnchor": [
        {"name": "text", "tl_type": "RichText"},
        {"name": "name", "tl_type": "string"},
    ],
    "textMath": [
        {"name": "source", "tl_type": "string"},
    ],
    "textCustomEmoji": [
        {"name": "document_id", "tl_type": "long"},
        {"name": "alt", "tl_type": "string"},
    ],
    "textSpoiler": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "textMention": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "textHashtag": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "textBotCommand": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "textCashtag": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "textAutoUrl": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "textAutoEmail": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "textAutoPhone": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "textBankCard": [
        {"name": "text", "tl_type": "RichText"},
    ],
    "textMentionName": [
        {"name": "text", "tl_type": "RichText"},
        {"name": "user_id", "tl_type": "long"},
    ],
    "textDate": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "relative", "tl_type": "true", "cond": 0},
        {"name": "short_time", "tl_type": "true", "cond": 1},
        {"name": "long_time", "tl_type": "true", "cond": 2},
        {"name": "short_date", "tl_type": "true", "cond": 3},
        {"name": "long_date", "tl_type": "true", "cond": 4},
        {"name": "day_of_week", "tl_type": "true", "cond": 5},
        {"name": "text", "tl_type": "RichText"},
        {"name": "date", "tl_type": "int"},
    ],
    "savedPhoneContact": [
        {"name": "phone", "tl_type": "string"},
        {"name": "first_name", "tl_type": "string"},
        {"name": "last_name", "tl_type": "string"},
        {"name": "date", "tl_type": "int"},
    ],
    "savedDialog": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "pinned", "tl_type": "true", "cond": 2},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "top_message", "tl_type": "int"},
    ],
    "monoForumDialog": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "unread_mark", "tl_type": "true", "cond": 3},
        {"name": "nopaid_messages_exception", "tl_type": "true", "cond": 4},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "top_message", "tl_type": "int"},
        {"name": "read_inbox_max_id", "tl_type": "int"},
        {"name": "read_outbox_max_id", "tl_type": "int"},
        {"name": "unread_count", "tl_type": "int"},
        {"name": "unread_reactions_count", "tl_type": "int"},
        {"name": "draft", "tl_type": "DraftMessage", "cond": 1},
    ],
    "savedReactionTag": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "reaction", "tl_type": "Reaction"},
        {"name": "title", "tl_type": "string", "cond": 0},
        {"name": "count", "tl_type": "int"},
    ],
    "savedStarGift": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "name_hidden", "tl_type": "true", "cond": 0},
        {"name": "unsaved", "tl_type": "true", "cond": 5},
        {"name": "refunded", "tl_type": "true", "cond": 9},
        {"name": "can_upgrade", "tl_type": "true", "cond": 10},
        {"name": "pinned_to_top", "tl_type": "true", "cond": 12},
        {"name": "upgrade_separate", "tl_type": "true", "cond": 17},
        {"name": "from_id", "tl_type": "Peer", "cond": 1},
        {"name": "date", "tl_type": "int"},
        {"name": "gift", "tl_type": "StarGift"},
        {"name": "message", "tl_type": "TextWithEntities", "cond": 2},
        {"name": "msg_id", "tl_type": "int", "cond": 3},
        {"name": "saved_id", "tl_type": "long", "cond": 11},
        {"name": "convert_stars", "tl_type": "long", "cond": 4},
        {"name": "upgrade_stars", "tl_type": "long", "cond": 6},
        {"name": "can_export_at", "tl_type": "int", "cond": 7},
        {"name": "transfer_stars", "tl_type": "long", "cond": 8},
        {"name": "can_transfer_at", "tl_type": "int", "cond": 13},
        {"name": "can_resell_at", "tl_type": "int", "cond": 14},
        {"name": "collection_id", "tl_type": "Vector", "cond": 15},
        {"name": "prepaid_upgrade_hash", "tl_type": "string", "cond": 16},
        {"name": "drop_original_details_stars", "tl_type": "long", "cond": 18},
        {"name": "gift_num", "tl_type": "int", "cond": 19},
        {"name": "can_craft_at", "tl_type": "int", "cond": 20},
    ],
    "searchPostsFlood": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "query_is_free", "tl_type": "true", "cond": 0},
        {"name": "total_daily", "tl_type": "int"},
        {"name": "remains", "tl_type": "int"},
        {"name": "wait_till", "tl_type": "int", "cond": 1},
        {"name": "stars_amount", "tl_type": "long"},
    ],
    "searchResultsCalendarPeriod": [
        {"name": "date", "tl_type": "int"},
        {"name": "min_msg_id", "tl_type": "int"},
        {"name": "max_msg_id", "tl_type": "int"},
        {"name": "count", "tl_type": "int"},
    ],
    "searchResultPosition": [
        {"name": "msg_id", "tl_type": "int"},
        {"name": "date", "tl_type": "int"},
        {"name": "offset", "tl_type": "int"},
    ],
    "secureCredentialsEncrypted": [
        {"name": "data", "tl_type": "bytes"},
        {"name": "hash", "tl_type": "bytes"},
        {"name": "secret", "tl_type": "bytes"},
    ],
    "secureData": [
        {"name": "data", "tl_type": "bytes"},
        {"name": "data_hash", "tl_type": "bytes"},
        {"name": "secret", "tl_type": "bytes"},
    ],
    "secureFile": [
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "size", "tl_type": "long"},
        {"name": "dc_id", "tl_type": "int"},
        {"name": "date", "tl_type": "int"},
        {"name": "file_hash", "tl_type": "bytes"},
        {"name": "secret", "tl_type": "bytes"},
    ],
    "securePasswordKdfAlgoPBKDF2HMACSHA512iter100000": [
        {"name": "salt", "tl_type": "bytes"},
    ],
    "securePasswordKdfAlgoSHA512": [
        {"name": "salt", "tl_type": "bytes"},
    ],
    "securePlainPhone": [
        {"name": "phone", "tl_type": "string"},
    ],
    "securePlainEmail": [
        {"name": "email", "tl_type": "string"},
    ],
    "secureRequiredType": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "native_names", "tl_type": "true", "cond": 0},
        {"name": "selfie_required", "tl_type": "true", "cond": 1},
        {"name": "translation_required", "tl_type": "true", "cond": 2},
        {"name": "type", "tl_type": "SecureValueType"},
    ],
    "secureRequiredTypeOneOf": [
        {"name": "types", "tl_type": "Vector"},
    ],
    "secureSecretSettings": [
        {"name": "secure_algo", "tl_type": "SecurePasswordKdfAlgo"},
        {"name": "secure_secret", "tl_type": "bytes"},
        {"name": "secure_secret_id", "tl_type": "long"},
    ],
    "secureValue": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "type", "tl_type": "SecureValueType"},
        {"name": "data", "tl_type": "SecureData", "cond": 0},
        {"name": "front_side", "tl_type": "SecureFile", "cond": 1},
        {"name": "reverse_side", "tl_type": "SecureFile", "cond": 2},
        {"name": "selfie", "tl_type": "SecureFile", "cond": 3},
        {"name": "translation", "tl_type": "Vector", "cond": 6},
        {"name": "files", "tl_type": "Vector", "cond": 4},
        {"name": "plain_data", "tl_type": "SecurePlainData", "cond": 5},
        {"name": "hash", "tl_type": "bytes"},
    ],
    "secureValueErrorData": [
        {"name": "type", "tl_type": "SecureValueType"},
        {"name": "data_hash", "tl_type": "bytes"},
        {"name": "field", "tl_type": "string"},
        {"name": "text", "tl_type": "string"},
    ],
    "secureValueErrorFrontSide": [
        {"name": "type", "tl_type": "SecureValueType"},
        {"name": "file_hash", "tl_type": "bytes"},
        {"name": "text", "tl_type": "string"},
    ],
    "secureValueErrorReverseSide": [
        {"name": "type", "tl_type": "SecureValueType"},
        {"name": "file_hash", "tl_type": "bytes"},
        {"name": "text", "tl_type": "string"},
    ],
    "secureValueErrorSelfie": [
        {"name": "type", "tl_type": "SecureValueType"},
        {"name": "file_hash", "tl_type": "bytes"},
        {"name": "text", "tl_type": "string"},
    ],
    "secureValueErrorFile": [
        {"name": "type", "tl_type": "SecureValueType"},
        {"name": "file_hash", "tl_type": "bytes"},
        {"name": "text", "tl_type": "string"},
    ],
    "secureValueErrorFiles": [
        {"name": "type", "tl_type": "SecureValueType"},
        {"name": "file_hash", "tl_type": "Vector"},
        {"name": "text", "tl_type": "string"},
    ],
    "secureValueError": [
        {"name": "type", "tl_type": "SecureValueType"},
        {"name": "hash", "tl_type": "bytes"},
        {"name": "text", "tl_type": "string"},
    ],
    "secureValueErrorTranslationFile": [
        {"name": "type", "tl_type": "SecureValueType"},
        {"name": "file_hash", "tl_type": "bytes"},
        {"name": "text", "tl_type": "string"},
    ],
    "secureValueErrorTranslationFiles": [
        {"name": "type", "tl_type": "SecureValueType"},
        {"name": "file_hash", "tl_type": "Vector"},
        {"name": "text", "tl_type": "string"},
    ],
    "secureValueHash": [
        {"name": "type", "tl_type": "SecureValueType"},
        {"name": "hash", "tl_type": "bytes"},
    ],
    "sendAsPeer": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "premium_required", "tl_type": "true", "cond": 0},
        {"name": "peer", "tl_type": "Peer"},
    ],
    "sendMessageUploadVideoAction": [
        {"name": "progress", "tl_type": "int"},
    ],
    "sendMessageUploadAudioAction": [
        {"name": "progress", "tl_type": "int"},
    ],
    "sendMessageUploadPhotoAction": [
        {"name": "progress", "tl_type": "int"},
    ],
    "sendMessageUploadDocumentAction": [
        {"name": "progress", "tl_type": "int"},
    ],
    "sendMessageUploadRoundAction": [
        {"name": "progress", "tl_type": "int"},
    ],
    "sendMessageHistoryImportAction": [
        {"name": "progress", "tl_type": "int"},
    ],
    "sendMessageEmojiInteraction": [
        {"name": "emoticon", "tl_type": "string"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "interaction", "tl_type": "DataJSON"},
    ],
    "sendMessageEmojiInteractionSeen": [
        {"name": "emoticon", "tl_type": "string"},
    ],
    "sendMessageTextDraftAction": [
        {"name": "random_id", "tl_type": "long"},
        {"name": "text", "tl_type": "TextWithEntities"},
    ],
    "inputSendMessageRichMessageDraftAction": [
        {"name": "random_id", "tl_type": "long"},
        {"name": "rich_message", "tl_type": "InputRichMessage"},
    ],
    "sendMessageRichMessageDraftAction": [
        {"name": "random_id", "tl_type": "long"},
        {"name": "rich_message", "tl_type": "RichMessage"},
    ],
    "shippingOption": [
        {"name": "id", "tl_type": "string"},
        {"name": "title", "tl_type": "string"},
        {"name": "prices", "tl_type": "Vector"},
    ],
    "smsJob": [
        {"name": "job_id", "tl_type": "string"},
        {"name": "phone_number", "tl_type": "string"},
        {"name": "text", "tl_type": "string"},
    ],
    "sponsoredMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "recommended", "tl_type": "true", "cond": 5},
        {"name": "can_report", "tl_type": "true", "cond": 12},
        {"name": "random_id", "tl_type": "bytes"},
        {"name": "url", "tl_type": "string"},
        {"name": "title", "tl_type": "string"},
        {"name": "message", "tl_type": "string"},
        {"name": "entities", "tl_type": "Vector", "cond": 1},
        {"name": "photo", "tl_type": "Photo", "cond": 6},
        {"name": "media", "tl_type": "MessageMedia", "cond": 14},
        {"name": "color", "tl_type": "PeerColor", "cond": 13},
        {"name": "button_text", "tl_type": "string"},
        {"name": "sponsor_info", "tl_type": "string", "cond": 7},
        {"name": "additional_info", "tl_type": "string", "cond": 8},
        {"name": "min_display_duration", "tl_type": "int", "cond": 15},
        {"name": "max_display_duration", "tl_type": "int", "cond": 15},
    ],
    "sponsoredMessageReportOption": [
        {"name": "text", "tl_type": "string"},
        {"name": "option", "tl_type": "bytes"},
    ],
    "sponsoredPeer": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "random_id", "tl_type": "bytes"},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "sponsor_info", "tl_type": "string", "cond": 0},
        {"name": "additional_info", "tl_type": "string", "cond": 1},
    ],
    "starGift": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "limited", "tl_type": "true", "cond": 0},
        {"name": "sold_out", "tl_type": "true", "cond": 1},
        {"name": "birthday", "tl_type": "true", "cond": 2},
        {"name": "require_premium", "tl_type": "true", "cond": 7},
        {"name": "limited_per_user", "tl_type": "true", "cond": 8},
        {"name": "peer_color_available", "tl_type": "true", "cond": 10},
        {"name": "auction", "tl_type": "true", "cond": 11},
        {"name": "id", "tl_type": "long"},
        {"name": "sticker", "tl_type": "Document"},
        {"name": "stars", "tl_type": "long"},
        {"name": "availability_remains", "tl_type": "int", "cond": 0},
        {"name": "availability_total", "tl_type": "int", "cond": 0},
        {"name": "availability_resale", "tl_type": "long", "cond": 4},
        {"name": "convert_stars", "tl_type": "long"},
        {"name": "first_sale_date", "tl_type": "int", "cond": 1},
        {"name": "last_sale_date", "tl_type": "int", "cond": 1},
        {"name": "upgrade_stars", "tl_type": "long", "cond": 3},
        {"name": "resell_min_stars", "tl_type": "long", "cond": 4},
        {"name": "title", "tl_type": "string", "cond": 5},
        {"name": "released_by", "tl_type": "Peer", "cond": 6},
        {"name": "per_user_total", "tl_type": "int", "cond": 8},
        {"name": "per_user_remains", "tl_type": "int", "cond": 8},
        {"name": "locked_until_date", "tl_type": "int", "cond": 9},
        {"name": "auction_slug", "tl_type": "string", "cond": 11},
        {"name": "gifts_per_round", "tl_type": "int", "cond": 11},
        {"name": "auction_start_date", "tl_type": "int", "cond": 11},
        {"name": "upgrade_variants", "tl_type": "int", "cond": 12},
        {"name": "background", "tl_type": "StarGiftBackground", "cond": 13},
    ],
    "starGiftUnique": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "require_premium", "tl_type": "true", "cond": 6},
        {"name": "resale_ton_only", "tl_type": "true", "cond": 7},
        {"name": "theme_available", "tl_type": "true", "cond": 9},
        {"name": "burned", "tl_type": "true", "cond": 14},
        {"name": "crafted", "tl_type": "true", "cond": 15},
        {"name": "id", "tl_type": "long"},
        {"name": "gift_id", "tl_type": "long"},
        {"name": "title", "tl_type": "string"},
        {"name": "slug", "tl_type": "string"},
        {"name": "num", "tl_type": "int"},
        {"name": "owner_id", "tl_type": "Peer", "cond": 0},
        {"name": "owner_name", "tl_type": "string", "cond": 1},
        {"name": "owner_address", "tl_type": "string", "cond": 2},
        {"name": "attributes", "tl_type": "Vector"},
        {"name": "availability_issued", "tl_type": "int"},
        {"name": "availability_total", "tl_type": "int"},
        {"name": "gift_address", "tl_type": "string", "cond": 3},
        {"name": "resell_amount", "tl_type": "Vector", "cond": 4},
        {"name": "released_by", "tl_type": "Peer", "cond": 5},
        {"name": "value_amount", "tl_type": "long", "cond": 8},
        {"name": "value_currency", "tl_type": "string", "cond": 8},
        {"name": "value_usd_amount", "tl_type": "long", "cond": 8},
        {"name": "theme_peer", "tl_type": "Peer", "cond": 10},
        {"name": "peer_color", "tl_type": "PeerColor", "cond": 11},
        {"name": "host_id", "tl_type": "Peer", "cond": 12},
        {"name": "offer_min_stars", "tl_type": "int", "cond": 13},
        {"name": "craft_chance_permille", "tl_type": "int", "cond": 16},
    ],
    "starGiftActiveAuctionState": [
        {"name": "gift", "tl_type": "StarGift"},
        {"name": "state", "tl_type": "StarGiftAuctionState"},
        {"name": "user_state", "tl_type": "StarGiftAuctionUserState"},
    ],
    "starGiftAttributeModel": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "crafted", "tl_type": "true", "cond": 0},
        {"name": "name", "tl_type": "string"},
        {"name": "document", "tl_type": "Document"},
        {"name": "rarity", "tl_type": "StarGiftAttributeRarity"},
    ],
    "starGiftAttributePattern": [
        {"name": "name", "tl_type": "string"},
        {"name": "document", "tl_type": "Document"},
        {"name": "rarity", "tl_type": "StarGiftAttributeRarity"},
    ],
    "starGiftAttributeBackdrop": [
        {"name": "name", "tl_type": "string"},
        {"name": "backdrop_id", "tl_type": "int"},
        {"name": "center_color", "tl_type": "int"},
        {"name": "edge_color", "tl_type": "int"},
        {"name": "pattern_color", "tl_type": "int"},
        {"name": "text_color", "tl_type": "int"},
        {"name": "rarity", "tl_type": "StarGiftAttributeRarity"},
    ],
    "starGiftAttributeOriginalDetails": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "sender_id", "tl_type": "Peer", "cond": 0},
        {"name": "recipient_id", "tl_type": "Peer"},
        {"name": "date", "tl_type": "int"},
        {"name": "message", "tl_type": "TextWithEntities", "cond": 1},
    ],
    "starGiftAttributeCounter": [
        {"name": "attribute", "tl_type": "StarGiftAttributeId"},
        {"name": "count", "tl_type": "int"},
    ],
    "starGiftAttributeIdModel": [
        {"name": "document_id", "tl_type": "long"},
    ],
    "starGiftAttributeIdPattern": [
        {"name": "document_id", "tl_type": "long"},
    ],
    "starGiftAttributeIdBackdrop": [
        {"name": "backdrop_id", "tl_type": "int"},
    ],
    "starGiftAttributeRarity": [
        {"name": "permille", "tl_type": "int"},
    ],
    "starGiftAuctionAcquiredGift": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "name_hidden", "tl_type": "true", "cond": 0},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "date", "tl_type": "int"},
        {"name": "bid_amount", "tl_type": "long"},
        {"name": "round", "tl_type": "int"},
        {"name": "pos", "tl_type": "int"},
        {"name": "message", "tl_type": "TextWithEntities", "cond": 1},
        {"name": "gift_num", "tl_type": "int", "cond": 2},
    ],
    "starGiftAuctionRound": [
        {"name": "num", "tl_type": "int"},
        {"name": "duration", "tl_type": "int"},
    ],
    "starGiftAuctionRoundExtendable": [
        {"name": "num", "tl_type": "int"},
        {"name": "duration", "tl_type": "int"},
        {"name": "extend_top", "tl_type": "int"},
        {"name": "extend_window", "tl_type": "int"},
    ],
    "starGiftAuctionState": [
        {"name": "version", "tl_type": "int"},
        {"name": "start_date", "tl_type": "int"},
        {"name": "end_date", "tl_type": "int"},
        {"name": "min_bid_amount", "tl_type": "long"},
        {"name": "bid_levels", "tl_type": "Vector"},
        {"name": "top_bidders", "tl_type": "Vector"},
        {"name": "next_round_at", "tl_type": "int"},
        {"name": "last_gift_num", "tl_type": "int"},
        {"name": "gifts_left", "tl_type": "int"},
        {"name": "current_round", "tl_type": "int"},
        {"name": "total_rounds", "tl_type": "int"},
        {"name": "rounds", "tl_type": "Vector"},
    ],
    "starGiftAuctionStateFinished": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "start_date", "tl_type": "int"},
        {"name": "end_date", "tl_type": "int"},
        {"name": "average_price", "tl_type": "long"},
        {"name": "listed_count", "tl_type": "int", "cond": 0},
        {"name": "fragment_listed_count", "tl_type": "int", "cond": 1},
        {"name": "fragment_listed_url", "tl_type": "string", "cond": 1},
    ],
    "starGiftAuctionUserState": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "returned", "tl_type": "true", "cond": 1},
        {"name": "bid_amount", "tl_type": "long", "cond": 0},
        {"name": "bid_date", "tl_type": "int", "cond": 0},
        {"name": "min_bid_amount", "tl_type": "long", "cond": 0},
        {"name": "bid_peer", "tl_type": "Peer", "cond": 0},
        {"name": "acquired_count", "tl_type": "int"},
    ],
    "starGiftBackground": [
        {"name": "center_color", "tl_type": "int"},
        {"name": "edge_color", "tl_type": "int"},
        {"name": "text_color", "tl_type": "int"},
    ],
    "starGiftCollection": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "collection_id", "tl_type": "int"},
        {"name": "title", "tl_type": "string"},
        {"name": "icon", "tl_type": "Document", "cond": 0},
        {"name": "gifts_count", "tl_type": "int"},
        {"name": "hash", "tl_type": "long"},
    ],
    "starGiftUpgradePrice": [
        {"name": "date", "tl_type": "int"},
        {"name": "upgrade_stars", "tl_type": "long"},
    ],
    "starRefProgram": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "bot_id", "tl_type": "long"},
        {"name": "commission_permille", "tl_type": "int"},
        {"name": "duration_months", "tl_type": "int", "cond": 0},
        {"name": "end_date", "tl_type": "int", "cond": 1},
        {"name": "daily_revenue_per_user", "tl_type": "StarsAmount", "cond": 2},
    ],
    "starsAmount": [
        {"name": "amount", "tl_type": "long"},
        {"name": "nanos", "tl_type": "int"},
    ],
    "starsTonAmount": [
        {"name": "amount", "tl_type": "long"},
    ],
    "starsGiftOption": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "extended", "tl_type": "true", "cond": 1},
        {"name": "stars", "tl_type": "long"},
        {"name": "store_product", "tl_type": "string", "cond": 0},
        {"name": "currency", "tl_type": "string"},
        {"name": "amount", "tl_type": "long"},
    ],
    "starsGiveawayOption": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "extended", "tl_type": "true", "cond": 0},
        {"name": "default", "tl_type": "true", "cond": 1},
        {"name": "stars", "tl_type": "long"},
        {"name": "yearly_boosts", "tl_type": "int"},
        {"name": "store_product", "tl_type": "string", "cond": 2},
        {"name": "currency", "tl_type": "string"},
        {"name": "amount", "tl_type": "long"},
        {"name": "winners", "tl_type": "Vector"},
    ],
    "starsGiveawayWinnersOption": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "default", "tl_type": "true", "cond": 0},
        {"name": "users", "tl_type": "int"},
        {"name": "per_user_stars", "tl_type": "long"},
    ],
    "starsRating": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "level", "tl_type": "int"},
        {"name": "current_level_stars", "tl_type": "long"},
        {"name": "stars", "tl_type": "long"},
        {"name": "next_level_stars", "tl_type": "long", "cond": 0},
    ],
    "starsRevenueStatus": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "withdrawal_enabled", "tl_type": "true", "cond": 0},
        {"name": "current_balance", "tl_type": "StarsAmount"},
        {"name": "available_balance", "tl_type": "StarsAmount"},
        {"name": "overall_revenue", "tl_type": "StarsAmount"},
        {"name": "next_withdrawal_at", "tl_type": "int", "cond": 1},
    ],
    "starsSubscription": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "canceled", "tl_type": "true", "cond": 0},
        {"name": "can_refulfill", "tl_type": "true", "cond": 1},
        {"name": "missing_balance", "tl_type": "true", "cond": 2},
        {"name": "bot_canceled", "tl_type": "true", "cond": 7},
        {"name": "id", "tl_type": "string"},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "until_date", "tl_type": "int"},
        {"name": "pricing", "tl_type": "StarsSubscriptionPricing"},
        {"name": "chat_invite_hash", "tl_type": "string", "cond": 3},
        {"name": "title", "tl_type": "string", "cond": 4},
        {"name": "photo", "tl_type": "WebDocument", "cond": 5},
        {"name": "invoice_slug", "tl_type": "string", "cond": 6},
    ],
    "starsSubscriptionPricing": [
        {"name": "period", "tl_type": "int"},
        {"name": "amount", "tl_type": "long"},
    ],
    "starsTopupOption": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "extended", "tl_type": "true", "cond": 1},
        {"name": "stars", "tl_type": "long"},
        {"name": "store_product", "tl_type": "string", "cond": 0},
        {"name": "currency", "tl_type": "string"},
        {"name": "amount", "tl_type": "long"},
    ],
    "starsTransaction": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "refund", "tl_type": "true", "cond": 3},
        {"name": "pending", "tl_type": "true", "cond": 4},
        {"name": "failed", "tl_type": "true", "cond": 6},
        {"name": "gift", "tl_type": "true", "cond": 10},
        {"name": "reaction", "tl_type": "true", "cond": 11},
        {"name": "stargift_upgrade", "tl_type": "true", "cond": 18},
        {"name": "business_transfer", "tl_type": "true", "cond": 21},
        {"name": "stargift_resale", "tl_type": "true", "cond": 22},
        {"name": "posts_search", "tl_type": "true", "cond": 24},
        {"name": "stargift_prepaid_upgrade", "tl_type": "true", "cond": 25},
        {"name": "stargift_drop_original_details", "tl_type": "true", "cond": 26},
        {"name": "phonegroup_message", "tl_type": "true", "cond": 27},
        {"name": "stargift_auction_bid", "tl_type": "true", "cond": 28},
        {"name": "offer", "tl_type": "true", "cond": 29},
        {"name": "id", "tl_type": "string"},
        {"name": "amount", "tl_type": "StarsAmount"},
        {"name": "date", "tl_type": "int"},
        {"name": "peer", "tl_type": "StarsTransactionPeer"},
        {"name": "title", "tl_type": "string", "cond": 0},
        {"name": "description", "tl_type": "string", "cond": 1},
        {"name": "photo", "tl_type": "WebDocument", "cond": 2},
        {"name": "transaction_date", "tl_type": "int", "cond": 5},
        {"name": "transaction_url", "tl_type": "string", "cond": 5},
        {"name": "bot_payload", "tl_type": "bytes", "cond": 7},
        {"name": "msg_id", "tl_type": "int", "cond": 8},
        {"name": "extended_media", "tl_type": "Vector", "cond": 9},
        {"name": "subscription_period", "tl_type": "int", "cond": 12},
        {"name": "giveaway_post_id", "tl_type": "int", "cond": 13},
        {"name": "stargift", "tl_type": "StarGift", "cond": 14},
        {"name": "floodskip_number", "tl_type": "int", "cond": 15},
        {"name": "starref_commission_permille", "tl_type": "int", "cond": 16},
        {"name": "starref_peer", "tl_type": "Peer", "cond": 17},
        {"name": "starref_amount", "tl_type": "StarsAmount", "cond": 17},
        {"name": "paid_messages", "tl_type": "int", "cond": 19},
        {"name": "premium_gift_months", "tl_type": "int", "cond": 20},
        {"name": "ads_proceeds_from_date", "tl_type": "int", "cond": 23},
        {"name": "ads_proceeds_to_date", "tl_type": "int", "cond": 23},
    ],
    "starsTransactionPeer": [
        {"name": "peer", "tl_type": "Peer"},
    ],
    "statsAbsValueAndPrev": [
        {"name": "current", "tl_type": "double"},
        {"name": "previous", "tl_type": "double"},
    ],
    "statsDateRangeDays": [
        {"name": "min_date", "tl_type": "int"},
        {"name": "max_date", "tl_type": "int"},
    ],
    "statsGraphAsync": [
        {"name": "token", "tl_type": "string"},
    ],
    "statsGraphError": [
        {"name": "error", "tl_type": "string"},
    ],
    "statsGraph": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "json", "tl_type": "DataJSON"},
        {"name": "zoom_token", "tl_type": "string", "cond": 0},
    ],
    "statsGroupTopAdmin": [
        {"name": "user_id", "tl_type": "long"},
        {"name": "deleted", "tl_type": "int"},
        {"name": "kicked", "tl_type": "int"},
        {"name": "banned", "tl_type": "int"},
    ],
    "statsGroupTopInviter": [
        {"name": "user_id", "tl_type": "long"},
        {"name": "invitations", "tl_type": "int"},
    ],
    "statsGroupTopPoster": [
        {"name": "user_id", "tl_type": "long"},
        {"name": "messages", "tl_type": "int"},
        {"name": "avg_chars", "tl_type": "int"},
    ],
    "statsPercentValue": [
        {"name": "part", "tl_type": "double"},
        {"name": "total", "tl_type": "double"},
    ],
    "statsURL": [
        {"name": "url", "tl_type": "string"},
    ],
    "stickerKeyword": [
        {"name": "document_id", "tl_type": "long"},
        {"name": "keyword", "tl_type": "Vector"},
    ],
    "stickerPack": [
        {"name": "emoticon", "tl_type": "string"},
        {"name": "documents", "tl_type": "Vector"},
    ],
    "stickerSet": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "archived", "tl_type": "true", "cond": 1},
        {"name": "official", "tl_type": "true", "cond": 2},
        {"name": "masks", "tl_type": "true", "cond": 3},
        {"name": "emojis", "tl_type": "true", "cond": 7},
        {"name": "text_color", "tl_type": "true", "cond": 9},
        {"name": "channel_emoji_status", "tl_type": "true", "cond": 10},
        {"name": "creator", "tl_type": "true", "cond": 11},
        {"name": "installed_date", "tl_type": "int", "cond": 0},
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "title", "tl_type": "string"},
        {"name": "short_name", "tl_type": "string"},
        {"name": "thumbs", "tl_type": "Vector", "cond": 4},
        {"name": "thumb_dc_id", "tl_type": "int", "cond": 4},
        {"name": "thumb_version", "tl_type": "int", "cond": 4},
        {"name": "thumb_document_id", "tl_type": "long", "cond": 8},
        {"name": "count", "tl_type": "int"},
        {"name": "hash", "tl_type": "int"},
    ],
    "stickerSetCovered": [
        {"name": "set", "tl_type": "StickerSet"},
        {"name": "cover", "tl_type": "Document"},
    ],
    "stickerSetMultiCovered": [
        {"name": "set", "tl_type": "StickerSet"},
        {"name": "covers", "tl_type": "Vector"},
    ],
    "stickerSetFullCovered": [
        {"name": "set", "tl_type": "StickerSet"},
        {"name": "packs", "tl_type": "Vector"},
        {"name": "keywords", "tl_type": "Vector"},
        {"name": "documents", "tl_type": "Vector"},
    ],
    "stickerSetNoCovered": [
        {"name": "set", "tl_type": "StickerSet"},
    ],
    "storiesStealthMode": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "active_until_date", "tl_type": "int", "cond": 0},
        {"name": "cooldown_until_date", "tl_type": "int", "cond": 1},
    ],
    "storyAlbum": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "album_id", "tl_type": "int"},
        {"name": "title", "tl_type": "string"},
        {"name": "icon_photo", "tl_type": "Photo", "cond": 0},
        {"name": "icon_video", "tl_type": "Document", "cond": 1},
    ],
    "storyFwdHeader": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "modified", "tl_type": "true", "cond": 3},
        {"name": "from", "tl_type": "Peer", "cond": 0},
        {"name": "from_name", "tl_type": "string", "cond": 1},
        {"name": "story_id", "tl_type": "int", "cond": 2},
    ],
    "storyItemDeleted": [
        {"name": "id", "tl_type": "int"},
    ],
    "storyItemSkipped": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "close_friends", "tl_type": "true", "cond": 8},
        {"name": "live", "tl_type": "true", "cond": 9},
        {"name": "id", "tl_type": "int"},
        {"name": "date", "tl_type": "int"},
        {"name": "expire_date", "tl_type": "int"},
    ],
    "storyItem": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "pinned", "tl_type": "true", "cond": 5},
        {"name": "public", "tl_type": "true", "cond": 7},
        {"name": "close_friends", "tl_type": "true", "cond": 8},
        {"name": "min", "tl_type": "true", "cond": 9},
        {"name": "noforwards", "tl_type": "true", "cond": 10},
        {"name": "edited", "tl_type": "true", "cond": 11},
        {"name": "contacts", "tl_type": "true", "cond": 12},
        {"name": "selected_contacts", "tl_type": "true", "cond": 13},
        {"name": "out", "tl_type": "true", "cond": 16},
        {"name": "id", "tl_type": "int"},
        {"name": "date", "tl_type": "int"},
        {"name": "from_id", "tl_type": "Peer", "cond": 18},
        {"name": "fwd_from", "tl_type": "StoryFwdHeader", "cond": 17},
        {"name": "expire_date", "tl_type": "int"},
        {"name": "caption", "tl_type": "string", "cond": 0},
        {"name": "entities", "tl_type": "Vector", "cond": 1},
        {"name": "media", "tl_type": "MessageMedia"},
        {"name": "media_areas", "tl_type": "Vector", "cond": 14},
        {"name": "privacy", "tl_type": "Vector", "cond": 2},
        {"name": "views", "tl_type": "StoryViews", "cond": 3},
        {"name": "sent_reaction", "tl_type": "Reaction", "cond": 15},
        {"name": "albums", "tl_type": "Vector", "cond": 19},
        {"name": "music", "tl_type": "Document", "cond": 20},
    ],
    "storyReaction": [
        {"name": "peer_id", "tl_type": "Peer"},
        {"name": "date", "tl_type": "int"},
        {"name": "reaction", "tl_type": "Reaction"},
    ],
    "storyReactionPublicForward": [
        {"name": "message", "tl_type": "Message"},
    ],
    "storyReactionPublicRepost": [
        {"name": "peer_id", "tl_type": "Peer"},
        {"name": "story", "tl_type": "StoryItem"},
    ],
    "storyView": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "blocked", "tl_type": "true", "cond": 0},
        {"name": "blocked_my_stories_from", "tl_type": "true", "cond": 1},
        {"name": "user_id", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "reaction", "tl_type": "Reaction", "cond": 2},
    ],
    "storyViewPublicForward": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "blocked", "tl_type": "true", "cond": 0},
        {"name": "blocked_my_stories_from", "tl_type": "true", "cond": 1},
        {"name": "message", "tl_type": "Message"},
    ],
    "storyViewPublicRepost": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "blocked", "tl_type": "true", "cond": 0},
        {"name": "blocked_my_stories_from", "tl_type": "true", "cond": 1},
        {"name": "peer_id", "tl_type": "Peer"},
        {"name": "story", "tl_type": "StoryItem"},
    ],
    "storyViews": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "has_viewers", "tl_type": "true", "cond": 1},
        {"name": "views_count", "tl_type": "int"},
        {"name": "forwards_count", "tl_type": "int", "cond": 2},
        {"name": "reactions", "tl_type": "Vector", "cond": 3},
        {"name": "reactions_count", "tl_type": "int", "cond": 4},
        {"name": "recent_viewers", "tl_type": "Vector", "cond": 0},
    ],
    "suggestedPost": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "accepted", "tl_type": "true", "cond": 1},
        {"name": "rejected", "tl_type": "true", "cond": 2},
        {"name": "price", "tl_type": "StarsAmount", "cond": 3},
        {"name": "schedule_date", "tl_type": "int", "cond": 0},
    ],
    "textWithEntities": [
        {"name": "text", "tl_type": "string"},
        {"name": "entities", "tl_type": "Vector"},
    ],
    "theme": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "creator", "tl_type": "true", "cond": 0},
        {"name": "default", "tl_type": "true", "cond": 1},
        {"name": "for_chat", "tl_type": "true", "cond": 5},
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "slug", "tl_type": "string"},
        {"name": "title", "tl_type": "string"},
        {"name": "document", "tl_type": "Document", "cond": 2},
        {"name": "settings", "tl_type": "Vector", "cond": 3},
        {"name": "emoticon", "tl_type": "string", "cond": 6},
        {"name": "installs_count", "tl_type": "int", "cond": 4},
    ],
    "themeSettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "message_colors_animated", "tl_type": "true", "cond": 2},
        {"name": "base_theme", "tl_type": "BaseTheme"},
        {"name": "accent_color", "tl_type": "int"},
        {"name": "outbox_accent_color", "tl_type": "int", "cond": 3},
        {"name": "message_colors", "tl_type": "Vector", "cond": 0},
        {"name": "wallpaper", "tl_type": "WallPaper", "cond": 1},
    ],
    "timezone": [
        {"name": "id", "tl_type": "string"},
        {"name": "name", "tl_type": "string"},
        {"name": "utc_offset", "tl_type": "int"},
    ],
    "todoCompletion": [
        {"name": "id", "tl_type": "int"},
        {"name": "completed_by", "tl_type": "Peer"},
        {"name": "date", "tl_type": "int"},
    ],
    "todoItem": [
        {"name": "id", "tl_type": "int"},
        {"name": "title", "tl_type": "TextWithEntities"},
    ],
    "todoList": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "others_can_append", "tl_type": "true", "cond": 0},
        {"name": "others_can_complete", "tl_type": "true", "cond": 1},
        {"name": "title", "tl_type": "TextWithEntities"},
        {"name": "list", "tl_type": "Vector"},
    ],
    "topPeer": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "rating", "tl_type": "double"},
    ],
    "topPeerCategoryPeers": [
        {"name": "category", "tl_type": "TopPeerCategory"},
        {"name": "count", "tl_type": "int"},
        {"name": "peers", "tl_type": "Vector"},
    ],
    "updateNewMessage": [
        {"name": "message", "tl_type": "Message"},
        {"name": "pts", "tl_type": "int"},
        {"name": "pts_count", "tl_type": "int"},
    ],
    "updateMessageID": [
        {"name": "id", "tl_type": "int"},
        {"name": "random_id", "tl_type": "long"},
    ],
    "updateDeleteMessages": [
        {"name": "messages", "tl_type": "Vector"},
        {"name": "pts", "tl_type": "int"},
        {"name": "pts_count", "tl_type": "int"},
    ],
    "updateUserTyping": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "user_id", "tl_type": "long"},
        {"name": "top_msg_id", "tl_type": "int", "cond": 0},
        {"name": "action", "tl_type": "SendMessageAction"},
    ],
    "updateChatUserTyping": [
        {"name": "chat_id", "tl_type": "long"},
        {"name": "from_id", "tl_type": "Peer"},
        {"name": "action", "tl_type": "SendMessageAction"},
    ],
    "updateChatParticipants": [
        {"name": "participants", "tl_type": "ChatParticipants"},
    ],
    "updateUserStatus": [
        {"name": "user_id", "tl_type": "long"},
        {"name": "status", "tl_type": "UserStatus"},
    ],
    "updateUserName": [
        {"name": "user_id", "tl_type": "long"},
        {"name": "first_name", "tl_type": "string"},
        {"name": "last_name", "tl_type": "string"},
        {"name": "usernames", "tl_type": "Vector"},
    ],
    "updateNewAuthorization": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "unconfirmed", "tl_type": "true", "cond": 0},
        {"name": "hash", "tl_type": "long"},
        {"name": "date", "tl_type": "int", "cond": 0},
        {"name": "device", "tl_type": "string", "cond": 0},
        {"name": "location", "tl_type": "string", "cond": 0},
    ],
    "updateNewEncryptedMessage": [
        {"name": "message", "tl_type": "EncryptedMessage"},
        {"name": "qts", "tl_type": "int"},
    ],
    "updateEncryptedChatTyping": [
        {"name": "chat_id", "tl_type": "int"},
    ],
    "updateEncryption": [
        {"name": "chat", "tl_type": "EncryptedChat"},
        {"name": "date", "tl_type": "int"},
    ],
    "updateEncryptedMessagesRead": [
        {"name": "chat_id", "tl_type": "int"},
        {"name": "max_date", "tl_type": "int"},
        {"name": "date", "tl_type": "int"},
    ],
    "updateChatParticipantAdd": [
        {"name": "chat_id", "tl_type": "long"},
        {"name": "user_id", "tl_type": "long"},
        {"name": "inviter_id", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "version", "tl_type": "int"},
    ],
    "updateChatParticipantDelete": [
        {"name": "chat_id", "tl_type": "long"},
        {"name": "user_id", "tl_type": "long"},
        {"name": "version", "tl_type": "int"},
    ],
    "updateDcOptions": [
        {"name": "dc_options", "tl_type": "Vector"},
    ],
    "updateNotifySettings": [
        {"name": "peer", "tl_type": "NotifyPeer"},
        {"name": "notify_settings", "tl_type": "PeerNotifySettings"},
    ],
    "updateServiceNotification": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "popup", "tl_type": "true", "cond": 0},
        {"name": "invert_media", "tl_type": "true", "cond": 2},
        {"name": "inbox_date", "tl_type": "int", "cond": 1},
        {"name": "type", "tl_type": "string"},
        {"name": "message", "tl_type": "string"},
        {"name": "media", "tl_type": "MessageMedia"},
        {"name": "entities", "tl_type": "Vector"},
    ],
    "updatePrivacy": [
        {"name": "key", "tl_type": "PrivacyKey"},
        {"name": "rules", "tl_type": "Vector"},
    ],
    "updateUserPhone": [
        {"name": "user_id", "tl_type": "long"},
        {"name": "phone", "tl_type": "string"},
    ],
    "updateReadHistoryInbox": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "folder_id", "tl_type": "int", "cond": 0},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "top_msg_id", "tl_type": "int", "cond": 1},
        {"name": "max_id", "tl_type": "int"},
        {"name": "still_unread_count", "tl_type": "int"},
        {"name": "pts", "tl_type": "int"},
        {"name": "pts_count", "tl_type": "int"},
    ],
    "updateReadHistoryOutbox": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "max_id", "tl_type": "int"},
        {"name": "pts", "tl_type": "int"},
        {"name": "pts_count", "tl_type": "int"},
    ],
    "updateWebPage": [
        {"name": "webpage", "tl_type": "WebPage"},
        {"name": "pts", "tl_type": "int"},
        {"name": "pts_count", "tl_type": "int"},
    ],
    "updateReadMessagesContents": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "messages", "tl_type": "Vector"},
        {"name": "pts", "tl_type": "int"},
        {"name": "pts_count", "tl_type": "int"},
        {"name": "date", "tl_type": "int", "cond": 0},
    ],
    "updateChannelTooLong": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "channel_id", "tl_type": "long"},
        {"name": "pts", "tl_type": "int", "cond": 0},
    ],
    "updateChannel": [
        {"name": "channel_id", "tl_type": "long"},
    ],
    "updateNewChannelMessage": [
        {"name": "message", "tl_type": "Message"},
        {"name": "pts", "tl_type": "int"},
        {"name": "pts_count", "tl_type": "int"},
    ],
    "updateReadChannelInbox": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "folder_id", "tl_type": "int", "cond": 0},
        {"name": "channel_id", "tl_type": "long"},
        {"name": "max_id", "tl_type": "int"},
        {"name": "still_unread_count", "tl_type": "int"},
        {"name": "pts", "tl_type": "int"},
    ],
    "updateDeleteChannelMessages": [
        {"name": "channel_id", "tl_type": "long"},
        {"name": "messages", "tl_type": "Vector"},
        {"name": "pts", "tl_type": "int"},
        {"name": "pts_count", "tl_type": "int"},
    ],
    "updateChannelMessageViews": [
        {"name": "channel_id", "tl_type": "long"},
        {"name": "id", "tl_type": "int"},
        {"name": "views", "tl_type": "int"},
    ],
    "updateChatParticipantAdmin": [
        {"name": "chat_id", "tl_type": "long"},
        {"name": "user_id", "tl_type": "long"},
        {"name": "is_admin", "tl_type": "Bool"},
        {"name": "version", "tl_type": "int"},
    ],
    "updateNewStickerSet": [
        {"name": "stickerset", "tl_type": "messages.StickerSet"},
    ],
    "updateStickerSetsOrder": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "masks", "tl_type": "true", "cond": 0},
        {"name": "emojis", "tl_type": "true", "cond": 1},
        {"name": "order", "tl_type": "Vector"},
    ],
    "updateStickerSets": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "masks", "tl_type": "true", "cond": 0},
        {"name": "emojis", "tl_type": "true", "cond": 1},
    ],
    "updateBotInlineQuery": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "query_id", "tl_type": "long"},
        {"name": "user_id", "tl_type": "long"},
        {"name": "query", "tl_type": "string"},
        {"name": "geo", "tl_type": "GeoPoint", "cond": 0},
        {"name": "peer_type", "tl_type": "InlineQueryPeerType", "cond": 1},
        {"name": "offset", "tl_type": "string"},
    ],
    "updateBotInlineSend": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "user_id", "tl_type": "long"},
        {"name": "query", "tl_type": "string"},
        {"name": "geo", "tl_type": "GeoPoint", "cond": 0},
        {"name": "id", "tl_type": "string"},
        {"name": "msg_id", "tl_type": "InputBotInlineMessageID", "cond": 1},
    ],
    "updateEditChannelMessage": [
        {"name": "message", "tl_type": "Message"},
        {"name": "pts", "tl_type": "int"},
        {"name": "pts_count", "tl_type": "int"},
    ],
    "updateBotCallbackQuery": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "query_id", "tl_type": "long"},
        {"name": "user_id", "tl_type": "long"},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "chat_instance", "tl_type": "long"},
        {"name": "data", "tl_type": "bytes", "cond": 0},
        {"name": "game_short_name", "tl_type": "string", "cond": 1},
    ],
    "updateEditMessage": [
        {"name": "message", "tl_type": "Message"},
        {"name": "pts", "tl_type": "int"},
        {"name": "pts_count", "tl_type": "int"},
    ],
    "updateInlineBotCallbackQuery": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "query_id", "tl_type": "long"},
        {"name": "user_id", "tl_type": "long"},
        {"name": "msg_id", "tl_type": "InputBotInlineMessageID"},
        {"name": "chat_instance", "tl_type": "long"},
        {"name": "data", "tl_type": "bytes", "cond": 0},
        {"name": "game_short_name", "tl_type": "string", "cond": 1},
    ],
    "updateReadChannelOutbox": [
        {"name": "channel_id", "tl_type": "long"},
        {"name": "max_id", "tl_type": "int"},
    ],
    "updateDraftMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "top_msg_id", "tl_type": "int", "cond": 0},
        {"name": "saved_peer_id", "tl_type": "Peer", "cond": 1},
        {"name": "draft", "tl_type": "DraftMessage"},
    ],
    "updateChannelWebPage": [
        {"name": "channel_id", "tl_type": "long"},
        {"name": "webpage", "tl_type": "WebPage"},
        {"name": "pts", "tl_type": "int"},
        {"name": "pts_count", "tl_type": "int"},
    ],
    "updateDialogPinned": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "pinned", "tl_type": "true", "cond": 0},
        {"name": "folder_id", "tl_type": "int", "cond": 1},
        {"name": "peer", "tl_type": "DialogPeer"},
    ],
    "updatePinnedDialogs": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "folder_id", "tl_type": "int", "cond": 1},
        {"name": "order", "tl_type": "Vector", "cond": 0},
    ],
    "updateBotWebhookJSON": [
        {"name": "data", "tl_type": "DataJSON"},
    ],
    "updateBotWebhookJSONQuery": [
        {"name": "query_id", "tl_type": "long"},
        {"name": "data", "tl_type": "DataJSON"},
        {"name": "timeout", "tl_type": "int"},
    ],
    "updateBotShippingQuery": [
        {"name": "query_id", "tl_type": "long"},
        {"name": "user_id", "tl_type": "long"},
        {"name": "payload", "tl_type": "bytes"},
        {"name": "shipping_address", "tl_type": "PostAddress"},
    ],
    "updateBotPrecheckoutQuery": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "query_id", "tl_type": "long"},
        {"name": "user_id", "tl_type": "long"},
        {"name": "payload", "tl_type": "bytes"},
        {"name": "info", "tl_type": "PaymentRequestedInfo", "cond": 0},
        {"name": "shipping_option_id", "tl_type": "string", "cond": 1},
        {"name": "currency", "tl_type": "string"},
        {"name": "total_amount", "tl_type": "long"},
    ],
    "updatePhoneCall": [
        {"name": "phone_call", "tl_type": "PhoneCall"},
    ],
    "updateLangPackTooLong": [
        {"name": "lang_code", "tl_type": "string"},
    ],
    "updateLangPack": [
        {"name": "difference", "tl_type": "LangPackDifference"},
    ],
    "updateChannelReadMessagesContents": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "channel_id", "tl_type": "long"},
        {"name": "top_msg_id", "tl_type": "int", "cond": 0},
        {"name": "saved_peer_id", "tl_type": "Peer", "cond": 1},
        {"name": "messages", "tl_type": "Vector"},
    ],
    "updateChannelAvailableMessages": [
        {"name": "channel_id", "tl_type": "long"},
        {"name": "available_min_id", "tl_type": "int"},
    ],
    "updateDialogUnreadMark": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "unread", "tl_type": "true", "cond": 0},
        {"name": "peer", "tl_type": "DialogPeer"},
        {"name": "saved_peer_id", "tl_type": "Peer", "cond": 1},
    ],
    "updateMessagePoll": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "Peer", "cond": 1},
        {"name": "msg_id", "tl_type": "int", "cond": 1},
        {"name": "top_msg_id", "tl_type": "int", "cond": 2},
        {"name": "poll_id", "tl_type": "long"},
        {"name": "poll", "tl_type": "Poll", "cond": 0},
        {"name": "results", "tl_type": "PollResults"},
    ],
    "updateChatDefaultBannedRights": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "default_banned_rights", "tl_type": "ChatBannedRights"},
        {"name": "version", "tl_type": "int"},
    ],
    "updateFolderPeers": [
        {"name": "folder_peers", "tl_type": "Vector"},
        {"name": "pts", "tl_type": "int"},
        {"name": "pts_count", "tl_type": "int"},
    ],
    "updatePeerSettings": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "settings", "tl_type": "PeerSettings"},
    ],
    "updatePeerLocated": [
        {"name": "peers", "tl_type": "Vector"},
    ],
    "updateNewScheduledMessage": [
        {"name": "message", "tl_type": "Message"},
    ],
    "updateDeleteScheduledMessages": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "messages", "tl_type": "Vector"},
        {"name": "sent_messages", "tl_type": "Vector", "cond": 0},
    ],
    "updateTheme": [
        {"name": "theme", "tl_type": "Theme"},
    ],
    "updateGeoLiveViewed": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "msg_id", "tl_type": "int"},
    ],
    "updateMessagePollVote": [
        {"name": "poll_id", "tl_type": "long"},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "options", "tl_type": "Vector"},
        {"name": "positions", "tl_type": "Vector"},
        {"name": "qts", "tl_type": "int"},
    ],
    "updateDialogFilter": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "id", "tl_type": "int"},
        {"name": "filter", "tl_type": "DialogFilter", "cond": 0},
    ],
    "updateDialogFilterOrder": [
        {"name": "order", "tl_type": "Vector"},
    ],
    "updatePhoneCallSignalingData": [
        {"name": "phone_call_id", "tl_type": "long"},
        {"name": "data", "tl_type": "bytes"},
    ],
    "updateChannelMessageForwards": [
        {"name": "channel_id", "tl_type": "long"},
        {"name": "id", "tl_type": "int"},
        {"name": "forwards", "tl_type": "int"},
    ],
    "updateReadChannelDiscussionInbox": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "channel_id", "tl_type": "long"},
        {"name": "top_msg_id", "tl_type": "int"},
        {"name": "read_max_id", "tl_type": "int"},
        {"name": "broadcast_id", "tl_type": "long", "cond": 0},
        {"name": "broadcast_post", "tl_type": "int", "cond": 0},
    ],
    "updateReadChannelDiscussionOutbox": [
        {"name": "channel_id", "tl_type": "long"},
        {"name": "top_msg_id", "tl_type": "int"},
        {"name": "read_max_id", "tl_type": "int"},
    ],
    "updatePeerBlocked": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "blocked", "tl_type": "true", "cond": 0},
        {"name": "blocked_my_stories_from", "tl_type": "true", "cond": 1},
        {"name": "peer_id", "tl_type": "Peer"},
    ],
    "updateChannelUserTyping": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "channel_id", "tl_type": "long"},
        {"name": "top_msg_id", "tl_type": "int", "cond": 0},
        {"name": "from_id", "tl_type": "Peer"},
        {"name": "action", "tl_type": "SendMessageAction"},
    ],
    "updatePinnedMessages": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "pinned", "tl_type": "true", "cond": 0},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "messages", "tl_type": "Vector"},
        {"name": "pts", "tl_type": "int"},
        {"name": "pts_count", "tl_type": "int"},
    ],
    "updatePinnedChannelMessages": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "pinned", "tl_type": "true", "cond": 0},
        {"name": "channel_id", "tl_type": "long"},
        {"name": "messages", "tl_type": "Vector"},
        {"name": "pts", "tl_type": "int"},
        {"name": "pts_count", "tl_type": "int"},
    ],
    "updateChat": [
        {"name": "chat_id", "tl_type": "long"},
    ],
    "updateGroupCallParticipants": [
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "participants", "tl_type": "Vector"},
        {"name": "version", "tl_type": "int"},
    ],
    "updateGroupCall": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "live_story", "tl_type": "true", "cond": 2},
        {"name": "peer", "tl_type": "Peer", "cond": 1},
        {"name": "call", "tl_type": "GroupCall"},
    ],
    "updatePeerHistoryTTL": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "ttl_period", "tl_type": "int", "cond": 0},
    ],
    "updateChatParticipant": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "chat_id", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "actor_id", "tl_type": "long"},
        {"name": "user_id", "tl_type": "long"},
        {"name": "prev_participant", "tl_type": "ChatParticipant", "cond": 0},
        {"name": "new_participant", "tl_type": "ChatParticipant", "cond": 1},
        {"name": "invite", "tl_type": "ExportedChatInvite", "cond": 2},
        {"name": "qts", "tl_type": "int"},
    ],
    "updateChannelParticipant": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "via_chatlist", "tl_type": "true", "cond": 3},
        {"name": "channel_id", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "actor_id", "tl_type": "long"},
        {"name": "user_id", "tl_type": "long"},
        {"name": "prev_participant", "tl_type": "ChannelParticipant", "cond": 0},
        {"name": "new_participant", "tl_type": "ChannelParticipant", "cond": 1},
        {"name": "invite", "tl_type": "ExportedChatInvite", "cond": 2},
        {"name": "qts", "tl_type": "int"},
    ],
    "updateBotStopped": [
        {"name": "user_id", "tl_type": "long"},
        {"name": "date", "tl_type": "int"},
        {"name": "stopped", "tl_type": "Bool"},
        {"name": "qts", "tl_type": "int"},
    ],
    "updateGroupCallConnection": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "presentation", "tl_type": "true", "cond": 0},
        {"name": "params", "tl_type": "DataJSON"},
    ],
    "updateBotCommands": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "bot_id", "tl_type": "long"},
        {"name": "commands", "tl_type": "Vector"},
    ],
    "updatePendingJoinRequests": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "requests_pending", "tl_type": "int"},
        {"name": "recent_requesters", "tl_type": "Vector"},
    ],
    "updateBotChatInviteRequester": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "date", "tl_type": "int"},
        {"name": "user_id", "tl_type": "long"},
        {"name": "about", "tl_type": "string"},
        {"name": "invite", "tl_type": "ExportedChatInvite"},
        {"name": "qts", "tl_type": "int"},
        {"name": "query_id", "tl_type": "long", "cond": 0},
    ],
    "updateMessageReactions": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "top_msg_id", "tl_type": "int", "cond": 0},
        {"name": "saved_peer_id", "tl_type": "Peer", "cond": 1},
        {"name": "reactions", "tl_type": "MessageReactions"},
    ],
    "updateWebViewResultSent": [
        {"name": "query_id", "tl_type": "long"},
    ],
    "updateBotMenuButton": [
        {"name": "bot_id", "tl_type": "long"},
        {"name": "button", "tl_type": "BotMenuButton"},
    ],
    "updateTranscribedAudio": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "pending", "tl_type": "true", "cond": 0},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "transcription_id", "tl_type": "long"},
        {"name": "text", "tl_type": "string"},
    ],
    "updateUserEmojiStatus": [
        {"name": "user_id", "tl_type": "long"},
        {"name": "emoji_status", "tl_type": "EmojiStatus"},
    ],
    "updateMoveStickerSetToTop": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "masks", "tl_type": "true", "cond": 0},
        {"name": "emojis", "tl_type": "true", "cond": 1},
        {"name": "stickerset", "tl_type": "long"},
    ],
    "updateMessageExtendedMedia": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "extended_media", "tl_type": "Vector"},
    ],
    "updateUser": [
        {"name": "user_id", "tl_type": "long"},
    ],
    "updateStory": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "story", "tl_type": "StoryItem"},
    ],
    "updateReadStories": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "max_id", "tl_type": "int"},
    ],
    "updateStoryID": [
        {"name": "id", "tl_type": "int"},
        {"name": "random_id", "tl_type": "long"},
    ],
    "updateStoriesStealthMode": [
        {"name": "stealth_mode", "tl_type": "StoriesStealthMode"},
    ],
    "updateSentStoryReaction": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "story_id", "tl_type": "int"},
        {"name": "reaction", "tl_type": "Reaction"},
    ],
    "updateBotChatBoost": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "boost", "tl_type": "Boost"},
        {"name": "qts", "tl_type": "int"},
    ],
    "updateChannelViewForumAsMessages": [
        {"name": "channel_id", "tl_type": "long"},
        {"name": "enabled", "tl_type": "Bool"},
    ],
    "updatePeerWallpaper": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "wallpaper_overridden", "tl_type": "true", "cond": 1},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "wallpaper", "tl_type": "WallPaper", "cond": 0},
    ],
    "updateBotMessageReaction": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "date", "tl_type": "int"},
        {"name": "actor", "tl_type": "Peer"},
        {"name": "old_reactions", "tl_type": "Vector"},
        {"name": "new_reactions", "tl_type": "Vector"},
        {"name": "qts", "tl_type": "int"},
    ],
    "updateBotMessageReactions": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "date", "tl_type": "int"},
        {"name": "reactions", "tl_type": "Vector"},
        {"name": "qts", "tl_type": "int"},
    ],
    "updateSavedDialogPinned": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "pinned", "tl_type": "true", "cond": 0},
        {"name": "peer", "tl_type": "DialogPeer"},
    ],
    "updatePinnedSavedDialogs": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "order", "tl_type": "Vector", "cond": 0},
    ],
    "updateSmsJob": [
        {"name": "job_id", "tl_type": "string"},
    ],
    "updateQuickReplies": [
        {"name": "quick_replies", "tl_type": "Vector"},
    ],
    "updateNewQuickReply": [
        {"name": "quick_reply", "tl_type": "QuickReply"},
    ],
    "updateDeleteQuickReply": [
        {"name": "shortcut_id", "tl_type": "int"},
    ],
    "updateQuickReplyMessage": [
        {"name": "message", "tl_type": "Message"},
    ],
    "updateDeleteQuickReplyMessages": [
        {"name": "shortcut_id", "tl_type": "int"},
        {"name": "messages", "tl_type": "Vector"},
    ],
    "updateBotBusinessConnect": [
        {"name": "connection", "tl_type": "BotBusinessConnection"},
        {"name": "qts", "tl_type": "int"},
    ],
    "updateBotNewBusinessMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "connection_id", "tl_type": "string"},
        {"name": "message", "tl_type": "Message"},
        {"name": "reply_to_message", "tl_type": "Message", "cond": 0},
        {"name": "qts", "tl_type": "int"},
    ],
    "updateBotEditBusinessMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "connection_id", "tl_type": "string"},
        {"name": "message", "tl_type": "Message"},
        {"name": "reply_to_message", "tl_type": "Message", "cond": 0},
        {"name": "qts", "tl_type": "int"},
    ],
    "updateBotDeleteBusinessMessage": [
        {"name": "connection_id", "tl_type": "string"},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "messages", "tl_type": "Vector"},
        {"name": "qts", "tl_type": "int"},
    ],
    "updateNewStoryReaction": [
        {"name": "story_id", "tl_type": "int"},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "reaction", "tl_type": "Reaction"},
    ],
    "updateStarsBalance": [
        {"name": "balance", "tl_type": "StarsAmount"},
    ],
    "updateBusinessBotCallbackQuery": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "query_id", "tl_type": "long"},
        {"name": "user_id", "tl_type": "long"},
        {"name": "connection_id", "tl_type": "string"},
        {"name": "message", "tl_type": "Message"},
        {"name": "reply_to_message", "tl_type": "Message", "cond": 2},
        {"name": "chat_instance", "tl_type": "long"},
        {"name": "data", "tl_type": "bytes", "cond": 0},
    ],
    "updateStarsRevenueStatus": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "status", "tl_type": "StarsRevenueStatus"},
    ],
    "updateBotPurchasedPaidMedia": [
        {"name": "user_id", "tl_type": "long"},
        {"name": "payload", "tl_type": "string"},
        {"name": "qts", "tl_type": "int"},
    ],
    "updatePaidReactionPrivacy": [
        {"name": "private", "tl_type": "PaidReactionPrivacy"},
    ],
    "updateSentPhoneCode": [
        {"name": "sent_code", "tl_type": "auth.SentCode"},
    ],
    "updateGroupCallChainBlocks": [
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "sub_chain_id", "tl_type": "int"},
        {"name": "blocks", "tl_type": "Vector"},
        {"name": "next_offset", "tl_type": "int"},
    ],
    "updateReadMonoForumInbox": [
        {"name": "channel_id", "tl_type": "long"},
        {"name": "saved_peer_id", "tl_type": "Peer"},
        {"name": "read_max_id", "tl_type": "int"},
    ],
    "updateReadMonoForumOutbox": [
        {"name": "channel_id", "tl_type": "long"},
        {"name": "saved_peer_id", "tl_type": "Peer"},
        {"name": "read_max_id", "tl_type": "int"},
    ],
    "updateMonoForumNoPaidException": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "exception", "tl_type": "true", "cond": 0},
        {"name": "channel_id", "tl_type": "long"},
        {"name": "saved_peer_id", "tl_type": "Peer"},
    ],
    "updateGroupCallMessage": [
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "message", "tl_type": "GroupCallMessage"},
    ],
    "updateGroupCallEncryptedMessage": [
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "from_id", "tl_type": "Peer"},
        {"name": "encrypted_message", "tl_type": "bytes"},
    ],
    "updatePinnedForumTopic": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "pinned", "tl_type": "true", "cond": 0},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "topic_id", "tl_type": "int"},
    ],
    "updatePinnedForumTopics": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "order", "tl_type": "Vector", "cond": 0},
    ],
    "updateDeleteGroupCallMessages": [
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "messages", "tl_type": "Vector"},
    ],
    "updateStarGiftAuctionState": [
        {"name": "gift_id", "tl_type": "long"},
        {"name": "state", "tl_type": "StarGiftAuctionState"},
    ],
    "updateStarGiftAuctionUserState": [
        {"name": "gift_id", "tl_type": "long"},
        {"name": "user_state", "tl_type": "StarGiftAuctionUserState"},
    ],
    "updateEmojiGameInfo": [
        {"name": "info", "tl_type": "messages.EmojiGameInfo"},
    ],
    "updateChatParticipantRank": [
        {"name": "chat_id", "tl_type": "long"},
        {"name": "user_id", "tl_type": "long"},
        {"name": "rank", "tl_type": "string"},
        {"name": "version", "tl_type": "int"},
    ],
    "updateManagedBot": [
        {"name": "user_id", "tl_type": "long"},
        {"name": "bot_id", "tl_type": "long"},
        {"name": "qts", "tl_type": "int"},
    ],
    "updateBotGuestChatQuery": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "query_id", "tl_type": "long"},
        {"name": "message", "tl_type": "Message"},
        {"name": "reference_messages", "tl_type": "Vector", "cond": 0},
        {"name": "qts", "tl_type": "int"},
    ],
    "updateJoinChatWebViewDecision": [
        {"name": "peer", "tl_type": "Peer"},
        {"name": "query_id", "tl_type": "long"},
        {"name": "result", "tl_type": "JoinChatBotResult"},
    ],
    "updateNewBotConnection": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "confirmed", "tl_type": "true", "cond": 0},
        {"name": "bot_id", "tl_type": "long"},
        {"name": "date", "tl_type": "int", "cond": 1},
        {"name": "device", "tl_type": "string", "cond": 1},
        {"name": "location", "tl_type": "string", "cond": 1},
    ],
    "updateWebBrowserSettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "open_external_browser", "tl_type": "true", "cond": 0},
        {"name": "display_close_button", "tl_type": "true", "cond": 1},
    ],
    "updateWebBrowserException": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "delete", "tl_type": "true", "cond": 1},
        {"name": "open_external_browser", "tl_type": "Bool", "cond": 0},
        {"name": "exception", "tl_type": "WebDomainException"},
    ],
    "updateShortMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "out", "tl_type": "true", "cond": 1},
        {"name": "mentioned", "tl_type": "true", "cond": 4},
        {"name": "media_unread", "tl_type": "true", "cond": 5},
        {"name": "silent", "tl_type": "true", "cond": 13},
        {"name": "id", "tl_type": "int"},
        {"name": "user_id", "tl_type": "long"},
        {"name": "message", "tl_type": "string"},
        {"name": "pts", "tl_type": "int"},
        {"name": "pts_count", "tl_type": "int"},
        {"name": "date", "tl_type": "int"},
        {"name": "fwd_from", "tl_type": "MessageFwdHeader", "cond": 2},
        {"name": "via_bot_id", "tl_type": "long", "cond": 11},
        {"name": "reply_to", "tl_type": "MessageReplyHeader", "cond": 3},
        {"name": "entities", "tl_type": "Vector", "cond": 7},
        {"name": "ttl_period", "tl_type": "int", "cond": 25},
    ],
    "updateShortChatMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "out", "tl_type": "true", "cond": 1},
        {"name": "mentioned", "tl_type": "true", "cond": 4},
        {"name": "media_unread", "tl_type": "true", "cond": 5},
        {"name": "silent", "tl_type": "true", "cond": 13},
        {"name": "id", "tl_type": "int"},
        {"name": "from_id", "tl_type": "long"},
        {"name": "chat_id", "tl_type": "long"},
        {"name": "message", "tl_type": "string"},
        {"name": "pts", "tl_type": "int"},
        {"name": "pts_count", "tl_type": "int"},
        {"name": "date", "tl_type": "int"},
        {"name": "fwd_from", "tl_type": "MessageFwdHeader", "cond": 2},
        {"name": "via_bot_id", "tl_type": "long", "cond": 11},
        {"name": "reply_to", "tl_type": "MessageReplyHeader", "cond": 3},
        {"name": "entities", "tl_type": "Vector", "cond": 7},
        {"name": "ttl_period", "tl_type": "int", "cond": 25},
    ],
    "updateShort": [
        {"name": "update", "tl_type": "Update"},
        {"name": "date", "tl_type": "int"},
    ],
    "updatesCombined": [
        {"name": "updates", "tl_type": "Vector"},
        {"name": "users", "tl_type": "Vector"},
        {"name": "chats", "tl_type": "Vector"},
        {"name": "date", "tl_type": "int"},
        {"name": "seq_start", "tl_type": "int"},
        {"name": "seq", "tl_type": "int"},
    ],
    "updates": [
        {"name": "updates", "tl_type": "Vector"},
        {"name": "users", "tl_type": "Vector"},
        {"name": "chats", "tl_type": "Vector"},
        {"name": "date", "tl_type": "int"},
        {"name": "seq", "tl_type": "int"},
    ],
    "updateShortSentMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "out", "tl_type": "true", "cond": 1},
        {"name": "id", "tl_type": "int"},
        {"name": "pts", "tl_type": "int"},
        {"name": "pts_count", "tl_type": "int"},
        {"name": "date", "tl_type": "int"},
        {"name": "media", "tl_type": "MessageMedia", "cond": 9},
        {"name": "entities", "tl_type": "Vector", "cond": 7},
        {"name": "ttl_period", "tl_type": "int", "cond": 25},
    ],
    "urlAuthResultRequest": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "request_write_access", "tl_type": "true", "cond": 0},
        {"name": "request_phone_number", "tl_type": "true", "cond": 1},
        {"name": "match_codes_first", "tl_type": "true", "cond": 5},
        {"name": "is_app", "tl_type": "true", "cond": 6},
        {"name": "bot", "tl_type": "User"},
        {"name": "domain", "tl_type": "string"},
        {"name": "browser", "tl_type": "string", "cond": 2},
        {"name": "platform", "tl_type": "string", "cond": 2},
        {"name": "ip", "tl_type": "string", "cond": 2},
        {"name": "region", "tl_type": "string", "cond": 2},
        {"name": "match_codes", "tl_type": "Vector", "cond": 3},
        {"name": "user_id_hint", "tl_type": "long", "cond": 4},
        {"name": "verified_app_name", "tl_type": "string", "cond": 7},
    ],
    "urlAuthResultAccepted": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "url", "tl_type": "string", "cond": 0},
    ],
    "userEmpty": [
        {"name": "id", "tl_type": "long"},
    ],
    "user": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "self", "tl_type": "true", "cond": 10},
        {"name": "contact", "tl_type": "true", "cond": 11},
        {"name": "mutual_contact", "tl_type": "true", "cond": 12},
        {"name": "deleted", "tl_type": "true", "cond": 13},
        {"name": "bot", "tl_type": "true", "cond": 14},
        {"name": "bot_chat_history", "tl_type": "true", "cond": 15},
        {"name": "bot_nochats", "tl_type": "true", "cond": 16},
        {"name": "verified", "tl_type": "true", "cond": 17},
        {"name": "restricted", "tl_type": "true", "cond": 18},
        {"name": "min", "tl_type": "true", "cond": 20},
        {"name": "bot_inline_geo", "tl_type": "true", "cond": 21},
        {"name": "support", "tl_type": "true", "cond": 23},
        {"name": "scam", "tl_type": "true", "cond": 24},
        {"name": "apply_min_photo", "tl_type": "true", "cond": 25},
        {"name": "fake", "tl_type": "true", "cond": 26},
        {"name": "bot_attach_menu", "tl_type": "true", "cond": 27},
        {"name": "premium", "tl_type": "true", "cond": 28},
        {"name": "attach_menu_enabled", "tl_type": "true", "cond": 29},
        {"name": "flags2", "tl_type": "flags", "is_flag": True},
        {"name": "bot_can_edit", "tl_type": "flags2.1?true"},
        {"name": "close_friend", "tl_type": "flags2.2?true"},
        {"name": "stories_hidden", "tl_type": "flags2.3?true"},
        {"name": "stories_unavailable", "tl_type": "flags2.4?true"},
        {"name": "contact_require_premium", "tl_type": "flags2.10?true"},
        {"name": "bot_business", "tl_type": "flags2.11?true"},
        {"name": "bot_has_main_app", "tl_type": "flags2.13?true"},
        {"name": "bot_forum_view", "tl_type": "flags2.16?true"},
        {"name": "bot_forum_can_manage_topics", "tl_type": "flags2.17?true"},
        {"name": "bot_can_manage_bots", "tl_type": "flags2.18?true"},
        {"name": "bot_guestchat", "tl_type": "flags2.19?true"},
        {"name": "bot_guard", "tl_type": "flags2.20?true"},
        {"name": "id", "tl_type": "long"},
        {"name": "access_hash", "tl_type": "long", "cond": 0},
        {"name": "first_name", "tl_type": "string", "cond": 1},
        {"name": "last_name", "tl_type": "string", "cond": 2},
        {"name": "username", "tl_type": "string", "cond": 3},
        {"name": "phone", "tl_type": "string", "cond": 4},
        {"name": "photo", "tl_type": "UserProfilePhoto", "cond": 5},
        {"name": "status", "tl_type": "UserStatus", "cond": 6},
        {"name": "bot_info_version", "tl_type": "int", "cond": 14},
        {"name": "restriction_reason", "tl_type": "Vector", "cond": 18},
        {"name": "bot_inline_placeholder", "tl_type": "string", "cond": 19},
        {"name": "lang_code", "tl_type": "string", "cond": 22},
        {"name": "emoji_status", "tl_type": "EmojiStatus", "cond": 30},
        {"name": "usernames", "tl_type": "flags2.0?Vector"},
        {"name": "stories_max_id", "tl_type": "flags2.5?RecentStory"},
        {"name": "color", "tl_type": "flags2.8?PeerColor"},
        {"name": "profile_color", "tl_type": "flags2.9?PeerColor"},
        {"name": "bot_active_users", "tl_type": "flags2.12?int"},
        {"name": "bot_verification_icon", "tl_type": "flags2.14?long"},
        {"name": "send_paid_messages_stars", "tl_type": "flags2.15?long"},
    ],
    "userFull": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "blocked", "tl_type": "true", "cond": 0},
        {"name": "phone_calls_available", "tl_type": "true", "cond": 4},
        {"name": "phone_calls_private", "tl_type": "true", "cond": 5},
        {"name": "can_pin_message", "tl_type": "true", "cond": 7},
        {"name": "has_scheduled", "tl_type": "true", "cond": 12},
        {"name": "video_calls_available", "tl_type": "true", "cond": 13},
        {"name": "voice_messages_forbidden", "tl_type": "true", "cond": 20},
        {"name": "translations_disabled", "tl_type": "true", "cond": 23},
        {"name": "stories_pinned_available", "tl_type": "true", "cond": 26},
        {"name": "blocked_my_stories_from", "tl_type": "true", "cond": 27},
        {"name": "wallpaper_overridden", "tl_type": "true", "cond": 28},
        {"name": "contact_require_premium", "tl_type": "true", "cond": 29},
        {"name": "read_dates_private", "tl_type": "true", "cond": 30},
        {"name": "flags2", "tl_type": "flags", "is_flag": True},
        {"name": "sponsored_enabled", "tl_type": "flags2.7?true"},
        {"name": "can_view_revenue", "tl_type": "flags2.9?true"},
        {"name": "bot_can_manage_emoji_status", "tl_type": "flags2.10?true"},
        {"name": "display_gifts_button", "tl_type": "flags2.16?true"},
        {"name": "noforwards_my_enabled", "tl_type": "flags2.23?true"},
        {"name": "noforwards_peer_enabled", "tl_type": "flags2.24?true"},
        {"name": "unofficial_security_risk", "tl_type": "flags2.26?true"},
        {"name": "id", "tl_type": "long"},
        {"name": "about", "tl_type": "string", "cond": 1},
        {"name": "settings", "tl_type": "PeerSettings"},
        {"name": "personal_photo", "tl_type": "Photo", "cond": 21},
        {"name": "profile_photo", "tl_type": "Photo", "cond": 2},
        {"name": "fallback_photo", "tl_type": "Photo", "cond": 22},
        {"name": "notify_settings", "tl_type": "PeerNotifySettings"},
        {"name": "bot_info", "tl_type": "BotInfo", "cond": 3},
        {"name": "pinned_msg_id", "tl_type": "int", "cond": 6},
        {"name": "common_chats_count", "tl_type": "int"},
        {"name": "folder_id", "tl_type": "int", "cond": 11},
        {"name": "ttl_period", "tl_type": "int", "cond": 14},
        {"name": "theme", "tl_type": "ChatTheme", "cond": 15},
        {"name": "private_forward_name", "tl_type": "string", "cond": 16},
        {"name": "bot_group_admin_rights", "tl_type": "ChatAdminRights", "cond": 17},
        {"name": "bot_broadcast_admin_rights", "tl_type": "ChatAdminRights", "cond": 18},
        {"name": "wallpaper", "tl_type": "WallPaper", "cond": 24},
        {"name": "stories", "tl_type": "PeerStories", "cond": 25},
        {"name": "business_work_hours", "tl_type": "flags2.0?BusinessWorkHours"},
        {"name": "business_location", "tl_type": "flags2.1?BusinessLocation"},
        {"name": "business_greeting_message", "tl_type": "flags2.2?BusinessGreetingMessage"},
        {"name": "business_away_message", "tl_type": "flags2.3?BusinessAwayMessage"},
        {"name": "business_intro", "tl_type": "flags2.4?BusinessIntro"},
        {"name": "birthday", "tl_type": "flags2.5?Birthday"},
        {"name": "personal_channel_id", "tl_type": "flags2.6?long"},
        {"name": "personal_channel_message", "tl_type": "flags2.6?int"},
        {"name": "stargifts_count", "tl_type": "flags2.8?int"},
        {"name": "starref_program", "tl_type": "flags2.11?StarRefProgram"},
        {"name": "bot_verification", "tl_type": "flags2.12?BotVerification"},
        {"name": "send_paid_messages_stars", "tl_type": "flags2.14?long"},
        {"name": "disallowed_gifts", "tl_type": "flags2.15?DisallowedGiftsSettings"},
        {"name": "stars_rating", "tl_type": "flags2.17?StarsRating"},
        {"name": "stars_my_pending_rating", "tl_type": "flags2.18?StarsRating"},
        {"name": "stars_my_pending_rating_date", "tl_type": "flags2.18?int"},
        {"name": "main_tab", "tl_type": "flags2.20?ProfileTab"},
        {"name": "saved_music", "tl_type": "flags2.21?Document"},
        {"name": "note", "tl_type": "flags2.22?TextWithEntities"},
        {"name": "bot_manager_id", "tl_type": "flags2.25?long"},
    ],
    "userProfilePhoto": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "has_video", "tl_type": "true", "cond": 0},
        {"name": "personal", "tl_type": "true", "cond": 2},
        {"name": "photo_id", "tl_type": "long"},
        {"name": "stripped_thumb", "tl_type": "bytes", "cond": 1},
        {"name": "dc_id", "tl_type": "int"},
    ],
    "userStatusOnline": [
        {"name": "expires", "tl_type": "int"},
    ],
    "userStatusOffline": [
        {"name": "was_online", "tl_type": "int"},
    ],
    "userStatusRecently": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "by_me", "tl_type": "true", "cond": 0},
    ],
    "userStatusLastWeek": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "by_me", "tl_type": "true", "cond": 0},
    ],
    "userStatusLastMonth": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "by_me", "tl_type": "true", "cond": 0},
    ],
    "username": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "editable", "tl_type": "true", "cond": 0},
        {"name": "active", "tl_type": "true", "cond": 1},
        {"name": "username", "tl_type": "string"},
    ],
    "videoSize": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "type", "tl_type": "string"},
        {"name": "w", "tl_type": "int"},
        {"name": "h", "tl_type": "int"},
        {"name": "size", "tl_type": "int"},
        {"name": "video_start_ts", "tl_type": "double", "cond": 0},
    ],
    "videoSizeEmojiMarkup": [
        {"name": "emoji_id", "tl_type": "long"},
        {"name": "background_colors", "tl_type": "Vector"},
    ],
    "videoSizeStickerMarkup": [
        {"name": "stickerset", "tl_type": "InputStickerSet"},
        {"name": "sticker_id", "tl_type": "long"},
        {"name": "background_colors", "tl_type": "Vector"},
    ],
    "wallPaper": [
        {"name": "id", "tl_type": "long"},
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "creator", "tl_type": "true", "cond": 0},
        {"name": "default", "tl_type": "true", "cond": 1},
        {"name": "pattern", "tl_type": "true", "cond": 3},
        {"name": "dark", "tl_type": "true", "cond": 4},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "slug", "tl_type": "string"},
        {"name": "document", "tl_type": "Document"},
        {"name": "settings", "tl_type": "WallPaperSettings", "cond": 2},
    ],
    "wallPaperNoFile": [
        {"name": "id", "tl_type": "long"},
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "default", "tl_type": "true", "cond": 1},
        {"name": "dark", "tl_type": "true", "cond": 4},
        {"name": "settings", "tl_type": "WallPaperSettings", "cond": 2},
    ],
    "wallPaperSettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "blur", "tl_type": "true", "cond": 1},
        {"name": "motion", "tl_type": "true", "cond": 2},
        {"name": "background_color", "tl_type": "int", "cond": 0},
        {"name": "second_background_color", "tl_type": "int", "cond": 4},
        {"name": "third_background_color", "tl_type": "int", "cond": 5},
        {"name": "fourth_background_color", "tl_type": "int", "cond": 6},
        {"name": "intensity", "tl_type": "int", "cond": 3},
        {"name": "rotation", "tl_type": "int", "cond": 4},
        {"name": "emoticon", "tl_type": "string", "cond": 7},
    ],
    "webAuthorization": [
        {"name": "hash", "tl_type": "long"},
        {"name": "bot_id", "tl_type": "long"},
        {"name": "domain", "tl_type": "string"},
        {"name": "browser", "tl_type": "string"},
        {"name": "platform", "tl_type": "string"},
        {"name": "date_created", "tl_type": "int"},
        {"name": "date_active", "tl_type": "int"},
        {"name": "ip", "tl_type": "string"},
        {"name": "region", "tl_type": "string"},
    ],
    "webDocument": [
        {"name": "url", "tl_type": "string"},
        {"name": "access_hash", "tl_type": "long"},
        {"name": "size", "tl_type": "int"},
        {"name": "mime_type", "tl_type": "string"},
        {"name": "attributes", "tl_type": "Vector"},
    ],
    "webDocumentNoProxy": [
        {"name": "url", "tl_type": "string"},
        {"name": "size", "tl_type": "int"},
        {"name": "mime_type", "tl_type": "string"},
        {"name": "attributes", "tl_type": "Vector"},
    ],
    "webDomainException": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "domain", "tl_type": "string"},
        {"name": "url", "tl_type": "string"},
        {"name": "title", "tl_type": "string"},
        {"name": "favicon", "tl_type": "long", "cond": 0},
    ],
    "webPageEmpty": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "id", "tl_type": "long"},
        {"name": "url", "tl_type": "string", "cond": 0},
    ],
    "webPagePending": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "id", "tl_type": "long"},
        {"name": "url", "tl_type": "string", "cond": 0},
        {"name": "date", "tl_type": "int"},
    ],
    "webPage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "has_large_media", "tl_type": "true", "cond": 13},
        {"name": "video_cover_photo", "tl_type": "true", "cond": 14},
        {"name": "id", "tl_type": "long"},
        {"name": "url", "tl_type": "string"},
        {"name": "display_url", "tl_type": "string"},
        {"name": "hash", "tl_type": "int"},
        {"name": "type", "tl_type": "string", "cond": 0},
        {"name": "site_name", "tl_type": "string", "cond": 1},
        {"name": "title", "tl_type": "string", "cond": 2},
        {"name": "description", "tl_type": "string", "cond": 3},
        {"name": "photo", "tl_type": "Photo", "cond": 4},
        {"name": "embed_url", "tl_type": "string", "cond": 5},
        {"name": "embed_type", "tl_type": "string", "cond": 5},
        {"name": "embed_width", "tl_type": "int", "cond": 6},
        {"name": "embed_height", "tl_type": "int", "cond": 6},
        {"name": "duration", "tl_type": "int", "cond": 7},
        {"name": "author", "tl_type": "string", "cond": 8},
        {"name": "document", "tl_type": "Document", "cond": 9},
        {"name": "cached_page", "tl_type": "Page", "cond": 10},
        {"name": "attributes", "tl_type": "Vector", "cond": 12},
    ],
    "webPageNotModified": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "cached_page_views", "tl_type": "int", "cond": 0},
    ],
    "webPageAttributeTheme": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "documents", "tl_type": "Vector", "cond": 0},
        {"name": "settings", "tl_type": "ThemeSettings", "cond": 1},
    ],
    "webPageAttributeStory": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "Peer"},
        {"name": "id", "tl_type": "int"},
        {"name": "story", "tl_type": "StoryItem", "cond": 0},
    ],
    "webPageAttributeStickerSet": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "emojis", "tl_type": "true", "cond": 0},
        {"name": "text_color", "tl_type": "true", "cond": 1},
        {"name": "stickers", "tl_type": "Vector"},
    ],
    "webPageAttributeUniqueStarGift": [
        {"name": "gift", "tl_type": "StarGift"},
    ],
    "webPageAttributeStarGiftCollection": [
        {"name": "icons", "tl_type": "Vector"},
    ],
    "webPageAttributeStarGiftAuction": [
        {"name": "gift", "tl_type": "StarGift"},
        {"name": "end_date", "tl_type": "int"},
    ],
    "webPageAttributeAiComposeTone": [
        {"name": "emoji_id", "tl_type": "long"},
    ],
    "webViewMessageSent": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "msg_id", "tl_type": "InputBotInlineMessageID", "cond": 0},
    ],
    "webViewResultUrl": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "fullsize", "tl_type": "true", "cond": 1},
        {"name": "fullscreen", "tl_type": "true", "cond": 2},
        {"name": "same_origin", "tl_type": "true", "cond": 3},
        {"name": "query_id", "tl_type": "long", "cond": 0},
        {"name": "url", "tl_type": "string"},
    ],
    "invokeAfterMsgs": [
        {"name": "msg_ids", "tl_type": "Vector"},
        {"name": "query", "tl_type": "!X"},
    ],
    "initConnection": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "api_id", "tl_type": "int"},
        {"name": "device_model", "tl_type": "string"},
        {"name": "system_version", "tl_type": "string"},
        {"name": "app_version", "tl_type": "string"},
        {"name": "system_lang_code", "tl_type": "string"},
        {"name": "lang_pack", "tl_type": "string"},
        {"name": "lang_code", "tl_type": "string"},
        {"name": "proxy", "tl_type": "InputClientProxy", "cond": 0},
        {"name": "params", "tl_type": "JSONValue", "cond": 1},
        {"name": "query", "tl_type": "!X"},
    ],
    "invokeWithLayer": [
        {"name": "layer", "tl_type": "int"},
        {"name": "query", "tl_type": "!X"},
    ],
    "invokeWithoutUpdates": [
        {"name": "query", "tl_type": "!X"},
    ],
    "invokeWithMessagesRange": [
        {"name": "range", "tl_type": "MessageRange"},
        {"name": "query", "tl_type": "!X"},
    ],
    "invokeWithTakeout": [
        {"name": "takeout_id", "tl_type": "long"},
        {"name": "query", "tl_type": "!X"},
    ],
    "invokeWithBusinessConnection": [
        {"name": "connection_id", "tl_type": "string"},
        {"name": "query", "tl_type": "!X"},
    ],
    "invokeWithGooglePlayIntegrity": [
        {"name": "nonce", "tl_type": "string"},
        {"name": "token", "tl_type": "string"},
        {"name": "query", "tl_type": "!X"},
    ],
    "invokeWithApnsSecret": [
        {"name": "nonce", "tl_type": "string"},
        {"name": "secret", "tl_type": "string"},
        {"name": "query", "tl_type": "!X"},
    ],
    "invokeWithReCaptcha": [
        {"name": "token", "tl_type": "string"},
        {"name": "query", "tl_type": "!X"},
    ],
    "account.acceptAuthorization": [
        {"name": "bot_id", "tl_type": "long"},
        {"name": "scope", "tl_type": "string"},
        {"name": "public_key", "tl_type": "string"},
        {"name": "value_hashes", "tl_type": "Vector"},
        {"name": "credentials", "tl_type": "SecureCredentialsEncrypted"},
    ],
    "account.changeAuthorizationSettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "confirmed", "tl_type": "true", "cond": 3},
        {"name": "hash", "tl_type": "long"},
        {"name": "encrypted_requests_disabled", "tl_type": "Bool", "cond": 0},
        {"name": "call_requests_disabled", "tl_type": "Bool", "cond": 1},
    ],
    "account.changePhone": [
        {"name": "phone_number", "tl_type": "string"},
        {"name": "phone_code_hash", "tl_type": "string"},
        {"name": "phone_code", "tl_type": "string"},
    ],
    "account.checkUsername": [
        {"name": "username", "tl_type": "string"},
    ],
    "account.confirmBotConnection": [
        {"name": "bot_id", "tl_type": "InputUser"},
    ],
    "account.confirmPasswordEmail": [
        {"name": "code", "tl_type": "string"},
    ],
    "account.confirmPhone": [
        {"name": "phone_code_hash", "tl_type": "string"},
        {"name": "phone_code", "tl_type": "string"},
    ],
    "account.createBusinessChatLink": [
        {"name": "link", "tl_type": "InputBusinessChatLink"},
    ],
    "account.createTheme": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "slug", "tl_type": "string"},
        {"name": "title", "tl_type": "string"},
        {"name": "document", "tl_type": "InputDocument", "cond": 2},
        {"name": "settings", "tl_type": "Vector", "cond": 3},
    ],
    "account.deleteAccount": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "reason", "tl_type": "string"},
        {"name": "password", "tl_type": "InputCheckPasswordSRP", "cond": 0},
    ],
    "account.deleteBusinessChatLink": [
        {"name": "slug", "tl_type": "string"},
    ],
    "account.deletePasskey": [
        {"name": "id", "tl_type": "string"},
    ],
    "account.deleteSecureValue": [
        {"name": "types", "tl_type": "Vector"},
    ],
    "account.disablePeerConnectedBot": [
        {"name": "peer", "tl_type": "InputPeer"},
    ],
    "account.editBusinessChatLink": [
        {"name": "slug", "tl_type": "string"},
        {"name": "link", "tl_type": "InputBusinessChatLink"},
    ],
    "account.finishTakeoutSession": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "success", "tl_type": "true", "cond": 0},
    ],
    "account.getBotBusinessConnection": [
        {"name": "connection_id", "tl_type": "string"},
    ],
    "account.getChannelRestrictedStatusEmojis": [
        {"name": "hash", "tl_type": "long"},
    ],
    "account.getDefaultBackgroundEmojis": [
        {"name": "hash", "tl_type": "long"},
    ],
    "account.getDefaultGroupPhotoEmojis": [
        {"name": "hash", "tl_type": "long"},
    ],
    "account.getDefaultProfilePhotoEmojis": [
        {"name": "hash", "tl_type": "long"},
    ],
    "account.getNotifyExceptions": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "compare_sound", "tl_type": "true", "cond": 1},
        {"name": "compare_stories", "tl_type": "true", "cond": 2},
        {"name": "peer", "tl_type": "InputNotifyPeer", "cond": 0},
    ],
    "account.getNotifySettings": [
        {"name": "peer", "tl_type": "InputNotifyPeer"},
    ],
    "account.getTheme": [
        {"name": "format", "tl_type": "string"},
        {"name": "theme", "tl_type": "InputTheme"},
    ],
    "account.getWallPaper": [
        {"name": "wallpaper", "tl_type": "InputWallPaper"},
    ],
    "account.installTheme": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "dark", "tl_type": "true", "cond": 0},
        {"name": "theme", "tl_type": "InputTheme", "cond": 1},
        {"name": "format", "tl_type": "string", "cond": 2},
        {"name": "base_theme", "tl_type": "BaseTheme", "cond": 3},
    ],
    "account.installWallPaper": [
        {"name": "wallpaper", "tl_type": "InputWallPaper"},
        {"name": "settings", "tl_type": "WallPaperSettings"},
    ],
    "account.invalidateSignInCodes": [
        {"name": "codes", "tl_type": "Vector"},
    ],
    "account.registerDevice": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "no_muted", "tl_type": "true", "cond": 0},
        {"name": "token_type", "tl_type": "int"},
        {"name": "token", "tl_type": "string"},
        {"name": "app_sandbox", "tl_type": "Bool"},
        {"name": "secret", "tl_type": "bytes"},
        {"name": "other_uids", "tl_type": "Vector"},
    ],
    "account.registerPasskey": [
        {"name": "credential", "tl_type": "InputPasskeyCredential"},
    ],
    "account.reorderUsernames": [
        {"name": "order", "tl_type": "Vector"},
    ],
    "account.reportPeer": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "reason", "tl_type": "ReportReason"},
        {"name": "message", "tl_type": "string"},
    ],
    "account.reportProfilePhoto": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "photo_id", "tl_type": "InputPhoto"},
        {"name": "reason", "tl_type": "ReportReason"},
        {"name": "message", "tl_type": "string"},
    ],
    "account.resetAuthorization": [
        {"name": "hash", "tl_type": "long"},
    ],
    "account.resetWebAuthorization": [
        {"name": "hash", "tl_type": "long"},
    ],
    "account.saveAutoDownloadSettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "low", "tl_type": "true", "cond": 0},
        {"name": "high", "tl_type": "true", "cond": 1},
        {"name": "settings", "tl_type": "AutoDownloadSettings"},
    ],
    "account.saveAutoSaveSettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "users", "tl_type": "true", "cond": 0},
        {"name": "chats", "tl_type": "true", "cond": 1},
        {"name": "broadcasts", "tl_type": "true", "cond": 2},
        {"name": "peer", "tl_type": "InputPeer", "cond": 3},
        {"name": "settings", "tl_type": "AutoSaveSettings"},
    ],
    "account.saveMusic": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "unsave", "tl_type": "true", "cond": 0},
        {"name": "id", "tl_type": "InputDocument"},
        {"name": "after_id", "tl_type": "InputDocument", "cond": 1},
    ],
    "account.saveSecureValue": [
        {"name": "value", "tl_type": "InputSecureValue"},
        {"name": "secure_secret_id", "tl_type": "long"},
    ],
    "account.saveTheme": [
        {"name": "theme", "tl_type": "InputTheme"},
        {"name": "unsave", "tl_type": "Bool"},
    ],
    "account.saveWallPaper": [
        {"name": "wallpaper", "tl_type": "InputWallPaper"},
        {"name": "unsave", "tl_type": "Bool"},
        {"name": "settings", "tl_type": "WallPaperSettings"},
    ],
    "account.setAccountTTL": [
        {"name": "ttl", "tl_type": "AccountDaysTTL"},
    ],
    "account.setAuthorizationTTL": [
        {"name": "authorization_ttl_days", "tl_type": "int"},
    ],
    "account.setContactSignUpNotification": [
        {"name": "silent", "tl_type": "Bool"},
    ],
    "account.setContentSettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "sensitive_enabled", "tl_type": "true", "cond": 0},
    ],
    "account.setGlobalPrivacySettings": [
        {"name": "settings", "tl_type": "GlobalPrivacySettings"},
    ],
    "account.setMainProfileTab": [
        {"name": "tab", "tl_type": "ProfileTab"},
    ],
    "account.setReactionsNotifySettings": [
        {"name": "settings", "tl_type": "ReactionsNotifySettings"},
    ],
    "account.toggleConnectedBotPaused": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "paused", "tl_type": "Bool"},
    ],
    "account.toggleNoPaidMessagesException": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "refund_charged", "tl_type": "true", "cond": 0},
        {"name": "require_payment", "tl_type": "true", "cond": 2},
        {"name": "parent_peer", "tl_type": "InputPeer", "cond": 1},
        {"name": "user_id", "tl_type": "InputUser"},
    ],
    "account.toggleSponsoredMessages": [
        {"name": "enabled", "tl_type": "Bool"},
    ],
    "account.toggleUsername": [
        {"name": "username", "tl_type": "string"},
        {"name": "active", "tl_type": "Bool"},
    ],
    "account.toggleWebBrowserSettingsException": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "delete", "tl_type": "true", "cond": 1},
        {"name": "open_external_browser", "tl_type": "Bool", "cond": 0},
        {"name": "url", "tl_type": "string"},
    ],
    "account.unregisterDevice": [
        {"name": "token_type", "tl_type": "int"},
        {"name": "token", "tl_type": "string"},
        {"name": "other_uids", "tl_type": "Vector"},
    ],
    "account.updateBirthday": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "birthday", "tl_type": "Birthday", "cond": 0},
    ],
    "account.updateBusinessAwayMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "message", "tl_type": "InputBusinessAwayMessage", "cond": 0},
    ],
    "account.updateBusinessGreetingMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "message", "tl_type": "InputBusinessGreetingMessage", "cond": 0},
    ],
    "account.updateBusinessIntro": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "intro", "tl_type": "InputBusinessIntro", "cond": 0},
    ],
    "account.updateBusinessLocation": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "geo_point", "tl_type": "InputGeoPoint", "cond": 1},
        {"name": "address", "tl_type": "string", "cond": 0},
    ],
    "account.updateBusinessWorkHours": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "business_work_hours", "tl_type": "BusinessWorkHours", "cond": 0},
    ],
    "account.updateColor": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "for_profile", "tl_type": "true", "cond": 1},
        {"name": "color", "tl_type": "PeerColor", "cond": 2},
    ],
    "account.updateConnectedBot": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "deleted", "tl_type": "true", "cond": 1},
        {"name": "rights", "tl_type": "BusinessBotRights", "cond": 0},
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "recipients", "tl_type": "InputBusinessBotRecipients"},
    ],
    "account.updateDeviceLocked": [
        {"name": "period", "tl_type": "int"},
    ],
    "account.updateEmojiStatus": [
        {"name": "emoji_status", "tl_type": "EmojiStatus"},
    ],
    "account.updateNotifySettings": [
        {"name": "peer", "tl_type": "InputNotifyPeer"},
        {"name": "settings", "tl_type": "InputPeerNotifySettings"},
    ],
    "account.updatePasswordSettings": [
        {"name": "password", "tl_type": "InputCheckPasswordSRP"},
        {"name": "new_settings", "tl_type": "account.PasswordInputSettings"},
    ],
    "account.updatePersonalChannel": [
        {"name": "channel", "tl_type": "InputChannel"},
    ],
    "account.updateProfile": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "first_name", "tl_type": "string", "cond": 0},
        {"name": "last_name", "tl_type": "string", "cond": 1},
        {"name": "about", "tl_type": "string", "cond": 2},
    ],
    "account.updateStatus": [
        {"name": "offline", "tl_type": "Bool"},
    ],
    "account.updateTheme": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "format", "tl_type": "string"},
        {"name": "theme", "tl_type": "InputTheme"},
        {"name": "slug", "tl_type": "string", "cond": 0},
        {"name": "title", "tl_type": "string", "cond": 1},
        {"name": "document", "tl_type": "InputDocument", "cond": 2},
        {"name": "settings", "tl_type": "Vector", "cond": 3},
    ],
    "account.updateUsername": [
        {"name": "username", "tl_type": "string"},
    ],
    "account.uploadRingtone": [
        {"name": "file", "tl_type": "InputFile"},
        {"name": "file_name", "tl_type": "string"},
        {"name": "mime_type", "tl_type": "string"},
    ],
    "account.uploadTheme": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "file", "tl_type": "InputFile"},
        {"name": "thumb", "tl_type": "InputFile", "cond": 0},
        {"name": "file_name", "tl_type": "string"},
        {"name": "mime_type", "tl_type": "string"},
    ],
    "account.uploadWallPaper": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "for_chat", "tl_type": "true", "cond": 0},
        {"name": "file", "tl_type": "InputFile"},
        {"name": "mime_type", "tl_type": "string"},
        {"name": "settings", "tl_type": "WallPaperSettings"},
    ],
    "account.verifyPhone": [
        {"name": "phone_number", "tl_type": "string"},
        {"name": "phone_code_hash", "tl_type": "string"},
        {"name": "phone_code", "tl_type": "string"},
    ],
    "aicompose.createTone": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "display_author", "tl_type": "true", "cond": 0},
        {"name": "emoji_id", "tl_type": "long"},
        {"name": "title", "tl_type": "string"},
        {"name": "prompt", "tl_type": "string"},
    ],
    "aicompose.deleteTone": [
        {"name": "tone", "tl_type": "InputAiComposeTone"},
    ],
    "aicompose.getToneExample": [
        {"name": "tone", "tl_type": "InputAiComposeTone"},
        {"name": "num", "tl_type": "int"},
    ],
    "aicompose.saveTone": [
        {"name": "tone", "tl_type": "InputAiComposeTone"},
        {"name": "unsave", "tl_type": "Bool"},
    ],
    "aicompose.updateTone": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "tone", "tl_type": "InputAiComposeTone"},
        {"name": "display_author", "tl_type": "Bool", "cond": 0},
        {"name": "emoji_id", "tl_type": "long", "cond": 1},
        {"name": "title", "tl_type": "string", "cond": 2},
        {"name": "prompt", "tl_type": "string", "cond": 3},
    ],
    "auth.acceptLoginToken": [
        {"name": "token", "tl_type": "bytes"},
    ],
    "auth.bindTempAuthKey": [
        {"name": "perm_auth_key_id", "tl_type": "long"},
        {"name": "nonce", "tl_type": "long"},
        {"name": "expires_at", "tl_type": "int"},
        {"name": "encrypted_message", "tl_type": "bytes"},
    ],
    "auth.cancelCode": [
        {"name": "phone_number", "tl_type": "string"},
        {"name": "phone_code_hash", "tl_type": "string"},
    ],
    "auth.checkRecoveryPassword": [
        {"name": "code", "tl_type": "string"},
    ],
    "auth.dropTempAuthKeys": [
        {"name": "except_auth_keys", "tl_type": "Vector"},
    ],
    "auth.reportMissingCode": [
        {"name": "phone_number", "tl_type": "string"},
        {"name": "phone_code_hash", "tl_type": "string"},
        {"name": "mnc", "tl_type": "string"},
    ],
    "auth.requestFirebaseSms": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "phone_number", "tl_type": "string"},
        {"name": "phone_code_hash", "tl_type": "string"},
        {"name": "safety_net_token", "tl_type": "string", "cond": 0},
        {"name": "play_integrity_token", "tl_type": "string", "cond": 2},
        {"name": "ios_push_secret", "tl_type": "string", "cond": 1},
    ],
    "bots.addPreviewMedia": [
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "lang_code", "tl_type": "string"},
        {"name": "media", "tl_type": "InputMedia"},
    ],
    "bots.allowSendMessage": [
        {"name": "bot", "tl_type": "InputUser"},
    ],
    "bots.answerWebhookJSONQuery": [
        {"name": "query_id", "tl_type": "long"},
        {"name": "data", "tl_type": "DataJSON"},
    ],
    "bots.canSendMessage": [
        {"name": "bot", "tl_type": "InputUser"},
    ],
    "bots.checkDownloadFileParams": [
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "file_name", "tl_type": "string"},
        {"name": "url", "tl_type": "string"},
    ],
    "bots.checkUsername": [
        {"name": "username", "tl_type": "string"},
    ],
    "bots.createBot": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "via_deeplink", "tl_type": "true", "cond": 0},
        {"name": "name", "tl_type": "string"},
        {"name": "username", "tl_type": "string"},
        {"name": "manager_id", "tl_type": "InputUser"},
    ],
    "bots.deletePreviewMedia": [
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "lang_code", "tl_type": "string"},
        {"name": "media", "tl_type": "Vector"},
    ],
    "bots.editAccessSettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "restricted", "tl_type": "true", "cond": 0},
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "add_users", "tl_type": "Vector", "cond": 1},
    ],
    "bots.editPreviewMedia": [
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "lang_code", "tl_type": "string"},
        {"name": "media", "tl_type": "InputMedia"},
        {"name": "new_media", "tl_type": "InputMedia"},
    ],
    "bots.getBotMenuButton": [
        {"name": "user_id", "tl_type": "InputUser"},
    ],
    "bots.getRequestedWebViewButton": [
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "webapp_req_id", "tl_type": "string"},
    ],
    "bots.invokeWebViewCustomMethod": [
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "custom_method", "tl_type": "string"},
        {"name": "params", "tl_type": "DataJSON"},
    ],
    "bots.reorderPreviewMedias": [
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "lang_code", "tl_type": "string"},
        {"name": "order", "tl_type": "Vector"},
    ],
    "bots.reorderUsernames": [
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "order", "tl_type": "Vector"},
    ],
    "bots.resetBotCommands": [
        {"name": "scope", "tl_type": "BotCommandScope"},
        {"name": "lang_code", "tl_type": "string"},
    ],
    "bots.sendCustomRequest": [
        {"name": "custom_method", "tl_type": "string"},
        {"name": "params", "tl_type": "DataJSON"},
    ],
    "bots.setBotBroadcastDefaultAdminRights": [
        {"name": "admin_rights", "tl_type": "ChatAdminRights"},
    ],
    "bots.setBotCommands": [
        {"name": "scope", "tl_type": "BotCommandScope"},
        {"name": "lang_code", "tl_type": "string"},
        {"name": "commands", "tl_type": "Vector"},
    ],
    "bots.setBotGroupDefaultAdminRights": [
        {"name": "admin_rights", "tl_type": "ChatAdminRights"},
    ],
    "bots.setBotInfo": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "bot", "tl_type": "InputUser", "cond": 2},
        {"name": "lang_code", "tl_type": "string"},
        {"name": "name", "tl_type": "string", "cond": 3},
        {"name": "about", "tl_type": "string", "cond": 0},
        {"name": "description", "tl_type": "string", "cond": 1},
    ],
    "bots.setBotMenuButton": [
        {"name": "user_id", "tl_type": "InputUser"},
        {"name": "button", "tl_type": "BotMenuButton"},
    ],
    "bots.setCustomVerification": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "enabled", "tl_type": "true", "cond": 1},
        {"name": "bot", "tl_type": "InputUser", "cond": 0},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "custom_description", "tl_type": "string", "cond": 2},
    ],
    "bots.setJoinChatResults": [
        {"name": "query_id", "tl_type": "long"},
        {"name": "result", "tl_type": "JoinChatBotResult"},
    ],
    "bots.toggleUserEmojiStatusPermission": [
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "enabled", "tl_type": "Bool"},
    ],
    "bots.toggleUsername": [
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "username", "tl_type": "string"},
        {"name": "active", "tl_type": "Bool"},
    ],
    "bots.updateStarRefProgram": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "commission_permille", "tl_type": "int"},
        {"name": "duration_months", "tl_type": "int", "cond": 0},
    ],
    "bots.updateUserEmojiStatus": [
        {"name": "user_id", "tl_type": "InputUser"},
        {"name": "emoji_status", "tl_type": "EmojiStatus"},
    ],
    "channels.checkSearchPostsFlood": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "query", "tl_type": "string", "cond": 0},
    ],
    "channels.checkUsername": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "username", "tl_type": "string"},
    ],
    "channels.convertToGigagroup": [
        {"name": "channel", "tl_type": "InputChannel"},
    ],
    "channels.createChannel": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "broadcast", "tl_type": "true", "cond": 0},
        {"name": "megagroup", "tl_type": "true", "cond": 1},
        {"name": "for_import", "tl_type": "true", "cond": 3},
        {"name": "forum", "tl_type": "true", "cond": 5},
        {"name": "title", "tl_type": "string"},
        {"name": "about", "tl_type": "string"},
        {"name": "geo_point", "tl_type": "InputGeoPoint", "cond": 2},
        {"name": "address", "tl_type": "string", "cond": 2},
        {"name": "ttl_period", "tl_type": "int", "cond": 4},
    ],
    "channels.deactivateAllUsernames": [
        {"name": "channel", "tl_type": "InputChannel"},
    ],
    "channels.deleteChannel": [
        {"name": "channel", "tl_type": "InputChannel"},
    ],
    "channels.deleteHistory": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "for_everyone", "tl_type": "true", "cond": 0},
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "max_id", "tl_type": "int"},
    ],
    "channels.editAdmin": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "user_id", "tl_type": "InputUser"},
        {"name": "admin_rights", "tl_type": "ChatAdminRights"},
        {"name": "rank", "tl_type": "string", "cond": 0},
    ],
    "channels.editBanned": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "participant", "tl_type": "InputPeer"},
        {"name": "banned_rights", "tl_type": "ChatBannedRights"},
    ],
    "channels.editLocation": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "geo_point", "tl_type": "InputGeoPoint"},
        {"name": "address", "tl_type": "string"},
    ],
    "channels.editPhoto": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "photo", "tl_type": "InputChatPhoto"},
    ],
    "channels.editTitle": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "title", "tl_type": "string"},
    ],
    "channels.exportMessageLink": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "grouped", "tl_type": "true", "cond": 0},
        {"name": "thread", "tl_type": "true", "cond": 1},
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "id", "tl_type": "int"},
    ],
    "channels.getMessageAuthor": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "id", "tl_type": "int"},
    ],
    "channels.leaveChannel": [
        {"name": "channel", "tl_type": "InputChannel"},
    ],
    "channels.readHistory": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "max_id", "tl_type": "int"},
    ],
    "channels.readMessageContents": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "id", "tl_type": "Vector"},
    ],
    "channels.reorderUsernames": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "order", "tl_type": "Vector"},
    ],
    "channels.reportAntiSpamFalsePositive": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "msg_id", "tl_type": "int"},
    ],
    "channels.reportSpam": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "participant", "tl_type": "InputPeer"},
        {"name": "id", "tl_type": "Vector"},
    ],
    "channels.restrictSponsoredMessages": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "restricted", "tl_type": "Bool"},
    ],
    "channels.setBoostsToUnblockRestrictions": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "boosts", "tl_type": "int"},
    ],
    "channels.setDiscussionGroup": [
        {"name": "broadcast", "tl_type": "InputChannel"},
        {"name": "group", "tl_type": "InputChannel"},
    ],
    "channels.setEmojiStickers": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "stickerset", "tl_type": "InputStickerSet"},
    ],
    "channels.setMainProfileTab": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "tab", "tl_type": "ProfileTab"},
    ],
    "channels.setStickers": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "stickerset", "tl_type": "InputStickerSet"},
    ],
    "channels.toggleAntiSpam": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "enabled", "tl_type": "Bool"},
    ],
    "channels.toggleAutotranslation": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "enabled", "tl_type": "Bool"},
    ],
    "channels.toggleForum": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "enabled", "tl_type": "Bool"},
        {"name": "tabs", "tl_type": "Bool"},
    ],
    "channels.toggleJoinRequest": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "apply_to_invites", "tl_type": "true", "cond": 1},
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "enabled", "tl_type": "Bool"},
        {"name": "guard_bot", "tl_type": "InputUser", "cond": 0},
    ],
    "channels.toggleJoinToSend": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "enabled", "tl_type": "Bool"},
    ],
    "channels.toggleParticipantsHidden": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "enabled", "tl_type": "Bool"},
    ],
    "channels.togglePreHistoryHidden": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "enabled", "tl_type": "Bool"},
    ],
    "channels.toggleSignatures": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "signatures_enabled", "tl_type": "true", "cond": 0},
        {"name": "profiles_enabled", "tl_type": "true", "cond": 1},
        {"name": "channel", "tl_type": "InputChannel"},
    ],
    "channels.toggleSlowMode": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "seconds", "tl_type": "int"},
    ],
    "channels.toggleUsername": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "username", "tl_type": "string"},
        {"name": "active", "tl_type": "Bool"},
    ],
    "channels.toggleViewForumAsMessages": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "enabled", "tl_type": "Bool"},
    ],
    "channels.updateColor": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "for_profile", "tl_type": "true", "cond": 1},
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "color", "tl_type": "int", "cond": 2},
        {"name": "background_emoji_id", "tl_type": "long", "cond": 0},
    ],
    "channels.updateEmojiStatus": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "emoji_status", "tl_type": "EmojiStatus"},
    ],
    "channels.updatePaidMessagesPrice": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "broadcast_messages_allowed", "tl_type": "true", "cond": 0},
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "send_paid_messages_stars", "tl_type": "long"},
    ],
    "channels.updateUsername": [
        {"name": "channel", "tl_type": "InputChannel"},
        {"name": "username", "tl_type": "string"},
    ],
    "chatlists.deleteExportedInvite": [
        {"name": "chatlist", "tl_type": "InputChatlist"},
        {"name": "slug", "tl_type": "string"},
    ],
    "chatlists.editExportedInvite": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "chatlist", "tl_type": "InputChatlist"},
        {"name": "slug", "tl_type": "string"},
        {"name": "title", "tl_type": "string", "cond": 1},
        {"name": "peers", "tl_type": "Vector", "cond": 2},
    ],
    "chatlists.hideChatlistUpdates": [
        {"name": "chatlist", "tl_type": "InputChatlist"},
    ],
    "chatlists.joinChatlistInvite": [
        {"name": "slug", "tl_type": "string"},
        {"name": "peers", "tl_type": "Vector"},
    ],
    "chatlists.joinChatlistUpdates": [
        {"name": "chatlist", "tl_type": "InputChatlist"},
        {"name": "peers", "tl_type": "Vector"},
    ],
    "chatlists.leaveChatlist": [
        {"name": "chatlist", "tl_type": "InputChatlist"},
        {"name": "peers", "tl_type": "Vector"},
    ],
    "contacts.acceptContact": [
        {"name": "id", "tl_type": "InputUser"},
    ],
    "contacts.addContact": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "add_phone_privacy_exception", "tl_type": "true", "cond": 0},
        {"name": "id", "tl_type": "InputUser"},
        {"name": "first_name", "tl_type": "string"},
        {"name": "last_name", "tl_type": "string"},
        {"name": "phone", "tl_type": "string"},
        {"name": "note", "tl_type": "TextWithEntities", "cond": 1},
    ],
    "contacts.block": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "my_stories_from", "tl_type": "true", "cond": 0},
        {"name": "id", "tl_type": "InputPeer"},
    ],
    "contacts.blockFromReplies": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "delete_message", "tl_type": "true", "cond": 0},
        {"name": "delete_history", "tl_type": "true", "cond": 1},
        {"name": "report_spam", "tl_type": "true", "cond": 2},
        {"name": "msg_id", "tl_type": "int"},
    ],
    "contacts.deleteByPhones": [
        {"name": "phones", "tl_type": "Vector"},
    ],
    "contacts.deleteContacts": [
        {"name": "id", "tl_type": "Vector"},
    ],
    "contacts.editCloseFriends": [
        {"name": "id", "tl_type": "Vector"},
    ],
    "contacts.getLocated": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "background", "tl_type": "true", "cond": 1},
        {"name": "geo_point", "tl_type": "InputGeoPoint"},
        {"name": "self_expires", "tl_type": "int", "cond": 0},
    ],
    "contacts.importContactToken": [
        {"name": "token", "tl_type": "string"},
    ],
    "contacts.resetTopPeerRating": [
        {"name": "category", "tl_type": "TopPeerCategory"},
        {"name": "peer", "tl_type": "InputPeer"},
    ],
    "contacts.setBlocked": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "my_stories_from", "tl_type": "true", "cond": 0},
        {"name": "id", "tl_type": "Vector"},
        {"name": "limit", "tl_type": "int"},
    ],
    "contacts.toggleTopPeers": [
        {"name": "enabled", "tl_type": "Bool"},
    ],
    "contacts.unblock": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "my_stories_from", "tl_type": "true", "cond": 0},
        {"name": "id", "tl_type": "InputPeer"},
    ],
    "contacts.updateContactNote": [
        {"name": "id", "tl_type": "InputUser"},
        {"name": "note", "tl_type": "TextWithEntities"},
    ],
    "folders.editPeerFolders": [
        {"name": "folder_peers", "tl_type": "Vector"},
    ],
    "help.acceptTermsOfService": [
        {"name": "id", "tl_type": "DataJSON"},
    ],
    "help.dismissSuggestion": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "suggestion", "tl_type": "string"},
    ],
    "help.hidePromoData": [
        {"name": "peer", "tl_type": "InputPeer"},
    ],
    "help.saveAppLog": [
        {"name": "events", "tl_type": "Vector"},
    ],
    "help.setBotUpdatesStatus": [
        {"name": "pending_updates_count", "tl_type": "int"},
        {"name": "message", "tl_type": "string"},
    ],
    "langpack.getDifference": [
        {"name": "lang_pack", "tl_type": "string"},
        {"name": "lang_code", "tl_type": "string"},
        {"name": "from_version", "tl_type": "int"},
    ],
    "langpack.getLangPack": [
        {"name": "lang_pack", "tl_type": "string"},
        {"name": "lang_code", "tl_type": "string"},
    ],
    "langpack.getLanguage": [
        {"name": "lang_pack", "tl_type": "string"},
        {"name": "lang_code", "tl_type": "string"},
    ],
    "messages.acceptEncryption": [
        {"name": "peer", "tl_type": "InputEncryptedChat"},
        {"name": "g_b", "tl_type": "bytes"},
        {"name": "key_fingerprint", "tl_type": "long"},
    ],
    "messages.acceptUrlAuth": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "write_allowed", "tl_type": "true", "cond": 0},
        {"name": "share_phone_number", "tl_type": "true", "cond": 3},
        {"name": "peer", "tl_type": "InputPeer", "cond": 1},
        {"name": "msg_id", "tl_type": "int", "cond": 1},
        {"name": "button_id", "tl_type": "int", "cond": 1},
        {"name": "url", "tl_type": "string", "cond": 2},
        {"name": "match_code", "tl_type": "string", "cond": 4},
    ],
    "messages.addPollAnswer": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "answer", "tl_type": "PollAnswer"},
    ],
    "messages.appendTodoList": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "list", "tl_type": "Vector"},
    ],
    "messages.checkChatInvite": [
        {"name": "hash", "tl_type": "string"},
    ],
    "messages.checkQuickReplyShortcut": [
        {"name": "shortcut", "tl_type": "string"},
    ],
    "messages.checkUrlAuthMatchCode": [
        {"name": "url", "tl_type": "string"},
        {"name": "match_code", "tl_type": "string"},
    ],
    "messages.clearRecentStickers": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "attached", "tl_type": "true", "cond": 0},
    ],
    "messages.clickSponsoredMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "media", "tl_type": "true", "cond": 0},
        {"name": "fullscreen", "tl_type": "true", "cond": 1},
        {"name": "random_id", "tl_type": "bytes"},
    ],
    "messages.createForumTopic": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "title_missing", "tl_type": "true", "cond": 4},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "title", "tl_type": "string"},
        {"name": "icon_color", "tl_type": "int", "cond": 0},
        {"name": "icon_emoji_id", "tl_type": "long", "cond": 3},
        {"name": "random_id", "tl_type": "long"},
        {"name": "send_as", "tl_type": "InputPeer", "cond": 2},
    ],
    "messages.declineUrlAuth": [
        {"name": "url", "tl_type": "string"},
    ],
    "messages.deleteChat": [
        {"name": "chat_id", "tl_type": "long"},
    ],
    "messages.deleteChatUser": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "revoke_history", "tl_type": "true", "cond": 0},
        {"name": "chat_id", "tl_type": "long"},
        {"name": "user_id", "tl_type": "InputUser"},
    ],
    "messages.deleteExportedChatInvite": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "link", "tl_type": "string"},
    ],
    "messages.deleteFactCheck": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
    ],
    "messages.deleteParticipantReaction": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "participant", "tl_type": "InputPeer"},
    ],
    "messages.deleteParticipantReactions": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "participant", "tl_type": "InputPeer"},
    ],
    "messages.deletePollAnswer": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "option", "tl_type": "bytes"},
    ],
    "messages.deleteQuickReplyMessages": [
        {"name": "shortcut_id", "tl_type": "int"},
        {"name": "id", "tl_type": "Vector"},
    ],
    "messages.deleteQuickReplyShortcut": [
        {"name": "shortcut_id", "tl_type": "int"},
    ],
    "messages.deleteRevokedExportedChatInvites": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "admin_id", "tl_type": "InputUser"},
    ],
    "messages.deleteScheduledMessages": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "id", "tl_type": "Vector"},
    ],
    "messages.discardEncryption": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "delete_history", "tl_type": "true", "cond": 0},
        {"name": "chat_id", "tl_type": "int"},
    ],
    "messages.editChatAbout": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "about", "tl_type": "string"},
    ],
    "messages.editChatAdmin": [
        {"name": "chat_id", "tl_type": "long"},
        {"name": "user_id", "tl_type": "InputUser"},
        {"name": "is_admin", "tl_type": "Bool"},
    ],
    "messages.editChatCreator": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "user_id", "tl_type": "InputUser"},
        {"name": "password", "tl_type": "InputCheckPasswordSRP"},
    ],
    "messages.editChatDefaultBannedRights": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "banned_rights", "tl_type": "ChatBannedRights"},
    ],
    "messages.editChatParticipantRank": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "participant", "tl_type": "InputPeer"},
        {"name": "rank", "tl_type": "string"},
    ],
    "messages.editChatPhoto": [
        {"name": "chat_id", "tl_type": "long"},
        {"name": "photo", "tl_type": "InputChatPhoto"},
    ],
    "messages.editChatTitle": [
        {"name": "chat_id", "tl_type": "long"},
        {"name": "title", "tl_type": "string"},
    ],
    "messages.editFactCheck": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "text", "tl_type": "TextWithEntities"},
    ],
    "messages.editForumTopic": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "topic_id", "tl_type": "int"},
        {"name": "title", "tl_type": "string", "cond": 0},
        {"name": "icon_emoji_id", "tl_type": "long", "cond": 1},
        {"name": "closed", "tl_type": "Bool", "cond": 2},
        {"name": "hidden", "tl_type": "Bool", "cond": 3},
    ],
    "messages.editInlineBotMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "no_webpage", "tl_type": "true", "cond": 1},
        {"name": "invert_media", "tl_type": "true", "cond": 16},
        {"name": "id", "tl_type": "InputBotInlineMessageID"},
        {"name": "message", "tl_type": "string", "cond": 11},
        {"name": "media", "tl_type": "InputMedia", "cond": 14},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
        {"name": "entities", "tl_type": "Vector", "cond": 3},
        {"name": "rich_message", "tl_type": "InputRichMessage", "cond": 23},
    ],
    "messages.editMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "no_webpage", "tl_type": "true", "cond": 1},
        {"name": "invert_media", "tl_type": "true", "cond": 16},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "id", "tl_type": "int"},
        {"name": "message", "tl_type": "string", "cond": 11},
        {"name": "media", "tl_type": "InputMedia", "cond": 14},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
        {"name": "entities", "tl_type": "Vector", "cond": 3},
        {"name": "schedule_date", "tl_type": "int", "cond": 15},
        {"name": "schedule_repeat_period", "tl_type": "int", "cond": 18},
        {"name": "quick_reply_shortcut_id", "tl_type": "int", "cond": 17},
        {"name": "rich_message", "tl_type": "InputRichMessage", "cond": 23},
    ],
    "messages.editQuickReplyShortcut": [
        {"name": "shortcut_id", "tl_type": "int"},
        {"name": "shortcut", "tl_type": "string"},
    ],
    "messages.exportChatInvite": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "legacy_revoke_permanent", "tl_type": "true", "cond": 2},
        {"name": "request_needed", "tl_type": "true", "cond": 3},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "expire_date", "tl_type": "int", "cond": 0},
        {"name": "usage_limit", "tl_type": "int", "cond": 1},
        {"name": "title", "tl_type": "string", "cond": 4},
        {"name": "subscription_pricing", "tl_type": "StarsSubscriptionPricing", "cond": 5},
    ],
    "messages.faveSticker": [
        {"name": "id", "tl_type": "InputDocument"},
        {"name": "unfave", "tl_type": "Bool"},
    ],
    "messages.forwardMessages": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "silent", "tl_type": "true", "cond": 5},
        {"name": "background", "tl_type": "true", "cond": 6},
        {"name": "with_my_score", "tl_type": "true", "cond": 8},
        {"name": "drop_author", "tl_type": "true", "cond": 11},
        {"name": "drop_media_captions", "tl_type": "true", "cond": 12},
        {"name": "noforwards", "tl_type": "true", "cond": 14},
        {"name": "allow_paid_floodskip", "tl_type": "true", "cond": 19},
        {"name": "from_peer", "tl_type": "InputPeer"},
        {"name": "id", "tl_type": "Vector"},
        {"name": "random_id", "tl_type": "Vector"},
        {"name": "to_peer", "tl_type": "InputPeer"},
        {"name": "top_msg_id", "tl_type": "int", "cond": 9},
        {"name": "reply_to", "tl_type": "InputReplyTo", "cond": 22},
        {"name": "schedule_date", "tl_type": "int", "cond": 10},
        {"name": "schedule_repeat_period", "tl_type": "int", "cond": 24},
        {"name": "send_as", "tl_type": "InputPeer", "cond": 13},
        {"name": "quick_reply_shortcut", "tl_type": "InputQuickReplyShortcut", "cond": 17},
        {"name": "effect", "tl_type": "long", "cond": 18},
        {"name": "video_timestamp", "tl_type": "int", "cond": 20},
        {"name": "allow_paid_stars", "tl_type": "long", "cond": 21},
        {"name": "suggested_post", "tl_type": "SuggestedPost", "cond": 23},
    ],
    "messages.getAttachMenuBot": [
        {"name": "bot", "tl_type": "InputUser"},
    ],
    "messages.getAttachMenuBots": [
        {"name": "hash", "tl_type": "long"},
    ],
    "messages.getDocumentByHash": [
        {"name": "sha256", "tl_type": "bytes"},
        {"name": "size", "tl_type": "long"},
        {"name": "mime_type", "tl_type": "string"},
    ],
    "messages.getEmojiKeywords": [
        {"name": "lang_code", "tl_type": "string"},
    ],
    "messages.getEmojiKeywordsDifference": [
        {"name": "lang_code", "tl_type": "string"},
        {"name": "from_version", "tl_type": "int"},
    ],
    "messages.getEmojiURL": [
        {"name": "lang_code", "tl_type": "string"},
    ],
    "messages.getExtendedMedia": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "id", "tl_type": "Vector"},
    ],
    "messages.getFutureChatCreatorAfterLeave": [
        {"name": "peer", "tl_type": "InputPeer"},
    ],
    "messages.getMessagesReactions": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "id", "tl_type": "Vector"},
    ],
    "messages.getOnlines": [
        {"name": "peer", "tl_type": "InputPeer"},
    ],
    "messages.getOutboxReadDate": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
    ],
    "messages.getPollResults": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "poll_hash", "tl_type": "long"},
    ],
    "messages.hideAllChatJoinRequests": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "approved", "tl_type": "true", "cond": 0},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "link", "tl_type": "string", "cond": 1},
    ],
    "messages.hideChatJoinRequest": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "approved", "tl_type": "true", "cond": 0},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "user_id", "tl_type": "InputUser"},
    ],
    "messages.hidePeerSettingsBar": [
        {"name": "peer", "tl_type": "InputPeer"},
    ],
    "messages.markDialogUnread": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "unread", "tl_type": "true", "cond": 0},
        {"name": "parent_peer", "tl_type": "InputPeer", "cond": 1},
        {"name": "peer", "tl_type": "InputDialogPeer"},
    ],
    "messages.migrateChat": [
        {"name": "chat_id", "tl_type": "long"},
    ],
    "messages.prolongWebView": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "silent", "tl_type": "true", "cond": 5},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "query_id", "tl_type": "long"},
        {"name": "reply_to", "tl_type": "InputReplyTo", "cond": 0},
        {"name": "send_as", "tl_type": "InputPeer", "cond": 13},
    ],
    "messages.rateTranscribedAudio": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "transcription_id", "tl_type": "long"},
        {"name": "good", "tl_type": "Bool"},
    ],
    "messages.readDiscussion": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "read_max_id", "tl_type": "int"},
    ],
    "messages.readEncryptedHistory": [
        {"name": "peer", "tl_type": "InputEncryptedChat"},
        {"name": "max_date", "tl_type": "int"},
    ],
    "messages.readFeaturedStickers": [
        {"name": "id", "tl_type": "Vector"},
    ],
    "messages.readSavedHistory": [
        {"name": "parent_peer", "tl_type": "InputPeer"},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "max_id", "tl_type": "int"},
    ],
    "messages.reorderPinnedDialogs": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "force", "tl_type": "true", "cond": 0},
        {"name": "folder_id", "tl_type": "int"},
        {"name": "order", "tl_type": "Vector"},
    ],
    "messages.reorderPinnedForumTopics": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "force", "tl_type": "true", "cond": 0},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "order", "tl_type": "Vector"},
    ],
    "messages.reorderPinnedSavedDialogs": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "force", "tl_type": "true", "cond": 0},
        {"name": "order", "tl_type": "Vector"},
    ],
    "messages.reorderQuickReplies": [
        {"name": "order", "tl_type": "Vector"},
    ],
    "messages.reorderStickerSets": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "masks", "tl_type": "true", "cond": 0},
        {"name": "emojis", "tl_type": "true", "cond": 1},
        {"name": "order", "tl_type": "Vector"},
    ],
    "messages.report": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "id", "tl_type": "Vector"},
        {"name": "option", "tl_type": "bytes"},
        {"name": "message", "tl_type": "string"},
    ],
    "messages.reportEncryptedSpam": [
        {"name": "peer", "tl_type": "InputEncryptedChat"},
    ],
    "messages.reportMessagesDelivery": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "push", "tl_type": "true", "cond": 0},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "id", "tl_type": "Vector"},
    ],
    "messages.reportMusicListen": [
        {"name": "id", "tl_type": "InputDocument"},
        {"name": "listened_duration", "tl_type": "int"},
    ],
    "messages.reportReaction": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "id", "tl_type": "int"},
        {"name": "reaction_peer", "tl_type": "InputPeer"},
    ],
    "messages.reportReadMetrics": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "metrics", "tl_type": "Vector"},
    ],
    "messages.reportSpam": [
        {"name": "peer", "tl_type": "InputPeer"},
    ],
    "messages.requestAppWebView": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "write_allowed", "tl_type": "true", "cond": 0},
        {"name": "compact", "tl_type": "true", "cond": 7},
        {"name": "fullscreen", "tl_type": "true", "cond": 8},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "app", "tl_type": "InputBotApp"},
        {"name": "start_param", "tl_type": "string", "cond": 1},
        {"name": "theme_params", "tl_type": "DataJSON", "cond": 2},
        {"name": "platform", "tl_type": "string"},
    ],
    "messages.requestEncryption": [
        {"name": "user_id", "tl_type": "InputUser"},
        {"name": "random_id", "tl_type": "int"},
        {"name": "g_a", "tl_type": "bytes"},
    ],
    "messages.requestMainWebView": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "compact", "tl_type": "true", "cond": 7},
        {"name": "fullscreen", "tl_type": "true", "cond": 8},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "start_param", "tl_type": "string", "cond": 1},
        {"name": "theme_params", "tl_type": "DataJSON", "cond": 0},
        {"name": "platform", "tl_type": "string"},
    ],
    "messages.requestSimpleWebView": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "from_switch_webview", "tl_type": "true", "cond": 1},
        {"name": "from_side_menu", "tl_type": "true", "cond": 2},
        {"name": "compact", "tl_type": "true", "cond": 7},
        {"name": "fullscreen", "tl_type": "true", "cond": 8},
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "url", "tl_type": "string", "cond": 3},
        {"name": "start_param", "tl_type": "string", "cond": 4},
        {"name": "theme_params", "tl_type": "DataJSON", "cond": 0},
        {"name": "platform", "tl_type": "string"},
    ],
    "messages.requestUrlAuth": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "InputPeer", "cond": 1},
        {"name": "msg_id", "tl_type": "int", "cond": 1},
        {"name": "button_id", "tl_type": "int", "cond": 1},
        {"name": "url", "tl_type": "string", "cond": 2},
        {"name": "in_app_origin", "tl_type": "string", "cond": 3},
    ],
    "messages.requestWebView": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "from_bot_menu", "tl_type": "true", "cond": 4},
        {"name": "silent", "tl_type": "true", "cond": 5},
        {"name": "compact", "tl_type": "true", "cond": 7},
        {"name": "fullscreen", "tl_type": "true", "cond": 8},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "url", "tl_type": "string", "cond": 1},
        {"name": "start_param", "tl_type": "string", "cond": 3},
        {"name": "theme_params", "tl_type": "DataJSON", "cond": 2},
        {"name": "platform", "tl_type": "string"},
        {"name": "reply_to", "tl_type": "InputReplyTo", "cond": 0},
        {"name": "send_as", "tl_type": "InputPeer", "cond": 13},
    ],
    "messages.saveDefaultSendAs": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "send_as", "tl_type": "InputPeer"},
    ],
    "messages.saveDraft": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "no_webpage", "tl_type": "true", "cond": 1},
        {"name": "invert_media", "tl_type": "true", "cond": 6},
        {"name": "reply_to", "tl_type": "InputReplyTo", "cond": 4},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "message", "tl_type": "string"},
        {"name": "entities", "tl_type": "Vector", "cond": 3},
        {"name": "media", "tl_type": "InputMedia", "cond": 5},
        {"name": "effect", "tl_type": "long", "cond": 7},
        {"name": "suggested_post", "tl_type": "SuggestedPost", "cond": 8},
        {"name": "rich_message", "tl_type": "InputRichMessage", "cond": 9},
    ],
    "messages.saveGif": [
        {"name": "id", "tl_type": "InputDocument"},
        {"name": "unsave", "tl_type": "Bool"},
    ],
    "messages.saveRecentSticker": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "attached", "tl_type": "true", "cond": 0},
        {"name": "id", "tl_type": "InputDocument"},
        {"name": "unsave", "tl_type": "Bool"},
    ],
    "messages.searchCustomEmoji": [
        {"name": "emoticon", "tl_type": "string"},
        {"name": "hash", "tl_type": "long"},
    ],
    "messages.sendBotRequestedPeer": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int", "cond": 0},
        {"name": "webapp_req_id", "tl_type": "string", "cond": 1},
        {"name": "button_id", "tl_type": "int"},
        {"name": "requested_peers", "tl_type": "Vector"},
    ],
    "messages.sendInlineBotResult": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "silent", "tl_type": "true", "cond": 5},
        {"name": "background", "tl_type": "true", "cond": 6},
        {"name": "clear_draft", "tl_type": "true", "cond": 7},
        {"name": "hide_via", "tl_type": "true", "cond": 11},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "reply_to", "tl_type": "InputReplyTo", "cond": 0},
        {"name": "random_id", "tl_type": "long"},
        {"name": "query_id", "tl_type": "long"},
        {"name": "id", "tl_type": "string"},
        {"name": "schedule_date", "tl_type": "int", "cond": 10},
        {"name": "send_as", "tl_type": "InputPeer", "cond": 13},
        {"name": "quick_reply_shortcut", "tl_type": "InputQuickReplyShortcut", "cond": 17},
        {"name": "allow_paid_stars", "tl_type": "long", "cond": 21},
    ],
    "messages.sendMedia": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "silent", "tl_type": "true", "cond": 5},
        {"name": "background", "tl_type": "true", "cond": 6},
        {"name": "clear_draft", "tl_type": "true", "cond": 7},
        {"name": "noforwards", "tl_type": "true", "cond": 14},
        {"name": "update_stickersets_order", "tl_type": "true", "cond": 15},
        {"name": "invert_media", "tl_type": "true", "cond": 16},
        {"name": "allow_paid_floodskip", "tl_type": "true", "cond": 19},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "reply_to", "tl_type": "InputReplyTo", "cond": 0},
        {"name": "media", "tl_type": "InputMedia"},
        {"name": "message", "tl_type": "string"},
        {"name": "random_id", "tl_type": "long"},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
        {"name": "entities", "tl_type": "Vector", "cond": 3},
        {"name": "schedule_date", "tl_type": "int", "cond": 10},
        {"name": "schedule_repeat_period", "tl_type": "int", "cond": 24},
        {"name": "send_as", "tl_type": "InputPeer", "cond": 13},
        {"name": "quick_reply_shortcut", "tl_type": "InputQuickReplyShortcut", "cond": 17},
        {"name": "effect", "tl_type": "long", "cond": 18},
        {"name": "allow_paid_stars", "tl_type": "long", "cond": 21},
        {"name": "suggested_post", "tl_type": "SuggestedPost", "cond": 22},
    ],
    "messages.sendMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "no_webpage", "tl_type": "true", "cond": 1},
        {"name": "silent", "tl_type": "true", "cond": 5},
        {"name": "background", "tl_type": "true", "cond": 6},
        {"name": "clear_draft", "tl_type": "true", "cond": 7},
        {"name": "noforwards", "tl_type": "true", "cond": 14},
        {"name": "update_stickersets_order", "tl_type": "true", "cond": 15},
        {"name": "invert_media", "tl_type": "true", "cond": 16},
        {"name": "allow_paid_floodskip", "tl_type": "true", "cond": 19},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "reply_to", "tl_type": "InputReplyTo", "cond": 0},
        {"name": "message", "tl_type": "string"},
        {"name": "random_id", "tl_type": "long"},
        {"name": "reply_markup", "tl_type": "ReplyMarkup", "cond": 2},
        {"name": "entities", "tl_type": "Vector", "cond": 3},
        {"name": "schedule_date", "tl_type": "int", "cond": 10},
        {"name": "schedule_repeat_period", "tl_type": "int", "cond": 24},
        {"name": "send_as", "tl_type": "InputPeer", "cond": 13},
        {"name": "quick_reply_shortcut", "tl_type": "InputQuickReplyShortcut", "cond": 17},
        {"name": "effect", "tl_type": "long", "cond": 18},
        {"name": "allow_paid_stars", "tl_type": "long", "cond": 21},
        {"name": "suggested_post", "tl_type": "SuggestedPost", "cond": 22},
        {"name": "rich_message", "tl_type": "InputRichMessage", "cond": 23},
    ],
    "messages.sendMultiMedia": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "silent", "tl_type": "true", "cond": 5},
        {"name": "background", "tl_type": "true", "cond": 6},
        {"name": "clear_draft", "tl_type": "true", "cond": 7},
        {"name": "noforwards", "tl_type": "true", "cond": 14},
        {"name": "update_stickersets_order", "tl_type": "true", "cond": 15},
        {"name": "invert_media", "tl_type": "true", "cond": 16},
        {"name": "allow_paid_floodskip", "tl_type": "true", "cond": 19},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "reply_to", "tl_type": "InputReplyTo", "cond": 0},
        {"name": "multi_media", "tl_type": "Vector"},
        {"name": "schedule_date", "tl_type": "int", "cond": 10},
        {"name": "send_as", "tl_type": "InputPeer", "cond": 13},
        {"name": "quick_reply_shortcut", "tl_type": "InputQuickReplyShortcut", "cond": 17},
        {"name": "effect", "tl_type": "long", "cond": 18},
        {"name": "allow_paid_stars", "tl_type": "long", "cond": 21},
    ],
    "messages.sendPaidReaction": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "count", "tl_type": "int"},
        {"name": "random_id", "tl_type": "long"},
        {"name": "private", "tl_type": "PaidReactionPrivacy", "cond": 0},
    ],
    "messages.sendQuickReplyMessages": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "shortcut_id", "tl_type": "int"},
        {"name": "id", "tl_type": "Vector"},
        {"name": "random_id", "tl_type": "Vector"},
    ],
    "messages.sendReaction": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "big", "tl_type": "true", "cond": 1},
        {"name": "add_to_recent", "tl_type": "true", "cond": 2},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "reaction", "tl_type": "Vector", "cond": 0},
    ],
    "messages.sendScheduledMessages": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "id", "tl_type": "Vector"},
    ],
    "messages.sendScreenshotNotification": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "reply_to", "tl_type": "InputReplyTo"},
        {"name": "random_id", "tl_type": "long"},
    ],
    "messages.sendVote": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "options", "tl_type": "Vector"},
    ],
    "messages.sendWebViewData": [
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "random_id", "tl_type": "long"},
        {"name": "button_text", "tl_type": "string"},
        {"name": "data", "tl_type": "string"},
    ],
    "messages.sendWebViewResultMessage": [
        {"name": "bot_query_id", "tl_type": "string"},
        {"name": "result", "tl_type": "InputBotInlineResult"},
    ],
    "messages.setBotCallbackAnswer": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "alert", "tl_type": "true", "cond": 1},
        {"name": "query_id", "tl_type": "long"},
        {"name": "message", "tl_type": "string", "cond": 0},
        {"name": "url", "tl_type": "string", "cond": 2},
        {"name": "cache_time", "tl_type": "int"},
    ],
    "messages.setBotGuestChatResult": [
        {"name": "query_id", "tl_type": "long"},
        {"name": "result", "tl_type": "InputBotInlineResult"},
    ],
    "messages.setBotPrecheckoutResults": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "success", "tl_type": "true", "cond": 1},
        {"name": "query_id", "tl_type": "long"},
        {"name": "error", "tl_type": "string", "cond": 0},
    ],
    "messages.setBotShippingResults": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "query_id", "tl_type": "long"},
        {"name": "error", "tl_type": "string", "cond": 0},
        {"name": "shipping_options", "tl_type": "Vector", "cond": 1},
    ],
    "messages.setChatAvailableReactions": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "available_reactions", "tl_type": "ChatReactions"},
        {"name": "reactions_limit", "tl_type": "int", "cond": 0},
        {"name": "paid_enabled", "tl_type": "Bool", "cond": 1},
    ],
    "messages.setChatTheme": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "theme", "tl_type": "InputChatTheme"},
    ],
    "messages.setChatWallPaper": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "for_both", "tl_type": "true", "cond": 3},
        {"name": "revert", "tl_type": "true", "cond": 4},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "wallpaper", "tl_type": "InputWallPaper", "cond": 0},
        {"name": "settings", "tl_type": "WallPaperSettings", "cond": 2},
        {"name": "id", "tl_type": "int", "cond": 1},
    ],
    "messages.setDefaultHistoryTTL": [
        {"name": "period", "tl_type": "int"},
    ],
    "messages.setDefaultReaction": [
        {"name": "reaction", "tl_type": "Reaction"},
    ],
    "messages.setEncryptedTyping": [
        {"name": "peer", "tl_type": "InputEncryptedChat"},
        {"name": "typing", "tl_type": "Bool"},
    ],
    "messages.setGameScore": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "edit_message", "tl_type": "true", "cond": 0},
        {"name": "force", "tl_type": "true", "cond": 1},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "id", "tl_type": "int"},
        {"name": "user_id", "tl_type": "InputUser"},
        {"name": "score", "tl_type": "int"},
    ],
    "messages.setHistoryTTL": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "period", "tl_type": "int"},
    ],
    "messages.setInlineBotResults": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "gallery", "tl_type": "true", "cond": 0},
        {"name": "private", "tl_type": "true", "cond": 1},
        {"name": "query_id", "tl_type": "long"},
        {"name": "results", "tl_type": "Vector"},
        {"name": "cache_time", "tl_type": "int"},
        {"name": "next_offset", "tl_type": "string", "cond": 2},
        {"name": "switch_pm", "tl_type": "InlineBotSwitchPM", "cond": 3},
        {"name": "switch_webview", "tl_type": "InlineBotWebView", "cond": 4},
    ],
    "messages.setInlineGameScore": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "edit_message", "tl_type": "true", "cond": 0},
        {"name": "force", "tl_type": "true", "cond": 1},
        {"name": "id", "tl_type": "InputBotInlineMessageID"},
        {"name": "user_id", "tl_type": "InputUser"},
        {"name": "score", "tl_type": "int"},
    ],
    "messages.setTyping": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "top_msg_id", "tl_type": "int", "cond": 0},
        {"name": "action", "tl_type": "SendMessageAction"},
    ],
    "messages.startBot": [
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "random_id", "tl_type": "long"},
        {"name": "start_param", "tl_type": "string"},
    ],
    "messages.startHistoryImport": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "import_id", "tl_type": "long"},
    ],
    "messages.summarizeText": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "id", "tl_type": "int"},
        {"name": "to_lang", "tl_type": "string", "cond": 0},
        {"name": "tone", "tl_type": "string", "cond": 2},
    ],
    "messages.toggleBotInAttachMenu": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "write_allowed", "tl_type": "true", "cond": 0},
        {"name": "bot", "tl_type": "InputUser"},
        {"name": "enabled", "tl_type": "Bool"},
    ],
    "messages.toggleDialogFilterTags": [
        {"name": "enabled", "tl_type": "Bool"},
    ],
    "messages.toggleDialogPin": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "pinned", "tl_type": "true", "cond": 0},
        {"name": "peer", "tl_type": "InputDialogPeer"},
    ],
    "messages.toggleNoForwards": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "enabled", "tl_type": "Bool"},
        {"name": "request_msg_id", "tl_type": "int", "cond": 0},
    ],
    "messages.togglePaidReactionPrivacy": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "private", "tl_type": "PaidReactionPrivacy"},
    ],
    "messages.togglePeerTranslations": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "disabled", "tl_type": "true", "cond": 0},
        {"name": "peer", "tl_type": "InputPeer"},
    ],
    "messages.toggleSavedDialogPin": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "pinned", "tl_type": "true", "cond": 0},
        {"name": "peer", "tl_type": "InputDialogPeer"},
    ],
    "messages.toggleStickerSets": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "uninstall", "tl_type": "true", "cond": 0},
        {"name": "archive", "tl_type": "true", "cond": 1},
        {"name": "unarchive", "tl_type": "true", "cond": 2},
        {"name": "stickersets", "tl_type": "Vector"},
    ],
    "messages.toggleSuggestedPostApproval": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "reject", "tl_type": "true", "cond": 1},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "schedule_date", "tl_type": "int", "cond": 0},
        {"name": "reject_comment", "tl_type": "string", "cond": 2},
    ],
    "messages.toggleTodoCompleted": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "msg_id", "tl_type": "int"},
        {"name": "completed", "tl_type": "Vector"},
        {"name": "incompleted", "tl_type": "Vector"},
    ],
    "messages.uninstallStickerSet": [
        {"name": "stickerset", "tl_type": "InputStickerSet"},
    ],
    "messages.updateDialogFilter": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "id", "tl_type": "int"},
        {"name": "filter", "tl_type": "DialogFilter", "cond": 0},
    ],
    "messages.updateDialogFiltersOrder": [
        {"name": "order", "tl_type": "Vector"},
    ],
    "messages.updatePinnedForumTopic": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "topic_id", "tl_type": "int"},
        {"name": "pinned", "tl_type": "Bool"},
    ],
    "messages.updatePinnedMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "silent", "tl_type": "true", "cond": 0},
        {"name": "unpin", "tl_type": "true", "cond": 1},
        {"name": "pm_oneside", "tl_type": "true", "cond": 2},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "id", "tl_type": "int"},
    ],
    "messages.updateSavedReactionTag": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "reaction", "tl_type": "Reaction"},
        {"name": "title", "tl_type": "string", "cond": 0},
    ],
    "messages.uploadEncryptedFile": [
        {"name": "peer", "tl_type": "InputEncryptedChat"},
        {"name": "file", "tl_type": "InputEncryptedFile"},
    ],
    "messages.uploadImportedMedia": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "import_id", "tl_type": "long"},
        {"name": "file_name", "tl_type": "string"},
        {"name": "media", "tl_type": "InputMedia"},
    ],
    "messages.uploadMedia": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "business_connection_id", "tl_type": "string", "cond": 0},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "media", "tl_type": "InputMedia"},
    ],
    "messages.viewSponsoredMessage": [
        {"name": "random_id", "tl_type": "bytes"},
    ],
    "payments.applyGiftCode": [
        {"name": "slug", "tl_type": "string"},
    ],
    "payments.assignAppStoreTransaction": [
        {"name": "receipt", "tl_type": "bytes"},
        {"name": "purpose", "tl_type": "InputStorePaymentPurpose"},
    ],
    "payments.assignPlayMarketTransaction": [
        {"name": "receipt", "tl_type": "DataJSON"},
        {"name": "purpose", "tl_type": "InputStorePaymentPurpose"},
    ],
    "payments.botCancelStarsSubscription": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "restore", "tl_type": "true", "cond": 0},
        {"name": "user_id", "tl_type": "InputUser"},
        {"name": "charge_id", "tl_type": "string"},
    ],
    "payments.canPurchaseStore": [
        {"name": "purpose", "tl_type": "InputStorePaymentPurpose"},
    ],
    "payments.changeStarsSubscription": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "subscription_id", "tl_type": "string"},
        {"name": "canceled", "tl_type": "Bool", "cond": 0},
    ],
    "payments.clearSavedInfo": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "credentials", "tl_type": "true", "cond": 0},
        {"name": "info", "tl_type": "true", "cond": 1},
    ],
    "payments.convertStarGift": [
        {"name": "stargift", "tl_type": "InputSavedStarGift"},
    ],
    "payments.craftStarGift": [
        {"name": "stargift", "tl_type": "Vector"},
    ],
    "payments.createStarGiftCollection": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "title", "tl_type": "string"},
        {"name": "stargift", "tl_type": "Vector"},
    ],
    "payments.deleteStarGiftCollection": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "collection_id", "tl_type": "int"},
    ],
    "payments.fulfillStarsSubscription": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "subscription_id", "tl_type": "string"},
    ],
    "payments.launchPrepaidGiveaway": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "giveaway_id", "tl_type": "long"},
        {"name": "purpose", "tl_type": "InputStorePaymentPurpose"},
    ],
    "payments.refundStarsCharge": [
        {"name": "user_id", "tl_type": "InputUser"},
        {"name": "charge_id", "tl_type": "string"},
    ],
    "payments.reorderStarGiftCollections": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "order", "tl_type": "Vector"},
    ],
    "payments.resolveStarGiftOffer": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "decline", "tl_type": "true", "cond": 0},
        {"name": "offer_msg_id", "tl_type": "int"},
    ],
    "payments.saveStarGift": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "unsave", "tl_type": "true", "cond": 0},
        {"name": "stargift", "tl_type": "InputSavedStarGift"},
    ],
    "payments.sendStarGiftOffer": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "slug", "tl_type": "string"},
        {"name": "price", "tl_type": "StarsAmount"},
        {"name": "duration", "tl_type": "int"},
        {"name": "random_id", "tl_type": "long"},
        {"name": "allow_paid_stars", "tl_type": "long", "cond": 0},
    ],
    "payments.toggleChatStarGiftNotifications": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "enabled", "tl_type": "true", "cond": 0},
        {"name": "peer", "tl_type": "InputPeer"},
    ],
    "payments.toggleStarGiftsPinnedToTop": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "stargift", "tl_type": "Vector"},
    ],
    "payments.transferStarGift": [
        {"name": "stargift", "tl_type": "InputSavedStarGift"},
        {"name": "to_id", "tl_type": "InputPeer"},
    ],
    "payments.updateStarGiftCollection": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "collection_id", "tl_type": "int"},
        {"name": "title", "tl_type": "string", "cond": 0},
        {"name": "delete_stargift", "tl_type": "Vector", "cond": 1},
        {"name": "add_stargift", "tl_type": "Vector", "cond": 2},
        {"name": "order", "tl_type": "Vector", "cond": 3},
    ],
    "payments.updateStarGiftPrice": [
        {"name": "stargift", "tl_type": "InputSavedStarGift"},
        {"name": "resell_amount", "tl_type": "StarsAmount"},
    ],
    "payments.upgradeStarGift": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "keep_original_details", "tl_type": "true", "cond": 0},
        {"name": "stargift", "tl_type": "InputSavedStarGift"},
    ],
    "phone.createConferenceCall": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "muted", "tl_type": "true", "cond": 0},
        {"name": "video_stopped", "tl_type": "true", "cond": 2},
        {"name": "join", "tl_type": "true", "cond": 3},
        {"name": "random_id", "tl_type": "int"},
        {"name": "public_key", "tl_type": "int256", "cond": 3},
        {"name": "block", "tl_type": "bytes", "cond": 3},
        {"name": "params", "tl_type": "DataJSON", "cond": 3},
    ],
    "phone.createGroupCall": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "rtmp_stream", "tl_type": "true", "cond": 2},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "random_id", "tl_type": "int"},
        {"name": "title", "tl_type": "string", "cond": 0},
        {"name": "schedule_date", "tl_type": "int", "cond": 1},
    ],
    "phone.declineConferenceCallInvite": [
        {"name": "msg_id", "tl_type": "int"},
    ],
    "phone.deleteConferenceCallParticipants": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "only_left", "tl_type": "true", "cond": 0},
        {"name": "kick", "tl_type": "true", "cond": 1},
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "ids", "tl_type": "Vector"},
        {"name": "block", "tl_type": "bytes"},
    ],
    "phone.deleteGroupCallMessages": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "report_spam", "tl_type": "true", "cond": 0},
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "messages", "tl_type": "Vector"},
    ],
    "phone.deleteGroupCallParticipantMessages": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "report_spam", "tl_type": "true", "cond": 0},
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "participant", "tl_type": "InputPeer"},
    ],
    "phone.discardCall": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "video", "tl_type": "true", "cond": 0},
        {"name": "peer", "tl_type": "InputPhoneCall"},
        {"name": "duration", "tl_type": "int"},
        {"name": "reason", "tl_type": "PhoneCallDiscardReason"},
        {"name": "connection_id", "tl_type": "long"},
    ],
    "phone.discardGroupCall": [
        {"name": "call", "tl_type": "InputGroupCall"},
    ],
    "phone.editGroupCallParticipant": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "participant", "tl_type": "InputPeer"},
        {"name": "muted", "tl_type": "Bool", "cond": 0},
        {"name": "volume", "tl_type": "int", "cond": 1},
        {"name": "raise_hand", "tl_type": "Bool", "cond": 2},
        {"name": "video_stopped", "tl_type": "Bool", "cond": 3},
        {"name": "video_paused", "tl_type": "Bool", "cond": 4},
        {"name": "presentation_paused", "tl_type": "Bool", "cond": 5},
    ],
    "phone.editGroupCallTitle": [
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "title", "tl_type": "string"},
    ],
    "phone.getGroupCallChainBlocks": [
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "sub_chain_id", "tl_type": "int"},
        {"name": "offset", "tl_type": "int"},
        {"name": "limit", "tl_type": "int"},
    ],
    "phone.inviteConferenceCallParticipant": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "video", "tl_type": "true", "cond": 0},
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "user_id", "tl_type": "InputUser"},
    ],
    "phone.inviteToGroupCall": [
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "users", "tl_type": "Vector"},
    ],
    "phone.joinGroupCall": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "muted", "tl_type": "true", "cond": 0},
        {"name": "video_stopped", "tl_type": "true", "cond": 2},
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "join_as", "tl_type": "InputPeer"},
        {"name": "invite_hash", "tl_type": "string", "cond": 1},
        {"name": "public_key", "tl_type": "int256", "cond": 3},
        {"name": "block", "tl_type": "bytes", "cond": 3},
        {"name": "params", "tl_type": "DataJSON"},
    ],
    "phone.joinGroupCallPresentation": [
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "params", "tl_type": "DataJSON"},
    ],
    "phone.leaveGroupCall": [
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "source", "tl_type": "int"},
    ],
    "phone.leaveGroupCallPresentation": [
        {"name": "call", "tl_type": "InputGroupCall"},
    ],
    "phone.receivedCall": [
        {"name": "peer", "tl_type": "InputPhoneCall"},
    ],
    "phone.saveCallDebug": [
        {"name": "peer", "tl_type": "InputPhoneCall"},
        {"name": "debug", "tl_type": "DataJSON"},
    ],
    "phone.saveCallLog": [
        {"name": "peer", "tl_type": "InputPhoneCall"},
        {"name": "file", "tl_type": "InputFile"},
    ],
    "phone.saveDefaultGroupCallJoinAs": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "join_as", "tl_type": "InputPeer"},
    ],
    "phone.saveDefaultSendAs": [
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "send_as", "tl_type": "InputPeer"},
    ],
    "phone.sendConferenceCallBroadcast": [
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "block", "tl_type": "bytes"},
    ],
    "phone.sendGroupCallEncryptedMessage": [
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "encrypted_message", "tl_type": "bytes"},
    ],
    "phone.sendGroupCallMessage": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "random_id", "tl_type": "long"},
        {"name": "message", "tl_type": "TextWithEntities"},
        {"name": "allow_paid_stars", "tl_type": "long", "cond": 0},
        {"name": "send_as", "tl_type": "InputPeer", "cond": 1},
    ],
    "phone.sendSignalingData": [
        {"name": "peer", "tl_type": "InputPhoneCall"},
        {"name": "data", "tl_type": "bytes"},
    ],
    "phone.setCallRating": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "user_initiative", "tl_type": "true", "cond": 0},
        {"name": "peer", "tl_type": "InputPhoneCall"},
        {"name": "rating", "tl_type": "int"},
        {"name": "comment", "tl_type": "string"},
    ],
    "phone.startScheduledGroupCall": [
        {"name": "call", "tl_type": "InputGroupCall"},
    ],
    "phone.toggleGroupCallRecord": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "start", "tl_type": "true", "cond": 0},
        {"name": "video", "tl_type": "true", "cond": 2},
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "title", "tl_type": "string", "cond": 1},
        {"name": "video_portrait", "tl_type": "Bool", "cond": 2},
    ],
    "phone.toggleGroupCallSettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "reset_invite_hash", "tl_type": "true", "cond": 1},
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "join_muted", "tl_type": "Bool", "cond": 0},
        {"name": "messages_enabled", "tl_type": "Bool", "cond": 2},
        {"name": "send_paid_messages_stars", "tl_type": "long", "cond": 3},
    ],
    "phone.toggleGroupCallStartSubscription": [
        {"name": "call", "tl_type": "InputGroupCall"},
        {"name": "subscribed", "tl_type": "Bool"},
    ],
    "smsjobs.finishJob": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "job_id", "tl_type": "string"},
        {"name": "error", "tl_type": "string", "cond": 0},
    ],
    "smsjobs.getSmsJob": [
        {"name": "job_id", "tl_type": "string"},
    ],
    "smsjobs.updateSettings": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "allow_international", "tl_type": "true", "cond": 0},
    ],
    "stats.loadAsyncGraph": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "token", "tl_type": "string"},
        {"name": "x", "tl_type": "long", "cond": 0},
    ],
    "stickers.checkShortName": [
        {"name": "short_name", "tl_type": "string"},
    ],
    "stickers.deleteStickerSet": [
        {"name": "stickerset", "tl_type": "InputStickerSet"},
    ],
    "stories.activateStealthMode": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "past", "tl_type": "true", "cond": 0},
        {"name": "future", "tl_type": "true", "cond": 1},
    ],
    "stories.createAlbum": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "title", "tl_type": "string"},
        {"name": "stories", "tl_type": "Vector"},
    ],
    "stories.deleteAlbum": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "album_id", "tl_type": "int"},
    ],
    "stories.editStory": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "id", "tl_type": "int"},
        {"name": "media", "tl_type": "InputMedia", "cond": 0},
        {"name": "media_areas", "tl_type": "Vector", "cond": 3},
        {"name": "caption", "tl_type": "string", "cond": 1},
        {"name": "entities", "tl_type": "Vector", "cond": 1},
        {"name": "privacy_rules", "tl_type": "Vector", "cond": 2},
        {"name": "music", "tl_type": "InputDocument", "cond": 4},
    ],
    "stories.exportStoryLink": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "id", "tl_type": "int"},
    ],
    "stories.incrementStoryViews": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "id", "tl_type": "Vector"},
    ],
    "stories.reorderAlbums": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "order", "tl_type": "Vector"},
    ],
    "stories.report": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "id", "tl_type": "Vector"},
        {"name": "option", "tl_type": "bytes"},
        {"name": "message", "tl_type": "string"},
    ],
    "stories.sendReaction": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "add_to_recent", "tl_type": "true", "cond": 0},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "story_id", "tl_type": "int"},
        {"name": "reaction", "tl_type": "Reaction"},
    ],
    "stories.sendStory": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "pinned", "tl_type": "true", "cond": 2},
        {"name": "noforwards", "tl_type": "true", "cond": 4},
        {"name": "fwd_modified", "tl_type": "true", "cond": 7},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "media", "tl_type": "InputMedia"},
        {"name": "media_areas", "tl_type": "Vector", "cond": 5},
        {"name": "caption", "tl_type": "string", "cond": 0},
        {"name": "entities", "tl_type": "Vector", "cond": 1},
        {"name": "privacy_rules", "tl_type": "Vector"},
        {"name": "random_id", "tl_type": "long"},
        {"name": "period", "tl_type": "int", "cond": 3},
        {"name": "fwd_from_id", "tl_type": "InputPeer", "cond": 6},
        {"name": "fwd_from_story", "tl_type": "int", "cond": 6},
        {"name": "albums", "tl_type": "Vector", "cond": 8},
        {"name": "music", "tl_type": "InputDocument", "cond": 9},
    ],
    "stories.startLive": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "pinned", "tl_type": "true", "cond": 2},
        {"name": "noforwards", "tl_type": "true", "cond": 4},
        {"name": "rtmp_stream", "tl_type": "true", "cond": 5},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "caption", "tl_type": "string", "cond": 0},
        {"name": "entities", "tl_type": "Vector", "cond": 1},
        {"name": "privacy_rules", "tl_type": "Vector"},
        {"name": "random_id", "tl_type": "long"},
        {"name": "messages_enabled", "tl_type": "Bool", "cond": 6},
        {"name": "send_paid_messages_stars", "tl_type": "long", "cond": 7},
    ],
    "stories.toggleAllStoriesHidden": [
        {"name": "hidden", "tl_type": "Bool"},
    ],
    "stories.togglePeerStoriesHidden": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "hidden", "tl_type": "Bool"},
    ],
    "stories.togglePinnedToTop": [
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "id", "tl_type": "Vector"},
    ],
    "stories.updateAlbum": [
        {"name": "flags", "tl_type": "flags", "is_flag": True},
        {"name": "peer", "tl_type": "InputPeer"},
        {"name": "album_id", "tl_type": "int"},
        {"name": "title", "tl_type": "string", "cond": 0},
        {"name": "delete_stories", "tl_type": "Vector", "cond": 1},
        {"name": "add_stories", "tl_type": "Vector", "cond": 2},
        {"name": "order", "tl_type": "Vector", "cond": 3},
    ],
    "upload.saveBigFilePart": [
        {"name": "file_id", "tl_type": "long"},
        {"name": "file_part", "tl_type": "int"},
        {"name": "file_total_parts", "tl_type": "int"},
        {"name": "bytes", "tl_type": "bytes"},
    ],
    "upload.saveFilePart": [
        {"name": "file_id", "tl_type": "long"},
        {"name": "file_part", "tl_type": "int"},
        {"name": "bytes", "tl_type": "bytes"},
    ],
    "users.setSecureValueErrors": [
        {"name": "id", "tl_type": "InputUser"},
        {"name": "errors", "tl_type": "Vector"},
    ],
    "users.suggestBirthday": [
        {"name": "id", "tl_type": "InputUser"},
        {"name": "birthday", "tl_type": "Birthday"},
    ],
}


# === Common InputPeer constructors ===
INPUT_PEER_SELF = 0x7da07ec9
INPUT_PEER_USER = 0x7b8e7de6
INPUT_PEER_CHAT = 0x179be863
INPUT_PEER_CHANNEL = 0x20adaef8
