<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <!-- Bootswatch -->
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css"
        integrity="sha384-RxqHG2ilm4r6aFRpGmBbGTjsqwfqHOKy1ArsMhHusnRO47jcGqpIQqlQK/kmGy9R"
        crossorigin="anonymous"
      />

      <div class="row">
        <div class="col-sm-12">
          <p>Game Library 🎮</p>
          <hr />
          <br />

          <!-- Alert Message -->
          <button
            type="button"
            class="btn btn-success btn-sm"
            v-b-modal.game-modal
          >
            Add Game
          </button>
          <br />
          <br />

          <table class="table table-hover">
            <!-- Table Head -->
            <thead>
              <tr>
                <th scope="col">Title</th>
                <th scope="col">Genre</th>
                <th scope="col">Played</th>
                <th scope="col">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Identity V</td>
                <td>Honor</td>
                <td>Yes</td>
                <td>
                  <div class="btn-group" role="group">
                    <button type="button" class="btn btn-info btn-sm">
                      Update
                    </button>
                    <button type="button" class="btn btn-danger btn-sm">
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style></style>
