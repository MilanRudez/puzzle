# Solving the tech puzzle ![logo](https://www.smartly.io/hs-fs/hubfs/Frontpage%202019/Support-2.png?width=100&name=Support-2.png)
The tech puzzle is the second step in the interview process that allows candidates such as myself to demonstrate their technical knowledge and the ability to learn and adapt quickly.

## The first steps
According to the e-mail received and the first link provided the first step was to make a JSON request. To save time I used the [Advanced REST client](https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo)to make the call and see what the response will be. The output was as follows:

![First call](https://i.imgur.com/bCqgqyo.png)

Based on the content received it was easy to understand that the next URL I needed to fetch was baseURL + /bucecarlus. So I made a new call to the new page and have received a similar output pointing towards a different page. So, I repeated the step once again to see if the pattern will continue. This time I was encouraged by the output to create a script which confirmed my thoughts - the output will probably remain the same. So I started researching and coding. 

## The alpha script
I decided to use Python as that was the first language I've ever developed an interest in and because I wish to use it in the future for automatizations. As I haven't programmed anything in years I needed to refresh my memory a bit. I've read python documentation (such as [python requests for humans](https://2.python-requests.org//en/latest/user/quickstart/#more-complicated-post-requests)) and created the [first iteration of the script](https://github.com/MilanRudez/puzzle/blob/master/puzzle_alpha.py).

## First "problem"
Reaching the "auth" page required us to solve a regex crossword puzzle in order to get the username and password and then pass that information.

### The regex crossword puzzle
Before I could solve the puzzle I needed to understand the rules behind it. While I used regex in the past and love puzzle games such as Sudoku, Mahjong, etc. I wasn't sure what the approach was here. So I [practiced my regex](https://regexr.com/) for a bit found and read what seemed to be the authority website regarding [regex crossword puzzles](https://regexcrossword.com). There I've done their Tutorial and practiced with their Beginner puzzles. I've also watched a [youtube video](https://www.youtube.com/watch?v=0bT9D_z-BRQ) to make sure I understood the correct approach. After that, I had sufficient understanding to solve the puzzle.

### Using the username and password to authenticate
This was the first thing that made me go "Hmm". I couldn't remember how to authenticate so I took back to reading and decided to use the Advanced REST Client for one more call.

![The call](https://i.imgur.com/Lb1Wr9P.png)

However, right after the call, I've noticed something. The Advanced REST Client was cool enough to give me a hint as to what to do.
![It was such a BASIC problem](https://i.imgur.com/6ocIu8c.png)

So after some reading up, and searching on [stackoverflow](https://stackoverflow.com/questions/6999565/python-https-get-with-basic-authentication), the [second iteration of the script](https://github.com/MilanRudez/puzzle/blob/master/puzzle_beta.py) was basically born.

## Next: Trying the page in html
This was the first time I thought to myself "strange", I can just go to the page and look at the source code. But, curiosity killed the cat and I had to do it. However, I was unable to find a good way to decode and parse HTML so I altered the [final version of the script](https://github.com/MilanRudez/puzzle/blob/master/puzzle.py) to print out the output in PowerShell:

![Printing out html](https://i.imgur.com/HFqxkg2.png)

The output gave me two hints:
1. There was a very cool JavaScript file being used
2. There was a Facebook pixel installed on this page

And looking in the console gave me another hint (console.log, we love you):
1. Cool, you found this. Can you find more cool smartly stuff?

Because of the Facebook pixel, I went to some of the previous pages to check if there was a Facebook pixel installed and there wasn't. This meant that the Facebook pixel, or more accurately the ID of the pixel, should be of some use. Or it could have just been a diversion. But let's look further.

The next thing I've done was un-minify the JavaScript file and look up the text I saw in the console. The reason I've looked that up first is that I had a hunch that what ever else there was that was relevant to me it would be clumped up. That's where I saw:
```javascript
help: "You should explore me more",
        contactEmail: "ZmFzdHRyYWNrK291cl9mYWNlYm9va19pZEBzbWFydGx5Lmlv",
        instructions: "Q29uZ3JhdHVsYXRpb25zLCB5b3UgaGF2ZSBhbG1vc3QgY29tcGxldGVkIHRoZSBGYXN0IFRyYWNrISBBcyB0aGUgbGFzdCB0aGluZywgZmlndXJlIG91dCB0aGUgY29tcGxldGUgY29udGFjdCBhZGRyZXNzIGluIGNvbnRhY3RFbWFpbCBhbmQgc2VuZCB1cyBhIG1lc3NhZ2UuIA0KDQpJZiB5b3UgaGF2ZW4ndCB5ZXQgYmVlbiBpbiBjb250YWN0IHdpdGggdXMsIHdlIGFyZSBpbnRlcmVzdGVkIHRvIGhlYXIgaW4gdGhlIGVtYWlsIGFib3V0IHlvdXIgYmFja2dyb3VuZCBhbmQgaWYgeW91IGFyZSBpbnRlcmVzdGVkIGluIGFueSBvZiBvdXIgb3BlbiBwb3NpdGlvbnMgKHd3dy5zbWFydGx5LmlvL2NhcmVlcnMpIGF0IFNtYXJ0bHkuaW8uDQoNCklmIHlvdSBoYXZlIGFscmVhZHkgc3RhcnRlZCBkaXNjdXNzaW9ucyB3aXRoIHVzLCBwbGVhc2Ugc2VuZCB1cyBhIG5vdGUgdG8gdGhlIGNvbnRhY3RFbWFpbCBhbmQgQ0MgdGhlIHBlcnNvbnMgeW91IGhhdmUgYmVlbiBpbiBjb250YWN0IHdpdGgu"
    }, console.log("Cool, you found this. Can you find more cool smartly stuff?"),
```

Now, before I continued I decided to do a quick search for certain keywords such as "email", "instruction", "goal", "next", "congratulations" and "good job". I found a regex for e-mail, however, looking at the contactEmail string I was fairly sure it wasn't regex but a hash. Then I looked at different hashing algorithms for decoding but none seem to fit the bill. I didn't want to share this with anyone on the web but I felt like I needed help. Then it hit me, the first help I received was from the Advanced REST Client that pointed me to base64. I searched for a base64 encode/decode website to give this a try since I've almost tried everything else and once I printed the contactEmail I felt extremely happy. That was it! It was base64 encoded!

## Putting it all together

The e-mail requested a Facebook ID which could only mean the Facebook pixel ID. Nice, I got the e-mail.

The instructions told me to CC my contact person and as the last person I spoke with told me to e-mail them I've sent an e-mail to the contactEmail and CC-ed my contact. 

### The only thing I didn't follow and why


# How could I have improved on this

I reached out to a few friends of mine asking a hypothetical question of "What would you guys have done if you landed on a page and there was a Facebook pixel on there and a JavaScript file?". Most focused on the JS file and said they would go to the console and would type "window" which was something I didn't think of so I noted it down. This would have made the approach a bit cleaner and faster so I gave it a shot. After a few seconds of scrolling, I knew what I needed to do.

![Window](https://i.imgur.com/vgrxAtJ.png)

![Window.Smartly](https://i.imgur.com/LQz9wp6.png)

Then I asked, "What would you do if you found a hash you needed to decode?" to which a friend asked, "Well, what is the first character of the hash?". He then explained that different hashes have a set rule of starting within a specific range. I noted that down and started reading up on it. 
