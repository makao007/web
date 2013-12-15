    var data = [
        ['香港电台 第一台','http://202.177.192.119/radio1'],
        ['香港电台 第二台','http://202.177.192.119/radio2'],
        ['香港电台 第三台','http://202.177.192.119/radio3'],
        ['香港电台 第四台','http://202.177.192.119/radio4'],
        ['香港电台 第五台','http://202.177.192.119/radio5'],
        ['香港电台31','http://202.177.192.119/radio31'],
        ['香港电台33 [English]','http://202.177.192.119/radio33'],
        ['香港电台35','http://202.177.192.119/radio35'],
        ['香港电台pth','http://202.177.192.119/radiopth'],
    ];

    var bg = chrome.extension.getBackgroundPage();
    function start_play () {
        if (! bg.audio.paused) {
            bg.audio.load();
            document.getElementById('status').value = "Play";
            document.getElementById('title').innerHTML = "上次播放:" + data[parseInt(bg.order.value)][0];
        } else {
            bg.audio.play();
            if (bg.audio.src != "") {
                document.getElementById('title').innerHTML = "正在播放:" + data[parseInt(bg.order.value)][0];
                document.getElementById('status').value = "Stop";

            }
        }
    }
    function show_audio () {
        var tmp = document.getElementById('list');
        function play_audio (url, i) {
            var audio = bg.audio;
            bg.order.value = i;
            if (url=='') {
                audio.pause();
            } else {
                audio.src = url;
                audio.play();
                document.getElementById('status').value = "Stop";

            }
        }
        function update_show_list (n) {
            var lis = tmp.getElementsByTagName('li');
            for (var i=0; i<data.length; i++) {
                    lis[i].className = "";
            }
            document.getElementById('title').innerHTML = '正在播放: ' + data[n][0];
            lis[n].className = "current";
            if (! bg.audio.paused ) {
                document.getElementById('status').value = "Stop";
            }
        }

        for (var i=0; i<data.length; i++) {
            var li = document.createElement("li");
            li.innerHTML = data[i][0];
            li.i = i
            li.onclick = function () {
                play_audio(data[this.i][1], this.i);
                update_show_list (this.i);
            };
            tmp.appendChild (li);
        }
        if (bg.order.value != -1) {
            update_show_list (parseInt(bg.order.value));
        }

    }

    show_audio();
    document.getElementById('status').onclick = start_play;

