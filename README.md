# codeshare-server

Simple Flask SocketIO server application for broadcasting a code-snippets, basically a live gist. Viewers use codemirror formatting.

## TODO
Lots. Only basic functionality implemented.
- [x] Viewer code formatting
- [?] Data compression: newstate vs oldstate: compute a delta/diff.. something and then send the diff. Every ... seconds the client computes a hash of it's current data and sends to server. Server compares to current state hash and if not identical marks client as out of sync and sends full state. Same goes for server to client. If server gets out of sync the client retransmits all.
- [ ] Authentication
- [ ] (Locked) Rooms
- [ ] Basic admin
- [ ] Chat
- [ ] (Auto)Copy
- [ ] Highlight broadcasting

## Future
VSCode & Thonny plugin.