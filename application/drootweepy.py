# MIT License
# Copyright (c) 2015 Mihai Tabara
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

"""
Tool to scrap for tweets for a specific user
"""

from __future__ import absolute_import, print_function
from tweepy.error import TweepError
import tweepy

__all__ = (
    'Drootweepy'
)


class DrootweepyException(Exception):
    """Exception gets thrown should it come out from tweepy lib"""
    pass


class Drootweepy(object):
    """Create a new Drootweepy instance"""
    def __init__(self, consumer_key, consumer_secret,
                 access_token, access_token_secret,
                 no_of_tweets):

        self.no_of_tweets = no_of_tweets
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.secure = True
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def scrap_user(self, screen_name):
        try:
            ret = self.api.user_timeline(screen_name=screen_name,
                                        count=self.no_of_tweets,
                                        include_rts=1)
        except TweepError as e:
            raise DrootweepyException(e.message)
        return ret
