import XCTest
@testable import ProfileRefreshDemo

final class ProfileStoreTests: XCTestCase {
    func testMissingFileReturnsExplicitLegacyFallback() {
        let url = URL.temporaryDirectory.appending(path: UUID().uuidString)
        XCTAssertEqual(ProfileStore(fileURL: url).load(), .empty)
    }

    func testPersistedDisplayNameRoundTrips() throws {
        let url = URL.temporaryDirectory.appending(path: UUID().uuidString).appending(path: "profile.json")
        let store = ProfileStore(fileURL: url)
        let expected = Profile(id: "1", displayName: "Ada")
        try store.save(expected)
        XCTAssertEqual(store.load(), expected)
    }
}
