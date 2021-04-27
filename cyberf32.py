# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'cyber_f32'
insta_password = 'Tczcm1993,./'


# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)


with smart_run(session):

  """ Activity flow """		

  # general settings		
  session.set_dont_include(["friend1", "friend2", "friend3"])		


  # activity		
  session.like_by_tags(['bmw', 'n55', '435i', 'bmw435i', 'bmwf32', 'bimmer', 'bmw4series', 'bmwf30', 'bmwnation', 'bmwusa'], amount=10)
  session.set_dont_like(['nsfw', 'naked', 'nude', 'hotgirl', '🔞'])
  session.set_do_follow(True, percentage=70)
  session.set_do_comment(enabled=True, percentage=70)

  # Joining Engagement Pods
  
  session.set_comments(comments)

  comments = ['Nice shot🔥!',
        'You whip is on 🔥🔥🔥',
        'Your feeds are awesome 👍👌',
        'Just incredible!! 🔥🤩',
        'Your shot is on 🔥👌',
        'Love your posts!!',
        'Looks awesome!! 👌',
        'This is really dope!! 👌',
        ':raised_hands: Yes!']



  #*******************
  #Extra smart features
  #*******************
  
  session.set_quota_supervisor(enabled=True, peak_comments_daily=300, peak_commnets_hourly=50)
