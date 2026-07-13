package Week3_OOP_Part2_Core_APIs.Day16_Interfaces;

/*
### **Q2: Multiple Interfaces**
Create two interfaces: `Playable` (with method `play()`) and `Pauseable` (with method `pause()`).
Create a class `MediaPlayer` that implements both interfaces.
*/

interface Playable {
    void play();
}

interface Pauseable {
    void pause();
}

class MediaPlayer implements Playable, Pauseable {

    @Override
    public void play() {
        System.out.println("Play the video.");
    }

    @Override
    public void pause() {
        System.out.println("Pause the video.");
    }
}

public class Task2 {
    public static void main(String[] args) {
        MediaPlayer media = new MediaPlayer();

        media.play();
        media.pause();
    }
}
