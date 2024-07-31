# FAQ

## Which games do you play with this?

Mostly games that lack gamepad support.  
That includes older games and many indie games.

## Any popular titles?

I've played [Cassette Beasts](https://www.cassettebeasts.com/), [Dead Cells](https://dead-cells.com/) and [Asphalt 9](https://asphaltlegends.com/) with it.

## The default mapping doesn't work for me. What do I do?

You can:

1. Change the controls in-game, if the game supports it.
2. Change the mapping in the source code and build the server yourself.

With a bit of remapping, almost everything is playable.  
The server will eventually have a GUI for changing the mapping.

## I want to change the colour of the gamepad

This is already implemented on the main branch. The feature will be shipped in the next release.

If you are building the app yourself, you can add more base colours in [app/src/main/java/io/github/kitswas/virtualgamepadmobile/data/BaseColor.kt](https://github.com/kitswas/VirtualGamePad-Mobile/blob/592ef996af1b61f2cf848e3e01b97d2a1098f493/app/src/main/java/io/github/kitswas/virtualgamepadmobile/data/BaseColor.kt).  
The app will generate tonal variations of the base colour for the rest of the UI.

## You mentioned cool upcoming features. When will they be available?

As soon as I have time to work on it. :)  
If you want them sooner, you can _contribute to the project_.
