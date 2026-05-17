# Context window

The context window is the input and output tokens combined.
As the conversation gets longer, as more and more messages get put into the conversation, the number of tokens used grows.

## The "Lost in the Middle" Problem

But the biggest issue with context windows is that the bigger they get, the more "lost in the middle" issues you get.

If we imagine a huge conversation, where these rings are the individual messages, the messages at the start of the history have quite a big impact on the output, and the ones at the end do too, but the stuff in the middle the LLM pays a bit less attention to.
