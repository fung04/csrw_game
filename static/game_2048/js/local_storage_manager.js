function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

window.fakeStorage = {
  _data: {},

  setItem: function (id, val) {
    return this._data[id] = String(val);
  },

  getItem: function (id) {
    return this._data.hasOwnProperty(id) ? this._data[id] : undefined;
  },

  removeItem: function (id) {
    return delete this._data[id];
  },

  clear: function () {
    return this._data = {};
  }
};

function LocalStorageManager() {
  this.bestScoreKey = "bestScore";
  this.gameStateKey = "gameState";

  var supported = this.localStorageSupported();//receive TRUE of FALSE from localStorageSupported function
  this.storage = supported ? window.localStorage : window.fakeStorage;

  // fetch the best score from server
  fetch("/game-2048/get-result/")
    .then(response => response.json())
    .then(serverGameState => {

      // set the best score fom serverGameState
      this.storage.setItem(this.bestScoreKey, parseInt(serverGameState.best));

      // check if serverGameState is empty
      if (Object.keys(serverGameState).length > 0) {
        this.storage.removeItem(this.gameStateKey);
        //set game state to serverGameState
        this.storage.setItem(this.gameStateKey, JSON.stringify(serverGameState));
      } else {
        console.log("no game_flappy state");
        this.storage.removeItem(this.gameStateKey);
        // set game state to null
        this.gameStateKey = "gameState";
      }
    });
}

//check support local storage or not
LocalStorageManager.prototype.localStorageSupported = function () {
  var testKey = "test";

  try {
    var storage = window.localStorage;
    storage.setItem(testKey, "1");
    storage.removeItem(testKey);
    return true;
  } catch (error) {
    return false;
  }
};

// Best score getters/setters
LocalStorageManager.prototype.getBestScore = function () {
  return this.storage.getItem(this.bestScoreKey) || 0;
};


LocalStorageManager.prototype.setBestScore = function (score) {
  this.storage.setItem(this.bestScoreKey, score);
};

// Game state getters/setters and clearing
LocalStorageManager.prototype.getGameState = function () {

  var stateJSON = this.storage.getItem(this.gameStateKey);

  return stateJSON ? JSON.parse(stateJSON) : null;
};

LocalStorageManager.prototype.setGameState = function (gameState) {
  this.storage.setItem(this.gameStateKey, JSON.stringify(gameState));
};

LocalStorageManager.prototype.clearGameState = function () {
  this.storage.removeItem(this.gameStateKey);
};

