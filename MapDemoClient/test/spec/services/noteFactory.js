'use strict';

describe('Service: noteFactory', function () {

  // load the service's module
  beforeEach(module('MapDemoClientApp'));

  // instantiate service
  var noteFactory;
  beforeEach(inject(function (_noteFactory_) {
    noteFactory = _noteFactory_;
  }));

  it('should do something', function () {
    expect(!!noteFactory).toBe(true);
  });

});
