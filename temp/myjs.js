window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        copyToClipboard: function (n, text) {
          if (!navigator.clipboard) {
            alert("copy not available, use ctrl-c");
            return;
          }
          if (n > 0) {
            navigator.clipboard.writeText(text).then(function() {
                alert("copied")
              }, function() {
                alert('copy error')
              });
          }
        }
    }
});


