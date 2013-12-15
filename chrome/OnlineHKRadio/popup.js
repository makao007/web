    var data = [
        ['香港电台1','http://202.177.192.119/radio1'],
        ['香港电台2','http://202.177.192.119/radio2'],
        ['香港电台3','http://202.177.192.119/radio3'],
        ['香港电台4','http://202.177.192.119/radio4'],
        ['香港电台5','http://202.177.192.119/radio5'],
        ['香港电台31','http://202.177.192.119/radio31'],
        ['香港电台33 [English]','http://202.177.192.119/radio33'],
        ['香港电台35','http://202.177.192.119/radio35'],
        ['香港电台pth','http://202.177.192.119/radiopth'],
        ['停止',''],
    ];

    var bg = chrome.extension.getBackgroundPage();
    function show_audio () {
        var tmp = document.getElementById('list');
        function play_audio (url) {
            var audio = bg.audio;
            if (url=='') {
                audio.pause();
            } else {
                audio.src = url;
                audio.play();
            }
        }
        function update_show_list (n) {
            var lis = tmp.getElementsByTagName('li');
            for (var i=0; i<data.length; i++) {
                    lis[i].className = "";
            }
            lis[n].className = "current";
        }


        for (var i=0; i<data.length; i++) {
            var li = document.createElement("li");
            li.innerHTML = data[i][0];
            li.i = i
            li.onclick = function () {
                document.getElementById('title').innerHTML = '正在播放:' + data[this.i][0];
                play_audio(data[this.i][1]);
                update_show_list (this.i);
            };
            tmp.appendChild (li);
        }
    }

    show_audio();

