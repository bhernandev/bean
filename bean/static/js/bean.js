var config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: {y: 200}
        }
    },
    scene: {
        preload: preload,
        create: create
    }
};

var game = new Phaser.Game(config);

function preload () {
    this.load.setBaseURL("http://127.0.0.1:5000");
    this.load.image('seven', 'static/assets/7.png');
}

function create () {
    var seven = this.physics.add.image(400, 100, 'seven').setScale(0.3);
    seven.setVelocity(100,200);
    seven.setBounce(1, 1);
    seven.setCollideWorldBounds(true);
}
