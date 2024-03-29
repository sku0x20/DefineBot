pingRequest = '''
{
   "application_id":"replaceApplicationId",
   "id":"replaceRequestId",
   "token":"replaceRequestToken",
   "type":1,
   "user":{
      "avatar":"44r4e4efe4fet4",
      "discriminator":"3323",
      "id":"67870344238412801",
      "public_flags":0,
      "username":"testuser"
   },
   "version":1
}
'''

hiveFiveRequest = '''
{
   "application_id":"896745356944759297",
   "channel_id":"896805435435t4178",
   "data":{
      "id":"8971523342401613353",
      "name":"High Five",
      "resolved":{
         "members":{
            "678704423321638412801":{
               "avatar":"None",
               "is_pending":false,
               "joined_at":"2021-05-06T11:34:36.095000+00:00",
               "nick":"None",
               "pending":false,
               "permissions":"1099511627775",
               "premium_since":"None",
               "roles":[

               ]
            }
         },
         "users":{
            "678704423321638412801":{
               "avatar":"11f32ff3442f56a05930211814b0f",
               "discriminator":"3123",
               "id":"678704423321638412801",
               "public_flags":0,
               "username":"testuser2"
            }
         }
      },
      "target_id":"678704423321638412801",
      "type":2
   },
   "guild_id":"839432453256422335509",
   "id":"897884324538634",
   "member":{
      "avatar":"None",
      "deaf":false,
      "is_pending":false,
      "joined_at":"2021-05-06T11:34:36.095000+00:00",
      "mute":false,
      "nick":"None",
      "pending":false,
      "permissions":"1099511627775",
      "premium_since":"None",
      "roles":[

      ],
      "user":{
         "avatar":"115ewrwrfwbe261f56a05930211814b0f",
         "discriminator":"3123",
         "id":"67870443424412804",
         "public_flags":0,
         "username":"testuser"
      }
   },
   "token":"feshfse=fesf234",
   "type":2,
   "version":1
}
'''

defineRequest = '''
{
   "application_id":"118382028789745568",
   "channel_id":"432082637558205476",
   "data":{
      "id":"986943371695116014",
      "name":"define",
      "options":[
         {
            "name":"word",
            "type":3,
            "value":"wordToSearch"
         }
      ],
      "type":1
   },
   "guild_id":"480576936483357076",
   "id":"256121478197384959",
   "member":{
      "avatar":"None",
      "deaf":false,
      "is_pending":false,
      "joined_at":"2021-05-06T11:34:36.095000+00:00",
      "mute":false,
      "nick":"None",
      "pending":false,
      "permissions":"1099511627775",
      "premium_since":"None",
      "roles":[

      ],
      "user":{
         "avatar":"7u0uw78r7tws1r4ed0im",
         "discriminator":"9007",
         "id":"532841176724020215",
         "public_flags":0,
         "username":"testuser"
      }
   },
   "token":"x592fcnaee4huvjxg1ea",
   "type":2,
   "version":1
}
'''

anonymousResponse = '''
[
   {
      "word":"anonymous",
      "phonetic":"əˈnɒnɪməs",
      "phonetics":[
         {
            "text":"əˈnɒnɪməs",
            "audio":"//ssl.gstatic.com/dictionary/static/sounds/20200429/anonymous--_gb_1.mp3"
         }
      ],
      "origin":"late 16th century: via late Latin from Greek anōnumos ‘nameless’ (from an- ‘without’ + onoma ‘name’) + -ous.",
      "meanings":[
         {
            "partOfSpeech":"adjective",
            "definitions":[
               {
                  "definition":"(of a person) not identified by name; of unknown name.",
                  "example":"the donor's wish to remain anonymous",
                  "synonyms":[
                     "unnamed",
                     "of unknown name",
                     "nameless",
                     "incognito",
                     "unidentified",
                     "unknown",
                     "unspecified",
                     "undesignated",
                     "unacknowledged",
                     "mystery",
                     "unsung",
                     "innominate",
                     "unsigned",
                     "unattributed",
                     "unattested",
                     "uncredited"
                  ],
                  "antonyms":[
                     "known",
                     "identified",
                     "signed"
                  ]
               }
            ]
         }
      ]
   }
]
'''

testResponse = '''
[
   {
      "word":"test",
      "phonetic":"tɛst",
      "phonetics":[
         {
            "text":"tɛst",
            "audio":"//ssl.gstatic.com/dictionary/static/sounds/20200429/test--_gb_1.mp3"
         }
      ],
      "origin":"late Middle English (denoting a cupel used to treat gold or silver alloys or ore): via Old French from Latin testu, testum ‘earthen pot’, variant of testa ‘jug, shell’. Compare with test2. The verb dates from the early 17th century.",
      "meanings":[
         {
            "partOfSpeech":"noun",
            "definitions":[
               {
                  "definition":"a procedure intended to establish the quality, performance, or reliability of something, especially before it is taken into widespread use.",
                  "example":"both countries carried out nuclear tests in May",
                  "synonyms":[
                     "trial",
                     "experiment",
                     "pilot study",
                     "try-out",
                     "check",
                     "examination",
                     "assessment",
                     "evaluation",
                     "appraisal",
                     "investigation",
                     "inspection",
                     "analysis",
                     "scrutiny",
                     "scrutinization",
                     "study",
                     "probe",
                     "exploration",
                     "screening",
                     "audition",
                     "screen test",
                     "assay"
                  ],
                  "antonyms":[
                     
                  ]
               },
               {
                  "definition":"short for Test match.",
                  "example":"the first Test against New Zealand",
                  "synonyms":[
                     
                  ],
                  "antonyms":[
                     
                  ]
               },
               {
                  "definition":"a movable hearth in a reverberating furnace, used for separating gold or silver from lead.",
                  "synonyms":[
                     
                  ],
                  "antonyms":[
                     
                  ]
               }
            ]
         },
         {
            "partOfSpeech":"verb",
            "definitions":[
               {
                  "definition":"take measures to check the quality, performance, or reliability of (something), especially before putting it into widespread use or practice.",
                  "example":"this range has not been tested on animals",
                  "synonyms":[
                     "try out",
                     "trial",
                     "carry out trials on",
                     "put to the test",
                     "put through its paces",
                     "experiment with",
                     "pilot",
                     "check",
                     "examine",
                     "assess",
                     "evaluate",
                     "appraise",
                     "investigate",
                     "analyse",
                     "scrutinize",
                     "study",
                     "probe",
                     "explore",
                     "sample",
                     "screen",
                     "assay"
                  ],
                  "antonyms":[
                     
                  ]
               }
            ]
         }
      ]
   },
   {
      "word":"test",
      "phonetic":"tɛst",
      "phonetics":[
         {
            "text":"tɛst",
            "audio":"//ssl.gstatic.com/dictionary/static/sounds/20200429/test--_gb_1.mp3"
         }
      ],
      "origin":"mid 19th century: from Latin testa ‘tile, jug, shell’. Compare with test1.",
      "meanings":[
         {
            "partOfSpeech":"noun",
            "definitions":[
               {
                  "definition":"the shell or integument of some invertebrates and protozoans, especially the chalky shell of a foraminiferan or the tough outer layer of a tunicate.",
                  "synonyms":[
                     
                  ],
                  "antonyms":[
                     
                  ]
               }
            ]
         }
      ]
   }
]
'''
