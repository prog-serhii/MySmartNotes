from neo4j import GraphDatabase, Driver

from graph.application.repositories import GraphRepository


class Neo4jGraphRepository(GraphRepository):

    def __init__(self, driver: Driver) -> None:
        self.driver = driver

    def create_tag_node(self, tag_id):
        def _create_tag_node(tx, note_id):
            return tx.run('CREATE (tag:Tag {tag_id: $tag_id}', tag_id=tag_id)

    def remove_tag_node(self, note_id):
        pass

    def create_note_node(self, tag_id):
        def _create_note_node(tx, note_id):
            return tx.run('CREATE (note:Note {note_id: $note_id}', note_id=note_id)

    def remove_note_node(self, note_id):
        pass

    def create_relationship_from_note_to_tag(self, note_id, tag_id):
        def create_relationship_from_note_to_tag(tx, note_id, tag_id):
            return tx.run(
                """
                MATCH
                    (note:Note),
                    (tag:Tag)
                WHERE note.note_id = $note_id ANS tag.tag_id = $tag_id
                CREATE (note)-[relationship:CONTAIN]-(tag)
                """, note_id=note_id, tag_id=tag_id
            )

    def remove_relationship_from_note_to_tag(self, note_id, tag_id):
        pass
